# code-advanced-security-bug

This repository contains intentionally vulnerable Python code for testing GitHub Advanced Security (CodeQL).

## Vulnerabilities Included

### vulnerable_app.py
1. **Hardcoded Credentials** - Sensitive data hardcoded in source code
2. **SQL Injection** - Unsanitized user input in SQL queries
3. **Command Injection** - User input passed to os.system()
4. **Path Traversal** - No validation of file paths
5. **Weak Cryptography** - Use of MD5 for password hashing
6. **Command Injection via subprocess** - shell=True with user input
7. **Code Injection** - Use of eval() with user input

### insecure_utils.py
1. **Insecure Deserialization** - pickle.loads() on untrusted data
2. **YAML Unsafe Load** - yaml.load() without SafeLoader
3. **Path Traversal** - Unsanitized file paths
4. **Command Injection** - String formatting with user input
5. **Shell Injection** - subprocess with shell=True
6. **Hardcoded Secrets** - Secret keys in source code
7. **Insecure Random** - Using random module for security tokens

## Purpose

These files are intentionally insecure to demonstrate:
- How GitHub Advanced Security detects vulnerabilities
- Common security anti-patterns in Python
- How CodeQL scanning works

## Requirements

- Python 3.x
- Flask and PyYAML (install via `pip install -r requirements.txt`)
- Unix-like OS (some commands like `ping -c 1` are Unix-specific)

**⚠️ WARNING: Never use this code in production!**