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
        cmd = "kubectl describe namespace " + ns
        print("root@tejas1: %s" %(cmd))
        #nwp_output=subprocess.check_output(cmd,shell=True)
        #nwp_output=nwp_output.decode()
        #if (len(nwp_output)>0):
            #print("Following network policies are found for "+ns+" namespace\n")
            #cmd1 = "kubectl get networkpolicies -n "+ns+" | awk '(NR > 1) {print $1}' > "+ns+"_networkpolicies.txt"
        os.system(cmd)
            #cmd2 = "cat "+ns+"_networkpolicies.txt"
            #os.system(cmd2)
            #print("\n")
            #print("Describing the above listed network policies")
            #with open(ns + '_networkpolicies.txt', "rt") as nwp:
                #for n in nwp:
                    #n = n.strip("\n")
                    #cmd3 = 'kubectl describe networkpolicy ' + n + ' -n ' + ns
                    #print("Run cmd: %s" %(cmd3))
                    #os.system(cmd3)
                    #print("\n")
        #else:
            #print("NO NETWORK POLICIES ARE FOUND FOR " +ns+" NAMESPACE")
        print("\n")
#print("\n")
#print("FETCHED NETWORK POLICIES")
