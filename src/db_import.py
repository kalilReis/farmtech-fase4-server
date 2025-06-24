import oracledb
import csv
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

dsn = os.getenv("DB_DSN")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

def import_csv_to_db(csv_file_path):
    connection = oracledb.connect(user=user, password=password, dsn=dsn)
    cursor = connection.cursor()
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []
        for row in reader:
            timestamp = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')
            rows.append((
                timestamp,
                row['sensor_id'],
                int(row['hour']),
                float(row['temp']),
                float(row['humidity_air']),
                float(row['moisture_soil']),
                int(row['irrigated'])
            ))
        try:
            cursor.executemany("""
                INSERT INTO irrigation_data (timestamp, sensor_id, hour, temp, humidity_air, moisture_soil, irrigated)
                VALUES (:1, :2, :3, :4, :5, :6, :7)
            """, rows)
            connection.commit()
            print(f"{cursor.rowcount} linhas inseridas com sucesso.")
        except oracledb.DatabaseError as e:
            print("Erro ao inserir dados:", e)
        finally:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    import_csv_to_db('../data/irrigation_data.csv')
