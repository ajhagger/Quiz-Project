import mysql.connector
from mysql.connector import Error

def get_connection(host_name, user_name, user_password, db):
    connection = None
    try:
        connection = mysql.connector.connect(
            host= host_name,
            user= user_name,
            passwd= user_password,
            database= db
        )
        print("Connection Successful")
    except Error as err:
        print(f"Error: '{err}'")
    
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query Successful")

    except Error as err:
        print(f"Error: '{err}'")

def execute_list_query(connection, query, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(query,val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("Query Successful")
        return result
    
    except Error as err:
        print(f"Error: '{err}'")

host_name = 'localhost'
user_name = 'root'
user_password = 'LozK9WO3QWr8'
db = 'vault'
create_password_table = """
CREATE TABLE password (
    pw_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    site_name VARCHAR(20) NOT NULL,
    url VARCHAR(40) NOT NULL,
    pw_value VARCHAR(20)
);
"""
drop_password = """
DROP TABLE password
"""
pop_password = """
INSERT INTO password VALUES
    (1, 'netflix', 'netflix.com', 'uRwPQe7sm09K'),
    (2, 'amazon', 'amazon.com', 'JrEtfvTRr9o1'),
    (3, 'twitter', 'twitter.com', 'oaafolY9jLBX'),
    (4, 'google', 'google.com', 'PJwQpQlafmMu'),
    (5, 'microsoft', 'microsoft.com', 'rW5kX3BgFkfj'),
    (6, 'discord', 'discord.com', 'dJOYdJE4f7Yd'),
    (7, 'spotify', 'spotify.com', 'qSidNfw9LoAS'),
    (8, 'youtube', 'youtube', 'oyesqwvt76HG'),
    (9, 'sql', 'dev.mysql.com', 'LozK9WO3QWr8'),
    (10, 'popsql', 'popsql.com', 'mJWEloYBTeDx8'),
    (11, 'wayup', 'wayup.com', 'Zlr1Hjh2WW6X');
"""
read_password = """
SELECT *
FROM password;
"""

connection = get_connection(host_name, user_name, user_password, db)
#execute_query(connection, drop_password)
#execute_query(connection, create_password_table)


#execute_query(connection, pop_password)
results = read_query(connection, read_password)

for result in results:
    print(result)
