import pandas as pd
import psycopg2
import toml
import ssl

# Load the PostgreSQL connection details from the secrets.toml file
secrets_path = "./.streamlit/secrets.toml"
with open(secrets_path, "r") as file:
    secrets = toml.load(file)

postgres_user = secrets["connections"]["mydb"]["username"]
postgres_password = secrets["connections"]["mydb"]["password"]
postgres_host = secrets["connections"]["mydb"]["host"]
postgres_port = secrets["connections"]["mydb"]["port"]
postgres_db = secrets["connections"]["mydb"]["database"]

# SSL context setup
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

print("Connecting to the PostgreSQL database...")

# Establish a connection to PostgreSQL using the extracted values and SSL
conn = psycopg2.connect(
    user=postgres_user,
    password=postgres_password,
    host=postgres_host,
    port=postgres_port,
    database=postgres_db,
    sslmode='require',
    ssl=context
)
print("Connected successfully!")

# Drop the "incidents" table if it already exists
with conn.cursor() as cursor:
    print("Dropping the 'incidents' table if it already exists...")
    sql_drop_table = "DROP TABLE IF EXISTS incidents"
    cursor.execute(sql_drop_table)

print("Table dropped (if it existed).")

# Create the "incidents" table with the desired schema
with conn.cursor() as cursor:
    print("Creating the 'incidents' table...")
    sql_create_table = """
    CREATE TABLE incidents (
        "Unique Key" INTEGER PRIMARY KEY,
        "Complaint Type" TEXT,
        "Created Date" TIMESTAMP,
        "Borough" TEXT,
        "Longitude" FLOAT,
        "Latitude" FLOAT
    )
    """
    cursor.execute(sql_create_table)
print("Table created successfully!")

# Read the CSV file into a pandas DataFrame
csv_file_path = "nyc_2022_june_selected_columns.csv"  # Replace with the actual path to your CSV file
print(f"Reading data from the CSV file: {csv_file_path}")
df = pd.read_csv(csv_file_path)
print("Data read from the CSV file successfully.")

# Data insertion into the "incidents" table
with conn.cursor() as cursor:
    print("Inserting data into the 'incidents' table...")
    sql_insert = f"INSERT INTO incidents VALUES (%s, %s, %s, %s, %s, %s)"
    for index, row in df.iterrows():
        values = (row["Unique Key"], row["Complaint Type"], row["Created Date"],
                  row["Borough"], row["Longitude"], row["Latitude"])
        try:
            cursor.execute(sql_insert, values)
        except Exception as e:
            print(f"Error while inserting row {index + 1}: {e}")
            print(f"Data: {values}")

    conn.commit()  # Commit the changes
print("Data insertion into the 'incidents' table complete!")

# Make sure to close the connection
conn.close()
print("Connection to the PostgreSQL database closed.")
