from json_database import JSONDatabase

# Create a new database instance
db = JSONDatabase(database_dir='path/to/database')

# Create a new database
db.create_database('mydatabase')

# Create a new table in the database
db.create_table('mydatabase', 'users')

# Insert a record into the table
record = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'password': 'password123'
}
db.insert('mydatabase', 'users', record)

# Query records from the table
query = {'name': 'John Doe'}
result = db.query('mydatabase', 'users', query)
print(result)

# Update records in the table
query = {'name': 'John Doe'}
update = {'name': 'John Smith'}
db.update('mydatabase', 'users', query, update)

# Delete records from the table
query = {'name': 'John Doe'}
db.delete('mydatabase', 'users', query)

# Drop the table
db.drop_table('mydatabase', 'users')

# Drop the database
db.drop_database('mydatabase')

# Additional Database Functions

# Get the size of a table
table_size = db.get_table_size('mydatabase', 'users')
print(f"Size of table 'users': {table_size} bytes")

# Create a unique index on a field
db.create_unique_index('mydatabase', 'users', 'email')

# Get a record by index value
record = db.get_record_by_index('mydatabase', 'users', 'email', 'john@example.com')
print(record)

# Update a record by index value
new_values = {'name': 'John Smith'}
db.update_record_by_index('mydatabase', 'users', 'email', 'john@example.com', new_values)

# Delete a record by index value
db.delete_record_by_index('mydatabase', 'users', 'email', 'john@example.com')

# Optimize a table to remove invalid records
db.optimize_table('mydatabase', 'users')

# Log Database Operations

# Enable logging of database operations
db.enable_logging()

# Disable logging of database operations
db.disable_logging()

# Get the log of database operations
log = db.get_operation_log()
print(log)
