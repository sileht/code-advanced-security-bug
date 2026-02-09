#!/usr/bin/env python3
"""
Intentionally vulnerable Python application for testing GitHub Advanced Security.
This file contains multiple security vulnerabilities for demonstration purposes.
DO NOT USE IN PRODUCTION!
"""

import os
import sqlite3
import subprocess
import pickle
import yaml


# Vulnerability 1: Hardcoded credentials
DATABASE_PASSWORD = "super_secret_password_123"
API_KEY = "sk-1234567890abcdef"


def search_users(username):
    """
    Vulnerability 2: SQL Injection
    User input is directly concatenated into SQL query.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: SQL injection possible
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()
    return results


def execute_command(user_input):
    """
    Vulnerability 3: Command Injection
    User input is passed directly to shell command.
    """
    # VULNERABLE: Command injection possible
    command = "ping -c 1 " + user_input
    result = subprocess.call(command, shell=True)
    return result


def read_file(filename):
    """
    Vulnerability 4: Path Traversal
    User can access files outside intended directory.
    """
    # VULNERABLE: Path traversal possible
    base_path = "/var/www/uploads/"
    file_path = base_path + filename
    
    with open(file_path, 'r') as f:
        return f.read()


def evaluate_expression(expr):
    """
    Vulnerability 5: Use of eval() with user input
    Allows arbitrary code execution.
    """
    # VULNERABLE: Code injection via eval()
    result = eval(expr)
    return result


def load_user_data(data):
    """
    Vulnerability 6: Insecure deserialization
    Pickle can execute arbitrary code during deserialization.
    """
    # VULNERABLE: Insecure deserialization
    user_object = pickle.loads(data)
    return user_object


def load_config(config_string):
    """
    Vulnerability 7: YAML deserialization
    Can lead to arbitrary code execution with unsafe loader.
    """
    # VULNERABLE: Unsafe YAML deserialization
    config = yaml.load(config_string)
    return config


def weak_random_token():
    """
    Vulnerability 8: Weak random number generation for security
    """
    import random
    # VULNERABLE: Using weak random for security token
    token = random.randint(1000, 9999)
    return str(token)


def insecure_temp_file():
    """
    Secure temporary file creation (FIXED)
    """
    import tempfile
    # FIXED: Using secure mkstemp() instead of deprecated mktemp()
    fd, temp = tempfile.mkstemp()
    with open(temp, 'w') as f:
        f.write("sensitive data")
    os.close(fd)
    return temp


def check_password(password):
    """
    Strong cryptographic hash for passwords (FIXED)
    """
    import hashlib
    # FIXED: Using SHA-256 instead of MD5 for better security
    # Note: In production, use bcrypt or argon2 for password hashing
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed


def main():
    """Main function to demonstrate vulnerable code."""
    print("This is an intentionally vulnerable application.")
    print("DO NOT USE IN PRODUCTION!")
    
    # Example usage (commented out to avoid actual execution)
    # search_users("admin' OR '1'='1")
    # execute_command("localhost; cat /etc/passwd")
    # read_file("../../etc/passwd")
    # evaluate_expression("__import__('os').system('ls')")


if __name__ == "__main__":
    main()
