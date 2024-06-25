#!/bin/sh

kubectl exec pentest-pod5 -n default -- bash -c "egrep -ir 'password|passwd|secret|token|key|jwt|bearer|access|minio' /" > pod5.txt
