# Test file with intentional security and quality issues for AI agent review
import os
import requests
import sqlite3

def vulnerable_function(user_input):
    """Function with multiple security vulnerabilities."""
    
    # SECURITY ISSUE 1: SQL Injection vulnerability
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM users WHERE name = '{user_input}'"  # Vulnerable!
    cursor = conn.execute(query)
    
    # SECURITY ISSUE 2: Hardcoded secrets (should be flagged by AI)
    api_key = "sk-1234567890abcdef"  # Hardcoded API key - DANGEROUS!
    password = "admin123"  # Hardcoded password - INSECURE!
    database_url = "postgresql://admin:secret123@prod.db.com/app"
    
    # PERFORMANCE ISSUE: Blocking requests in loop
    results = []
    for i in range(100):  # This will be slow and block the thread
        response = requests.get(f"https://api.example.com/user/{i}")
        results.append(response.json())
    
    return results

def another_security_issue():
    """Another function with security problems."""
    
    # SECURITY ISSUE 3: Using eval() - EXTREMELY DANGEROUS
    user_code = input("Enter Python code to execute: ")
    return eval(user_code)  # Never do this in real code!

def poor_error_handling():
    """Function demonstrating poor error handling."""
    try:
        # This could fail in many ways
        result = requests.get("https://api.unreliable-service.com/data")
        return result.json()
    except:
        pass  # Silent failure - bad practice!

# SECURITY ISSUE 4: Exposed configuration
CONFIG = {
    "database_password": "supersecret123",
    "api_keys": {
        "stripe": "sk_live_real_stripe_key_here",
        "aws": "AKIAIOSFODNN7EXAMPLE"
    },
    "jwt_secret": "jwt-secret-key-dont-commit-this"
}

class InsecureDataProcessor:
    """Class with various security and quality issues."""
    
    def __init__(self):
        # Hardcoded credentials again
        self.admin_token = "admin_token_12345"
        
    def process_file(self, filename):
        """Process file without proper validation."""
        
        # SECURITY ISSUE 5: Path traversal vulnerability
        with open(f"/app/data/{filename}", "r") as f:  # No path validation!
            content = f.read()
            
        # SECURITY ISSUE 6: Potential code injection
        exec(f"result = process_{filename.replace('.', '_')}(content)")
        
        return result

# The AI agent should detect all these issues and provide detailed feedback!