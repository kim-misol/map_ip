import psycopg2
from instance import config
# Psycopg is a PostgreSQL adapter for the Python programming language.
# This tool allows us to connect the capabilities of the Python language and libraries
# to obtain, manipulate, input, and update data stored in a PostgreSQL database.
# Using psycopg2 module to communicate with PostgreSQL.

try:
    # create a connection to a PostgreSQL database instance. This returns a PostgreSQL Connection Object.
    connection = psycopg2.connect(user=f"{config.PSQL_USER}",
                                  password=f"{config.PSQL_PW}",
                                  host=f"{config.PSQL_HOST}",
                                  port=f"{config.PSQL_PORT}",
                                  database=f"{config.PSQL_DB}")
    # create a cursor object which allows us to execute PostgreSQL command through Python source code.
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    # It is always good practice to close the cursor and connection object
    # once your work gets completed to avoid database issues.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")