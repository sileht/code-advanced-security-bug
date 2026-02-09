"""
Intentionally vulnerable Python application for testing GitHub Advanced Security
This file contains multiple security vulnerabilities that should be detected by CodeQL
"""

import os
import sqlite3
import subprocess
import hashlib
from flask import Flask, request

app = Flask(__name__)

# Vulnerability 1: Hardcoded credentials
DATABASE_PASSWORD = "admin123"
API_KEY = "sk_live_1234567890abcdef"

# Vulnerability 2: SQL Injection
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # SQL Injection vulnerability - user input directly concatenated
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return str(result)

# Vulnerability 3: Command Injection
@app.route('/ping')
def ping_host():
    host = request.args.get('host')
    # Command injection vulnerability - user input passed to shell
    result = os.system('ping -c 1 ' + host)
    return f"Ping result: {result}"

# Vulnerability 4: Path Traversal
@app.route('/read_file')
def read_file():
    filename = request.args.get('file')
    # Path traversal vulnerability - no validation of file path
    with open('/var/data/' + filename, 'r') as f:
        content = f.read()
    return content

# Vulnerability 5: Weak cryptographic hash (MD5)
def hash_password(password):
    # Using MD5 which is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()

# Vulnerability 6: Another command injection with subprocess
@app.route('/execute')
def execute_command():
    cmd = request.args.get('cmd')
    # Command injection using subprocess with shell=True
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.stdout

# Vulnerability 7: Eval of user input
@app.route('/calc')
def calculate():
    expression = request.args.get('expr')
    # Code injection - eval of user input
    result = eval(expression)
    return str(result)

if __name__ == '__main__':
    # Running in debug mode with publicly accessible host
    app.run(debug=True, host='0.0.0.0')
