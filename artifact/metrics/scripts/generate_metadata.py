import os
import shutil

applications = [
    "spring-petclinic",
    "jpetstore",
    "partsunlimited",
    "demo"
]

base_dir = os.path.dirname(os.path.abspath(__file__))
graphs_dir = os.path.join(base_dir, "data", "relationship_graphs")
apps_dir = os.path.join(base_dir, "data", "applications")

for app in applications:
    print(f"Processing {app}...")
    
    # Create app directory if it doesn't exist
    app_dir = os.path.join(apps_dir, app)
    os.makedirs(app_dir, exist_ok=True)
    
    # Generate classes.txt
    nodes_csv = os.path.join(graphs_dir, app, "class_level", "nodes.csv")
    classes_txt = os.path.join(app_dir, "classes.txt")
    
    if os.path.exists(nodes_csv):
        print(f"Generating {classes_txt} from {nodes_csv}")
        shutil.copyfile(nodes_csv, classes_txt)
    else:
        print(f"Warning: {nodes_csv} not found!")

    # Generate methods.txt
    method_nodes_csv = os.path.join(graphs_dir, app, "method_level", "nodes.csv")
    methods_txt = os.path.join(app_dir, "methods.txt")
    
    if os.path.exists(method_nodes_csv):
        print(f"Generating {methods_txt} from {method_nodes_csv}")
        shutil.copyfile(method_nodes_csv, methods_txt)
    else:
        print(f"Warning: {method_nodes_csv} not found!")

print("Metadata generation complete.")
