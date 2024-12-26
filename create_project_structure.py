import os
import json

def create_structure(base_path, structure):
    for name, value in structure.items():
        current_path = os.path.join(base_path, name)
        
        if isinstance(value, dict):
            os.makedirs(current_path, exist_ok=True)
            create_structure(current_path, value)
        else:
            with open(current_path, 'w') as f:
                f.write(value)

def main():
    json_file_path = 'project_structure.json'
    
    with open(json_file_path, 'r') as file:
        project_data = json.load(file)
    
    project_name = project_data.get('name', 'project')
    project_structure = project_data.get('project', {})
    
    base_path = project_name
    os.makedirs(base_path, exist_ok=True)
    
    create_structure(base_path, project_structure)

if __name__ == "__main__":
    main()
