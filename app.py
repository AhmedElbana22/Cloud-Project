# app.py

from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database connection configuration
db_config = {
    'user': 'root',
    'password': '123',
    'host': 'db',  # Update host to use the service name from docker-compose.yml
    'port': '3306',
    'database': 'team'  # Update to 'team' database
}

# Connect to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Define a route to render the team.html template
@app.route('/team')
def team():
    # Fetch data from the database
    cursor.execute("SELECT * FROM STUDENTS")  # Update table name to STUDENTS
    students = cursor.fetchall()

    # Pass the data to the template for rendering
    return render_template('team.html', students=students)

# Define a route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Update host to allow access from outside the container
