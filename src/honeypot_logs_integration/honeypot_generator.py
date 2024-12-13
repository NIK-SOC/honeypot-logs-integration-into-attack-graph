# honeypot_generator.py
# Script to generate synthetic honeypot logs for testing purposes

import random
import json
from datetime import datetime, timedelta

# Attack types, corresponding target services, and example payloads
ATTACK_SCENARIOS = {
    "SSH brute-force": {
        "services": ["SSH"],
        "payloads": [
            {"type": "credentials", "content": '"username": "admin", "password": "password123"'},
            {"type": "credentials", "content": '"username": "root", "password": "123456"'},
            {"type": "credentials", "content": '"username": "user", "password": "letmein"'}
        ]
    },
    "SQL injection": {
        "services": ["MySQL", "PostgreSQL"],
        "payloads": [
            {"type": "query", "content": "' OR '1'='1' -- "},
            {"type": "query", "content": "UNION SELECT username, password FROM users -- "},
            {"type": "query", "content": "'; DROP TABLE users; --"}
        ]
    },
    "DDoS": {
        "services": ["HTTP", "DNS"],
        "payloads": [
            {"type": "request", "content": "GET / HTTP/1.1\\nHost: targetsite.com\\nUser-Agent: BotNet"},
            {"type": "packet", "content": "Massive UDP flood targeting port 53"},
            {"type": "request", "content": "Repeated HTTP POST requests to /login endpoint"}
        ]
    }
}

# Function to generate a random IP address
def generate_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Function to generate a random timestamp within the last 30 days
def generate_timestamp():
    now = datetime.now()
    past = now - timedelta(days=30)
    random_time = past + timedelta(seconds=random.randint(0, int((now - past).total_seconds())))
    return random_time.isoformat()

# Function to generate a random log entry with consistent payload format
def generate_log_entry():
    # Randomly select an attack type and corresponding details
    attack_type = random.choice(list(ATTACK_SCENARIOS.keys()))
    details = ATTACK_SCENARIOS[attack_type]
    target_service = random.choice(details["services"])
    payload = random.choice(details["payloads"])

    return {
        "timestamp": generate_timestamp(),
        "source_ip": generate_ip(),
        "attack_type": attack_type,
        "target_service": target_service,
        "payload": payload
    }

# Function to generate a batch of synthetic logs
def generate_logs(num_logs=100):
    return [generate_log_entry() for _ in range(num_logs)]

# Main script
if __name__ == "__main__":
    # Set the seed
    random.seed(42)

    # Number of logs to generate
    num_logs = 100

    # Generate synthetic honeypot logs
    logs = generate_logs(num_logs)

    # Save logs to a JSON file
    output_file = "synthetic_honeypot_logs.json"
    with open(output_file, "w") as f:
        json.dump(logs, f, indent=4)

    print(f"Synthetic honeypot logs ({num_logs}) generated and saved to '{output_file}'")
