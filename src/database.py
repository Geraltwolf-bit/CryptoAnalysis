import psycopg2
import configparser
import os

def get_db_connection():
    #establish and return a connection to the PostgreSQL database
    #read configuration:
    config = configparser.ConfigParser()
    config.read("config/database.conf")

    #get database credentials
    db_config = config['postgresql']
    
    try:
        connection = psycopg2.connect(
            host = db_config['host'],
            database = db_config['database'],
            user = db_config['user'],
            password = db_config['password'],
            port = db_config['port']            
        )
        print("Database connection successful")
        return connection
    except Exception as e:
        print(f" Database connection failed: {e}")
        return None
    
def test_connection():
    connection = get_db_connection()
    if connection:
        connection.close()
        print("Connection test passed!")
    else:
        print("Connection test failed!")

if __name__=='__main__':
    test_connection()


def create_tables():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        with open("sql/create_tables.sql") as file:
            sql_script = file.read()

        cursor.execute(sql_script)
        connection.commit()
        print("Tables created successfully.")

        cursor.execute("""
                       SELECT column_name, data_type, is_nullable
                       FROM information_schema.columns
                       WHERE table_name = 'market_sentiment'
                       """)
        print("\n Table structure:")
        for column in cursor.fetchall():
            print(f" {column[0]} ({column[1]}) - Nullable: {column[2]}")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f" Error creating tables: {e}")

    if __name__=='__main__':
        test_connection()
        create_tables()