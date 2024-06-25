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
                        cmd1 = 'kubectl exec ' + p + ' -n ' + ns + ' -c ' + c + r' -- curl -skv https://10.254.48.147:2379/version'
                        print("root@tejas1: %s" %(cmd1))
                        os.system(cmd1)
                        print("\n")

print("Installed KUBECTL")
