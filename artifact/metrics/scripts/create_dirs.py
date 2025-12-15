import os

applications = [
    "spring-petclinic",
    "jpetstore",
    "partsunlimited",
    "demo"
]

base_dir = os.path.dirname(os.path.abspath(__file__))
apps_dir = os.path.join(base_dir, "data", "applications")

for app in applications:
    gt_dir = os.path.join(apps_dir, app, "ground_truth")
    os.makedirs(gt_dir, exist_ok=True)
    print(f"Created {gt_dir}")

print("Directory creation complete.")
