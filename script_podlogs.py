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
                        cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'CAM_USERNAME|CAM_PASSWORD|BEARER|db2inst1_password|t042ZUDL6v93|keystore_new_password|aws_access|aws_secret|ssh'"
                        #cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'adminpasswd|userpasswd'"
                        #cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'jwt |auth |access '"
                        #cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'password = |password =='"
                        #cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'token=|tokens=|token =|tokens ='"
                        #cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'key=|key =|key:|key :'"
                        #cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'secret'"
                        #cmd = 'kubectl describe pod/' + p + ' -n ' + ns + r" | grep --color=always -i 'image:'"
                        #cmd = 'kubectl describe pod/' + p + ' -n ' + ns + r" | grep --color=always -i 'psp:'"
                        #cmd = 'kubectl get pod/' + p + ' -n ' + ns + r" -o yaml | grep --color=always -i 'serviceaccountname:'"
                        #cmd = 'kubectl get pod/' + p + ' -n ' + ns + r" -o yaml | grep --color=always -i 'port:'"
                        #cmd = 'kubectl get pod/' + p + ' -n ' + ns + r" -o yaml | grep --color=always -i 'scc:'"
                        #cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'foundationdb|fdb'"
                        print("root@tejas1: %s" %(cmd))
                        os.system(cmd)
                        print("\n")

print("DONE FULL TESTING")
