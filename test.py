from crypsDb import JSONDatabase
from datetime import datetime

# Create a JSONDatabase instance
db = JSONDatabase('database')

# Create the 'fame' database
db.create_database('fame')

# Create the 'users' table
db.create_table('fame', 'users')

# Get user input
name = input('Enter your name: ')
email = input('Enter your email: ')
password = input('Enter your password: ')

# Check if email already exists in the database
existing_users = db.query_record('fame', 'users', {'email': email})
if existing_users:
    print('Error: Email already exists.')
else:
    # Generate a 10-digit ID
    _id = str(datetime.now().timestamp())[-10:]

    # Hash the password
    hashed_password = db.hash_password(password)

    # Get current datetime in Indian Standard Time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")

    # Insert the data into the 'users' table
    db.insert_record('fame', 'users', {
        'id': _id,
        'name': name,
        'email': email,
        'password': hashed_password,
        'timestamp': timestamp
    })

    print('Success: Data inserted successfully.')
