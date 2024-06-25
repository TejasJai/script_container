import os

proj_dir = "/root/container"

image_list = proj_dir + "/image.txt"

print("Project directory path: %s" %(proj_dir))

with open(image_list,"rt") as f:
    print(f.read())

with open(image_list,"rt") as file:
    for ns in file:
        ns = ns.strip("\n")
        print("Testing NS: %s" %(image))

        with open(ns + '_pods.txt', "rt") as pod:
            for p in pod:
                p = p.strip("\n")
                cmd = 'kubectl describe pod' + r"/" + p + ' -n ' + ns + ' | grep -B1 "Container ID:" | grep -v "Container ID:" | grep ":" | cut -d":" -f1 | '
                cmd1 = "sed -e's/ *//g'" + ' > ' + ns + '_' + p + '_containers.txt'
                cmd = cmd + cmd1
                print("root@tejas1: %s" %(cmd))
                os.system(cmd)
                print("\n")

print("DONE FULL TESTING")
