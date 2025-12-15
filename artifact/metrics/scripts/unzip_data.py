import zipfile
import os
import glob

def unzip_all_in_dir(directory):
    print(f"Unzipping files in {directory}...")
    for zip_path in glob.glob(os.path.join(directory, "*.zip")):
        print(f"Unzipping {zip_path}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(directory)
        print(f"Unzipped {zip_path}")

base_dir = os.path.dirname(os.path.abspath(__file__))
decompositions_dir = os.path.join(base_dir, "data", "decompositions")
graphs_dir = os.path.join(base_dir, "data", "relationship_graphs")

unzip_all_in_dir(decompositions_dir)
unzip_all_in_dir(graphs_dir)
print("Unzipping complete.")
