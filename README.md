
# Honeypot Logs Integration into Attack Graph

This project facilitates the integration of honeypot logs into a Neo4j graph database using the STIX data model. By mapping honeypot data to STIX objects and relationships, it enables the visualization and analysis of attack patterns within a graph database.

## Features

- **Data Generation**: Generates honeypot logs.
- **STIX Mapping**: Converts honeypot logs into STIX-compliant objects and relationships.
- **Graph Database Integration**: Imports STIX data into a Neo4j database for advanced querying and visualization.

## Prerequisites

- Python 3.8 or higher
- Neo4j 4.0 or higher

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/NIK-SOC/honeypot-logs-integration-into-attack-graph.git
   cd honeypot-logs-integration-into-attack-graph
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Neo4j**:

   - Ensure Neo4j is installed and running.

4. **Configure a `.env` file**
   - Create a `.env` file
   - Set these variables below:
      - `NEO4J_URI`
      - `NEO4J_PASSWORD`
      - `NEO4J_USER`
      - `NEO4J_DATABASE`

## Usage

1. **Generate Honeypot Logs**:
   
   ```bash
   python src/honeypot_logs_integration/honeypot_generator.py
   ```

   Honeypot log files will be generated in the `.tmp/` directory as `synthetic_honeypot_logs.json`.

2. **Transform Honeypot Logs Into STIX Model**:

   ```bash
   python src/honeypot_logs_integration/transform_logs_to_stix.py
   ```

   Transformed honeypot logs will be saved in the `.tmp/` directory as `honeypot_logs_stix.json`.

   This script will parse the logs, map them to STIX objects.

3. **Import Honeypot logs into Neo4j**

   ```bash
   python src/honeypot_logs_integration/loading-into-neo4j.py
   ```

   Use Neo4j Browser or any compatible tool to explore the imported data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
