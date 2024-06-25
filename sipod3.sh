#!/bin/sh

kubectl exec pentest-pod3 -n default -- bash -c "egrep -ir 'password|passwd|secret|token|key|jwt|bearer|access|minio' /" > pod3.txt
