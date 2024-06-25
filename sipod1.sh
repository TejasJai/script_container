#!/bin/sh

kubectl exec pentest-pod1 -n default -- bash -c "egrep -ir 'password|passwd|secret|token|key|jwt|bearer|access|minio' /" > pod1.txt

