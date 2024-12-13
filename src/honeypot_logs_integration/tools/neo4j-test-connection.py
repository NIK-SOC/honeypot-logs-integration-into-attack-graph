# neo4j-test-connection.py
# Script to test the connection to a Neo4j database

from dotenv import load_dotenv
import os
from neo4j import GraphDatabase

# Load environment variables from .env file
load_dotenv()

# Neo4j connection details
uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")
database = os.getenv("NEO4J_DATABASE")

if not uri or not username or not password or not database:
    raise ValueError("Environment variables are not set properly.")

driver = GraphDatabase.driver(uri, auth=(username, password))

def test_connection():
    try:
        with driver.session(database=database) as session:
            greeting = session.run("RETURN 'Connected to the database securely!' AS message").single()
            print(greeting["message"])
    except Exception as e:
        print("Failed to connect to Neo4j:", str(e))
    finally:
        driver.close()

test_connection()
