# transform_logs_to_stix.py
# Script to transform synthetic honeypot logs into STIX format

import json
from datetime import datetime
import uuid
import base64
import hashlib
from stix2 import (
    ObservedData, AttackPattern, Identity, IPv4Address, NetworkTraffic,
    Relationship, Bundle, Artifact
)
from stix2.exceptions import InvalidValueError
from dateutil import parser as date_parser

# Function to load synthetic honeypot logs from JSON file
def load_synthetic_logs(file_path):
    with open(file_path, 'r') as f:
        logs = json.load(f)
    return logs

# Function to create STIX objects from a single log entry
def create_stix_objects(log_entry, creator_identity_id):
    stix_objects = []

    # Create AttackPattern object based on attack_type (SDO)
    attack_pattern = AttackPattern(
        id=f"attack-pattern--{uuid.uuid4()}",
        name=log_entry['attack_type'],
        created_by_ref=creator_identity_id,
        created=datetime.utcnow(),
        modified=datetime.utcnow(),
    )
    stix_objects.append(attack_pattern)

    # Create Identity object for the attacker (SDO)
    attacker_identity = Identity(
        id=f"identity--{uuid.uuid4()}",
        name="Unknown Attacker",
        identity_class="individual",
        created_by_ref=creator_identity_id,
        created=datetime.utcnow(),
        modified=datetime.utcnow(),
    )
    stix_objects.append(attacker_identity)

    # Create IPv4Address object for source_ip (SCO)
    ipv4 = IPv4Address(
        id=f"ipv4-addr--{uuid.uuid4()}",
        value=log_entry['source_ip'],
    )
    stix_objects.append(ipv4)

    # Parse timestamp into datetime object
    timestamp = date_parser.parse(log_entry['timestamp'])

    # Create NetworkTraffic object from payload (SCO)
    payload = log_entry['payload']
    network_traffic_kwargs = {
        "id": f"network-traffic--{uuid.uuid4()}",
        "protocols": ["tcp"],
        "src_ref": ipv4.id,
        "dst_port": 22 if log_entry['target_service'] == "SSH" else None,
        "src_port": None,
        "start": timestamp,
        "end": timestamp,  # Since the traffic is not ongoing, start and end are the same
        "is_active": False,  # Must be False if 'end' is present
    }

    # Handle extensions based on attack type
    if log_entry['attack_type'] == "DDoS":
        # For DDoS attacks, include the http-request-ext with required fields
        network_traffic_kwargs['extensions'] = {
            "http-request-ext": {
                "request_method": "GET",
                "request_value": payload.get('content', ''),
                "request_version": "HTTP/1.1",
                "request_header": {
                    "Host": "targetsite.com",
                    "User-Agent": "BotNet"
                }
            }
        }
    elif log_entry['attack_type'] == "SQL injection":
        # For SQL injection, create an Artifact for the message body
        message_body_content = payload.get('content', '')
        message_body_encoded = base64.b64encode(message_body_content.encode('utf-8')).decode('utf-8')

        # Compute the SHA-256 hash of the message body content
        sha256_hash = hashlib.sha256(message_body_content.encode('utf-8')).hexdigest()

        # Create Artifact object (SCO), remove 'created', 'modified', 'created_by_ref'
        message_body_artifact = Artifact(
            id=f"artifact--{uuid.uuid4()}",
            mime_type="application/sql",
            payload_bin=message_body_encoded,
            hashes={
                "SHA-256": sha256_hash
            },
        )
        stix_objects.append(message_body_artifact)

        # Include the http-request-ext with message_body_length and message_body_data_ref
        network_traffic_kwargs['extensions'] = {
            "http-request-ext": {
                "request_method": "POST",
                "request_value": "/login",
                "request_version": "HTTP/1.1",
                "request_header": {
                    "Host": "targetdatabase.com",
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                "message_body_length": len(message_body_content.encode('utf-8')),
                "message_body_data_ref": message_body_artifact.id
            }
        }
    # No extensions for SSH brute-force attacks

    # Create NetworkTraffic object
    network_traffic = NetworkTraffic(**network_traffic_kwargs)
    stix_objects.append(network_traffic)

    # Create ObservedData object (SDO)
    observed_data = ObservedData(
        id=f"observed-data--{uuid.uuid4()}",
        created_by_ref=creator_identity_id,
        first_observed=timestamp,
        last_observed=timestamp,
        number_observed=1,
        objects={
            "0": ipv4,
            "1": network_traffic,
        },
        created=datetime.utcnow(),
        modified=datetime.utcnow(),
    )
    stix_objects.append(observed_data)

    # Create relationships (SDOs)
    rel_attacker_ipv4 = Relationship(
        id=f"relationship--{uuid.uuid4()}",
        created_by_ref=creator_identity_id,
        source_ref=attacker_identity.id,
        relationship_type="uses",
        target_ref=ipv4.id,
        created=datetime.utcnow(),
        modified=datetime.utcnow(),
    )
    stix_objects.append(rel_attacker_ipv4)

    rel_observed_attack = Relationship(
        id=f"relationship--{uuid.uuid4()}",
        created_by_ref=creator_identity_id,
        source_ref=observed_data.id,
        relationship_type="related-to",
        target_ref=attack_pattern.id,
        created=datetime.utcnow(),
        modified=datetime.utcnow(),
    )
    stix_objects.append(rel_observed_attack)

    return stix_objects

# Main function to process logs and create STIX bundle
def main():
    # Load synthetic logs
    logs = load_synthetic_logs('synthetic_honeypot_logs.json')

    all_stix_objects = []

    # Create an Identity object for the creator (your organization) (SDO)
    creator_identity = Identity(
        id=f"identity--{uuid.uuid4()}",
        name="Your Organization",
        identity_class="organization",
        created=datetime.utcnow(),
        modified=datetime.utcnow(),
    )
    all_stix_objects.append(creator_identity)
    creator_identity_id = creator_identity.id

    for log_entry in logs:
        try:
            stix_objects = create_stix_objects(log_entry, creator_identity_id)
            all_stix_objects.extend(stix_objects)
        except InvalidValueError as e:
            print(f"Error processing log entry: {e}")
            continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue

    # Create a STIX Bundle
    bundle = Bundle(objects=all_stix_objects)

    # Export the STIX Bundle to a JSON file
    output_file = 'honeypot_logs_stix.json'
    with open(output_file, 'w') as f:
        f.write(bundle.serialize(pretty=True))

    print(f"STIX bundle created and saved to '{output_file}'")

if __name__ == '__main__':
    main()
