import os
import subprocess

y_cmd = 'id' #replace id with your command.

proj_dir = "/root/container"
ns_list = proj_dir + "/ns_list.txt"

print("Project directory path: %s" %(proj_dir))

print("namespaces to scan are: ")
with open(ns_list,"rt") as f:
    print(f.read())

with open(ns_list,"rt") as file:
    for ns in file:
        ns = ns.strip("\n")
        print("Testing NS: %s" %(ns))
        cmd1 = 'kubectl get pods -n ' + ns + r"| egrep -i 'internalapi' | grep -i 'running'" 
        cmd2 = " | awk '{print $1}'"
        cmd = cmd1 + cmd2
        print("root@tejas1: %s" %(cmd))
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout.strip()
        print("Current Pod: %s" %(output))
        test = 'kubectl exec %s -n %s -- %s' % (output, ns, y_cmd)
        print("root@tejas1: %s" %(test))
        os.system(test)
print("DONE FULL TESTING")
