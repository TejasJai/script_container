import os
import subprocess

proj_dir = "/root/container"
ns_list = proj_dir + "/ns_list.txt"

print("Project directory path: %s" %(proj_dir))

print("namespaces to scan are: ")
with open(ns_list,"rt") as f:
    print(f.read())

with open(ns_list,"rt") as file:
    for ns in file:
        ns = ns.strip("\n")
        print("*** Testing NS: %s" %(ns))
        cmd1 = "kubectl get pods -n " + ns + " | grep -i kube-hunter | awk '{print $1}'"
        print("Run cmd: %s" %(cmd1))
        pod_name = subprocess.check_output(cmd1, shell=True)
        pod_n = pod_name.decode()
        pod_n = pod_n.strip("\n")
        print("Kube-hunter pod name is %s" %(pod_n))
        print("\n")
        cmd2 = "kubectl logs " + pod_n + " -n " + ns
        print("Run cmd: %s" %(cmd2))
        os.system(cmd2)

print("KUBE-HUNTER RESULTS FETCHED")
