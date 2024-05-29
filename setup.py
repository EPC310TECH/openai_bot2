import os

# Define the base path for the project directory
project_path = "/Users/xx/PycharmProjects/bot_openai2"

# Define the folder structure based on the extracted details
folders = [
    "api",
    "models",
    "endpoints",
    "auth",
    "server",
    "libraries",
    "utils",
    "logs",
    "tests",
    "docs"
]

# Create the directory and subdirectories
os.makedirs(project_path, exist_ok=True)
for folder in folders:
    os.makedirs(os.path.join(project_path, folder), exist_ok=True)

# List the created directories to confirm
os.listdir(project_path)

# Define the paths and contents for the initial files
initial_files = {
    os.path.join(project_path, "server", "main.py"): "# Main server script\nimport flask\n\napp = flask.Flask(__name__)\n\n@app.route('/')\ndef hello_world():\n    return 'Hello, World!'\n\nif __name__ == '__main__':\n    app.run(debug=True)",
    os.path.join(project_path, "utils", "config.py"): "# Configuration settings\n\nAPI_KEY = 'Your-API-Key-Here'\nDATABASE_URL = 'Your-Database-URL-Here'",
    os.path.join(project_path, "docs", "README.md"): "# Project Documentation\n\nThis project integrates various APIs and handles data processing and server management."
}

# Create and write to the initial files
for file_path, content in initial_files.items():
    with open(file_path, "w") as file:
        file.write(content)

# List the files created to confirm
{file: os.path.exists(file) for file in initial_files}

# Define the paths and contents for the initial files
initial_files = {
    os.path.join(project_path, "server", "main.py"): "# Main server script\nimport flask\n\napp = flask.Flask(__name__)\n\n@app.route('/')\ndef hello_world():\n    return 'Hello, World!'\n\nif __name__ == '__main__':\n    app.run(debug=True)",
    os.path.join(project_path, "utils", "config.py"): "# Configuration settings\n\nAPI_KEY = 'Your-API-Key-Here'\nDATABASE_URL = 'Your-Database-URL-Here'",
    os.path.join(project_path, "docs", "README.md"): "# Project Documentation\n\nThis project integrates various APIs and handles data processing and server management."
}

# Create and write to the initial files
for file_path, content in initial_files.items():
    with open(file_path, "w") as file:
        file.write(content)

# List the files created to confirm
{file: os.path.exists(file) for file in initial_files}

import subprocess

# Function to run shell commands
def run_command(commands, cwd):
    process = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8'), stderr.decode('utf-8')

# Initialize the Git repository
init_output, init_error = run_command(["git", "init"], cwd=project_path)

# Add all files to the staging area
add_output, add_error = run_command(["git", "add", "."], cwd=project_path)

# Commit the changes
commit_output, commit_error = run_command(["git", "commit", "-m", "Initial commit"], cwd=project_path)

init_output, add_output, commit_output, init_error, add_error, commit_error
