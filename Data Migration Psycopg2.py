import json
import psycopg2
import urllib.request

# Connect to the database
def lambda_handler(event, context):
    db = psycopg2.connect(
        host='database-1.cl80waky6nkw.ap-south-1.rds.amazonaws.com',
        database='issdata',
        user='postgres',
        password='********'
    )

    create_table_query = """
        CREATE TABLE IF NOT EXISTS iss_position (
            id SERIAL PRIMARY KEY,
            latitude INTEGER,
            longitude INTEGER,
            timestamp INTEGER,
            message VARCHAR(255)
        )
    """
    
    cursor = db.cursor()
    cursor.execute(create_table_query)
    db.commit()

    # Fetch ISS position data from API
    api_url = 'http://api.open-notify.org/iss-now.json'
    with urllib.request.urlopen(api_url) as response:
        data = json.loads(response.read().decode())

    # Extract values
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp']
    message = data['message']

    insert_query = """
        INSERT INTO iss_position (latitude, longitude, timestamp, message)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (latitude, longitude, timestamp, message))
    db.commit()

    db.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
