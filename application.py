from flask import Flask, request, jsonify, render_template, redirect, url_for
import pymysql
import os

application = Flask(__name__)

# Database connection details
DB_HOST = os.getenv('RDS_HOSTNAME', 'awseb-e-pkpyq9p2tm-stack-awsebrdsdatabase-zgugmur70ij4.c4riw2sqc5ge.us-east-1.rds.amazonaws.com')
DB_PORT = os.getenv('RDS_PORT', '3306')
DB_USER = os.getenv('RDS_DB_USERNAME', 'admin')
DB_PASSWORD = os.getenv('RDS_PASSWORD', '1q2w3e4r5t6y')
DB_NAME = os.getenv('RDS_DB_NAME', 'awseb-e-pkpyq9p2tm-stack-awsebrdsdatabase-zgugmur70ij4')

# This function utilizes an Aurora RDS Database in AWS.
def create_db():
    query_qb('''
        CREATE TABLE IF NOT EXISTS fields (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            occupation VARCHAR(255),
            hire_date DATE,
            salary DECIMAL(10, 2),
            employed BOOLEAN
        )
    ''')

# This function handles the SQL queries to the Aurora RDS Database.
def query_qb(query, params=(), fetch=False):
    conn = pymysql.connect(host=DB_HOST, port=int(DB_PORT), user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, params)
    if fetch:
        result = cursor.fetchall()
    else:
        result = None
    conn.commit()
    conn.close()
    return result

# Loads the client.html file when the user accesses the hosting URL.
@application.route('/')
def index():
    return render_template('client.html')

# POST Operation; the C in CRUD. When the user hits "add" on the client.html page, this function grabs all the data and submits it to the table.
@application.route('/add', methods=['POST'])
def add_field():
    name = request.form['name']
    occupation = request.form['occupation']
    hire_date = request.form['hire_date']
    salary = request.form['salary']
    employed = request.form['employed'] == 'true'

    query_qb('INSERT INTO fields (name, occupation, hire_date, salary, employed) VALUES (%s, %s, %s, %s, %s)',
             (name, occupation, hire_date, salary, employed))

    # Doing a redirect here so the page is automatically refreshed with the new entry showing in the database view.
    return redirect(url_for('index'))

# GET Operation; the R in CRUD. This function is called by the fetch method. On load, it grabs all the data from the 'fields' table and returns it as JSON to display.
@application.route('/fields', methods=['GET'])
def get_fields():
    fields = query_qb('SELECT id, name, occupation, hire_date, salary, employed FROM fields', fetch=True)
    fields = [{'id': row[0], 'name': row[1], 'occupation': row[2], 'hire_date': row[3], 'salary': row[4], 'employed': row[5]} for row in fields]
    return jsonify({'fields': fields})

# PUT Operation; the U in CRUD. Called by the editField, and submitEdit functions. Runs a simple UPDATE query to change the data in the fields table.
# I think I could have combined this function and add_field by using "INSERT OR UPDATE" SQL command, but figured I should keep them separate in this assignment for both simplicity and clarity.
@application.route('/edit/<int:id>', methods=['PUT'])
def edit_field(id):
    data = request.json
    query_qb('UPDATE fields SET name = %s, occupation = %s, hire_date = %s, salary = %s, employed = %s WHERE id = %s',
             (data['name'], data['occupation'], data['hire_date'], data['salary'], data['employed'], id))
    return jsonify({'success': True})

# DELETE Operation; the D in CRUD. Only used by the deleteField function, similar to edit_field, its a simple DELETE query to the fields table.
@application.route('/delete/<int:id>', methods=['DELETE'])
def delete_field(id):
    query_qb('DELETE FROM fields WHERE id = %s', (id,))
    return jsonify({'success': True})

# Endpoint to create the fields table if it doesn't exist
@application.route('/create_table', methods=['GET'])
def create_table():
    create_db()
    return jsonify({'success': True, 'message': 'Table created if it did not exist.'})

if __name__ == '__main__':
    create_db()
    application.run()
