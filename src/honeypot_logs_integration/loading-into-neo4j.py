# loading-into-neo4j.py
# Script to load STIX data into Neo4j for visualization and analysis

from neo4j import GraphDatabase
from stix2 import parse
from dotenv import load_dotenv
import json
import os

# Load environment variables from .env file
load_dotenv()

# Neo4j connection details
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Function to create nodes and relationships in Neo4j
def import_stix_to_neo4j(stix_bundle, driver):
    with driver.session() as session:
        for obj in stix_bundle.objects:
            # Handle SDOs
            if obj.type == 'identity':
                session.write_transaction(create_identity_node, obj)
            elif obj.type == 'attack-pattern':
                session.write_transaction(create_attack_pattern_node, obj)
            elif obj.type == 'observed-data':
                session.write_transaction(create_observed_data_node, obj)
            elif obj.type == 'relationship':
                session.write_transaction(create_relationship, obj)
            # Handle SCOs
            elif obj.type == 'ipv4-addr':
                session.write_transaction(create_ipv4_node, obj)
            elif obj.type == 'network-traffic':
                session.write_transaction(create_network_traffic_node, obj)
            elif obj.type == 'artifact':
                session.write_transaction(create_artifact_node, obj)
            else:
                # Handle other types as needed
                pass

# Helper function to flatten dictionaries
def flatten_dict(d, parent_key='', sep='_'):
    items = []
    if isinstance(d, dict):
        for k, v in d.items():
            # Exclude certain keys if necessary
            if k in ['extensions', 'objects']:  # Adjust as needed
                continue
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                # Recursively flatten nested dictionaries
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            elif isinstance(v, list):
                # Convert lists to strings or handle appropriately
                items.append((new_key, str(v)))
            else:
                items.append((new_key, v))
    else:
        # If d is not a dict, return it as a single-item dictionary
        items.append((parent_key, d))
    return dict(items)

# Functions to create nodes
def create_identity_node(tx, obj):
    props = json.loads(obj.serialize())
    props = flatten_dict(props)
    tx.run(
        "MERGE (n:Identity {id: $id}) "
        "SET n += $props",
        id=obj.id,
        props=props
    )

def create_attack_pattern_node(tx, obj):
    props = json.loads(obj.serialize())
    props = flatten_dict(props)
    tx.run(
        "MERGE (n:AttackPattern {id: $id}) "
        "SET n += $props",
        id=obj.id,
        props=props
    )

def create_observed_data_node(tx, obj):
    props = json.loads(obj.serialize())
    props = flatten_dict(props)
    tx.run(
        "MERGE (n:ObservedData {id: $id}) "
        "SET n += $props",
        id=obj.id,
        props=props
    )
    # Create relationships to SCOs
    for key, sco in obj.objects.items():
        if isinstance(sco, dict) and 'id' in sco:
            tx.run(
                "MATCH (o:ObservedData {id: $obs_id}), (s {id: $sco_id}) "
                "MERGE (o)-[:OBSERVED]->(s)",
                obs_id=obj.id,
                sco_id=sco['id']
            )

def create_ipv4_node(tx, obj):
    props = json.loads(obj.serialize())
    props = flatten_dict(props)
    tx.run(
        "MERGE (n:IPv4Address {id: $id}) "
        "SET n += $props",
        id=obj.id,
        props=props
    )

def create_network_traffic_node(tx, obj):
    props = json.loads(obj.serialize())
    props = flatten_dict(props)
    tx.run(
        "MERGE (n:NetworkTraffic {id: $id}) "
        "SET n += $props",
        id=obj.id,
        props=props
    )
    # Handle extensions if needed

def create_artifact_node(tx, obj):
    props = json.loads(obj.serialize())
    props = flatten_dict(props)
    tx.run(
        "MERGE (n:Artifact {id: $id}) "
        "SET n += $props",
        id=obj.id,
        props=props
    )

# Function to create relationships
def create_relationship(tx, obj):
    relationship_type = obj.relationship_type.upper().replace('-', '_')
    props = json.loads(obj.serialize())
    props = flatten_dict(props)
    tx.run(
        "MATCH (a {id: $source_id}), (b {id: $target_id}) "
        "MERGE (a)-[r:" + relationship_type + "]->(b) "
        "SET r += $props",
        source_id=obj.source_ref,
        target_id=obj.target_ref,
        props=props
    )

def main():
    # Load the STIX bundle from the JSON file
    with open('sample_data/honeypot_logs_stix.json', 'r') as f:
        stix_bundle = json.load(f)
    # Parse the bundle
    bundle = parse(stix_bundle, allow_custom=True)
    
    # Connect to Neo4j
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    # Import STIX data into Neo4j
    import_stix_to_neo4j(bundle, driver)
    
    # Close the driver
    driver.close()
    print("Data import complete.")

if __name__ == "__main__":
    main()
