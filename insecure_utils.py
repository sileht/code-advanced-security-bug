"""
Additional utility functions with security vulnerabilities
"""

import pickle
import yaml
import os
import subprocess

# Vulnerability: Insecure deserialization
def load_user_data(data):
    """Deserialize user data using pickle - UNSAFE!"""
    # Pickle deserialization of untrusted data
    return pickle.loads(data)

# Vulnerability: YAML unsafe load
def load_config(config_string):
    """Load YAML config - using unsafe loader"""
    # yaml.load without safe loader is vulnerable
    return yaml.load(config_string)

# Vulnerability: Path traversal in file operations
def delete_user_file(username, filename):
    """Delete a file in user directory"""
    # No sanitization - path traversal vulnerability
    file_path = f"/home/{username}/{filename}"
    os.remove(file_path)

# Vulnerability: Command injection through string formatting
def backup_directory(directory):
    """Backup a directory using tar"""
    # Command injection via string formatting
    command = f"tar -czf backup.tar.gz {directory}"
    os.system(command)

# Vulnerability: Use of shell=True with user input
def run_user_script(script_name):
    """Execute user-provided script"""
    # Dangerous use of shell=True
    subprocess.call(f"python {script_name}", shell=True)

# Vulnerability: Hardcoded secret key
SECRET_KEY = "my-secret-key-12345"
JWT_SECRET = "jwt-secret-token-67890"

# Vulnerability: Insecure random for security purposes
import random

def generate_token():
    """Generate a security token"""
    # Using insecure random for security token
    return ''.join([str(random.randint(0, 9)) for _ in range(20)])
