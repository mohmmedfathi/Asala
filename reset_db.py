import os
import psycopg2
from urllib.parse import urlparse
import dj_database_url

# Get your database URL from Django settings
DATABASE_URL = 'postgresql://asala_postgres_user:wv209HQOYUTr7MDKClmIcq9N68xrO3sc@dpg-cvfi5t5umphs73daajh0-a.oregon-postgres.render.com/asala_postgres'

def reset_database():
    # Parse the database URL
    db_info = urlparse(DATABASE_URL)
    
    # Extract connection parameters
    dbname = db_info.path[1:]  # remove leading slash
    user = db_info.username
    password = db_info.password
    host = db_info.hostname
    port = db_info.port

    # Connect to postgres database (default db that always exists)
    conn = psycopg2.connect(
        dbname='postgres',  # Connect to default admin DB
        user=user,
        password=password,
        host=host,
        port=port
    )
    conn.autocommit = True  # Required for dropping databases
    
    try:
        with conn.cursor() as cursor:
            # Terminate all connections to the target database
            cursor.execute(f"""
                SELECT pg_terminate_backend(pg_stat_activity.pid)
                FROM pg_stat_activity
                WHERE pg_stat_activity.datname = '{dbname}'
                AND pid <> pg_backend_pid();
            """)
            
            # Drop the database
            cursor.execute(f"DROP DATABASE IF EXISTS {dbname};")
            
            # Recreate the database
            cursor.execute(f"CREATE DATABASE {dbname} WITH OWNER {user};")
            
            print(f"Successfully reset database: {dbname}")
            
    except Exception as e:
        print(f"Error resetting database: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    print("WARNING: This will completely DROP and RECREATE your database.")
    print(f"Target database: {DATABASE_URL}")
    confirm = input("Are you sure you want to proceed? (yes/no): ")
    
    if confirm.lower() == 'yes':
        reset_database()
    else:
        print("Database reset cancelled.")