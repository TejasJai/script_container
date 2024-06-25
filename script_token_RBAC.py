import os
import jwt

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

                with open( p + '_token.txt', "rt") as t:
                    token = t.read()
                    token = token.strip("\n")
                    print (token)
                    x = jwt.decode(token, verify=False)
                    print ("Decoded token for "+p+":")
                    print (x)
                    print ("\n")

print("cp kubctl")
