import os

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
        cmd = "kubectl create -f job.yaml -n " + ns
        print("Run cmd: %s" %(cmd))
        os.system(cmd)
        print("\n")
        cmd1 = "kubectl get pods -n " + ns + " | grep -i kube-hunter"
        print("Run cmd: %s" %(cmd1))
        os.system(cmd1)
        print("\n")
print("KUBE-HUNTER JOB CREATED")
