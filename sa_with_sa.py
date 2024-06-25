import os

proj_dir = "/root/container"  # Update this with the path to your project directory

# Read the service account pairs from sa_list.txt
sa_list_path = os.path.join(proj_dir, "sa_list.txt")
with open(sa_list_path, "r") as sa_file:
    sa_pairs = [line.strip() for line in sa_file.readlines() if line.strip()]

# Process each service account pair
for sa_pair in sa_pairs:
    ns, sa_name = sa_pair.split(":")
    print(f"Namespace: {ns}, ServiceAccount: {sa_name}")

    # Execute the kubectl auth can-i command
    cmd = f"kubectl auth can-i --list --as system:serviceaccount:{ns}:{sa_name} -n {ns}"
    print(f"Executing command: {cmd}")

    # Capture the output of the kubectl command
    try:
        result = os.system(cmd)
        if result == 0:
            print(f"ServiceAccount {sa_name} in namespace {ns} has access permissions")
        else:
            print(f"ServiceAccount {sa_name} in namespace {ns} does not have access permissions")
    except Exception as e:
        print(f"Failed to execute command: {str(e)}")

print("DONE FULL TESTING")
