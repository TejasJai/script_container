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

        with open(ns + '_pods.txt', "rt") as pod:
            for p in pod:
                p = p.strip("\n")

                with open(ns + '_' + p + '_containers.txt', "rt") as cont:
                    for c in cont:
                        c = c.strip("\n")
                        cmd = 'kubectl exec ' + p + ' -n ' + ns + ' -c ' + c + r" -- id"
                        #cmd = 'kubectl exec ' + p + ' -n ' + ns + ' -c ' + c + r" -- find / -perm -4000 -type f -exec ls -l {} \; 2>/dev/null"
                        #cmd = 'kubectl exec ' + p + ' -n ' + ns + ' -c ' + c + r" -- powershell -Command 'whoami /all' "
                        print("root@tejas1: %s" %(cmd))
                        os.system(cmd)
                        print("\n")

print("DONE FULL TESTING")
