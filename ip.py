import os
import subprocess

proj_dir = "/root/container"  # Update this with the path to your project directory

# Read the namespaces from ns_list.txt
ns_list_path = os.path.join(proj_dir, "ns_list.txt")
with open(ns_list_path, "r") as ns_file:
    namespaces = [ns.strip() for ns in ns_file.readlines() if ns.strip()]

# Process each namespace
for ns in namespaces:
    print(f"Namespace: {ns}")
    
    # Execute the kubectl command to get pods in the namespace
    cmd = f"kubectl get pods -n {ns} -o wide"
    print(f"Executing command: {cmd}")

    # Capture the output of the kubectl command
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to get pods in namespace {ns}: {e.output}")
        continue

    # Parse the output to extract pod names and IP addresses
    lines = result.splitlines()
    if len(lines) > 1:
        headers = lines[0].split()
        ip_index = headers.index("IP")
        pod_index = headers.index("NAME")

        for line in lines[1:]:
            parts = line.split()
            pod_name = parts[pod_index]
            ip_address = parts[ip_index]

            # Print pod name and IP address
            print(f"Pod: {pod_name}, IP: {ip_address}")
    else:
        print(f"No pods found in namespace {ns}")

print("DONE FULL TESTING")

