#!/bin/sh

kubectl exec pentest-pod8 -n default -- bash -c "egrep -ir 'password|passwd|secret|token|key|jwt|bearer|access|minio' /" > pod8.txt

