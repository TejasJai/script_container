#!/bin/sh

kubectl exec pentest-pod7 -n default -- bash -c "egrep -ir 'password|passwd|secret|token|key|jwt|bearer|access|minio' /" > pod7.txt
