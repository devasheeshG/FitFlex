# Path: utils/database.py
# Description: This file contains the code to connect to a Postgres database and execute queries.

import psycopg2
from typing import List

class Postgres:
    def __init__(self, uri: str, database: str):
        """This class is used to connect to a Postgres database and execute queries.

        Args:
            uri (str): `postgresql://[user[:password]@][netloc][:port][/auth_dbname]`
            database (str): The name of the database to use for executing queries.
        """
        self.uri = uri
        self.database = database
        self.conn = None
        self.cursor = None
        
        """Connect to the PostgreSQL database."""
        try:
            self.conn = psycopg2.connect(self.uri + '/postgres')
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            
            # Check if the database exists, if not, create it
            self.cursor.execute(f"SELECT 1 FROM pg_database WHERE datname='{self.database}'")
            if not self.cursor.fetchone():
                self.cursor.execute(f"CREATE DATABASE {self.database}")
                # self.conn.commit()
                
            # Reconnect to the new database
            self.conn.close()
            self.conn = psycopg2.connect(f"{self.uri}/{self.database}")
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            
            # Create the tables
            """Setup the Postgres database tables."""
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS users (
                    name VARCHAR(50) NOT NULL,
                    email VARCHAR(50) NOT NULL PRIMARY KEY,
                    password_hash BYTEA NOT NULL,
                    salt BYTEA NOT NULL,
                    gender VARCHAR(10) NOT NULL,
                    age INT NOT NULL,
                    weight FLOAT NOT NULL,
                    height INT NOT NULL,
                    goal VARCHAR(50) NOT NULL,
                    activity_level VARCHAR(50) NOT NULL,
                    joining_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )"""
            )
            
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL: {e}")
            raise
        
    def close(self):
        """Close the connection to the PostgreSQL database."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
    
    def __del__(self):
        self.close()
        
    def __str__(self):
        return f"Postgres(uri={self.uri}, database={self.database})"


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    if not os.getenv("POSTGRES_URI") or not os.getenv("POSTGRES_DATABASE"):
        raise ValueError("Please set the POSTGRES_URI and POSTGRES_DATABASE environment variables.")
    
    postgress = Postgres(uri=os.getenv("POSTGRES_URI"), database=os.getenv("POSTGRES_DATABASE"))
    postgress.close()
    print("Postgres connection successful.")
