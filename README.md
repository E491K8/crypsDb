# CrypsDB

CrypsDB is a Python library that provides a simple and lightweight JSON-based database for storing and querying data. It aims to offer an easy-to-use interface while maintaining flexibility and performance.

## Features

- Create and manage databases
- Create and manage tables within databases
- Insert, update, and delete records
- Query records using various conditions
- Perform aggregations
- Create and manage indexes
- Backup and restore databases
- Handle transactions

## Installation

pip install crypsdb

## Usage

Here's a simple example that demonstrates how to use CrypsDB:

```python
from crypsdb import JSONDatabase

# Create a new database
db = JSONDatabase('my_database')

# Create a table
db.create_table('users', ['id', 'name', 'email'])

# Insert records into the table
db.insert('users', {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'})
db.insert('users', {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'})

# Query records
results = db.query('users', {'name': 'John Doe'})
print(results)  # [{'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}]

# Update a record
db.update('users', {'id': 1}, {'email': 'john.doe@example.com'})

# Delete a record
db.delete('users', {'id': 2})

# Backup the database
db.backup('backup.zip')

# Restore the database
db.restore('backup.zip')

# Drop the database
db.drop_database()

For more detailed documentation and examples, please refer to the CrypsDB Documentation.
