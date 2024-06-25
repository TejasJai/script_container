import os

proj_dir = "/root/container"
ns_list = proj_dir + "/ns_list.txt"

print("Project directory path:", proj_dir)

print("Namespaces to scan are:")
with open(ns_list, "rt") as f:
    print(f.read())

with open(ns_list, "rt") as file:
    for ns in file:
        ns = ns.strip("\n")
        print("*** Testing NS:", ns)

        with open(ns + '_pods.txt', "rt") as pod:
            for p in pod:
                p = p.strip("\n")

                with open(ns + '_' + p + '_containers.txt', "rt") as cont:
                    for c in cont:
                        c = c.strip("\n")
                        cmd = f'kubectl logs pod/{p} -n {ns} -c {c}'
                        print("Command:", cmd)

                        try:
                            result = os.system(cmd)
                            if result != 0:
                                print(f"Failed to fetch logs for pod {p} in namespace {ns}")
                        except Exception as e:
                            print(f"Error executing command for pod {p} in namespace {ns}: {str(e)}")

print("DONE FULL TESTING")
