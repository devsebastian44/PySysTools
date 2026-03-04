import mysql.connector
import os
from typing import List, Any


class DatabaseConnector:
    """
    Handles database connections and queries.
    """
    def __init__(self, host: str = None, user: str = None,
                 password: str = None, database: str = None):
        # Use env vars or defaults (WARNING: Defaults are for dev only)
        self.host = host or os.getenv("DB_HOST", "mysql-5707.dinaserver.com")
        self.user = user or os.getenv("DB_USER", "mouredev_read")
        self.password = password or os.getenv("DB_PASS", "mouredev_pass")
        self.database = database or os.getenv("DB_NAME", "moure_test")
        self.connection = None

    def connect(self):
        """Establishes the database connection."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print(f"Connected to {self.database} at {self.host}")
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            raise

    def execute_query(self, query: str) -> List[Any]:
        """Executes a SQL query and returns results."""
        if not self.connection:
            self.connect()

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            return []
        finally:
            cursor.close()

    def close(self):
        """Closes the connection."""
        if self.connection:
            self.connection.close()
            print("Connection closed.")


if __name__ == "__main__":
    # Example usage
    db = DatabaseConnector()
    try:
        db.connect()  # Ensure connection is established for the example
        results = db.execute_query("SELECT * FROM `challenges` LIMIT 5")
        for row in results:
            print(row)
    except Exception as e:
        print(f"Failed to run example: {e}")
    finally:
        db.close()