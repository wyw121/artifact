import os

base_path = os.path.abspath("../../../data/decomposition_visualizations")
# Since I run this from metrics/scripts, ../../../ resolves to artifact root + /data...
# Actually, let's use absolute path based on __file__ to be safe.
script_dir = os.path.dirname(os.path.abspath(__file__))
# script_dir is .../metrics/scripts
# We want .../data/decomposition_visualizations (in the root artifact folder? or where?)
# The error message showed: C:\Users\aone\Downloads\artifact\data\decomposition_visualizations
# This corresponds to ../../../ from metrics/scripts if metrics/scripts is 2 levels deep from artifact root?
# artifact/metrics/scripts -> 3 levels.
# artifact/metrics/scripts -> .. -> metrics -> .. -> artifact -> .. -> root.
# So ../../../ is root.

# Let's assume root is C:\Users\aone\Downloads\artifact
root_dir = os.path.abspath(os.path.join(script_dir, "../../.."))
vis_dir = os.path.join(root_dir, "data", "decomposition_visualizations")

apps = {
    "jpetstore": "1_jpetstore",
    "spring-petclinic": "2_spring-petclinic",
    "partsunlimited": "3_partsunlimited",
    "demo": "4_demo"
}

tools = {
    "ground_truth": "1_ground_truth",
    "mono2micro": "2_mono2micro",
    "hydec": "3_hydec",
    "datacentric": "4_datacentric",
    "log2ms": "5_log2ms",
    "tomicroservices": "6_tomicroservices",
    "cargo": "7_cargo",
    "mem": "8_mem",
    "mosaic": "9_mosaic"
}

for app_key, app_val in apps.items():
    for tool_key, tool_val in tools.items():
        path = os.path.join(vis_dir, app_val, tool_val)
        os.makedirs(path, exist_ok=True)
        print(f"Created {path}")

print("Visualization directories created.")
