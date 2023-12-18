import subprocess

def start_recipe_database():
    script_path = 'scripts/start_mongo_locally.sh'
    try:
        subprocess.run(['bash', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}") 
