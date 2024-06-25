#!/bin/sh

kubectl exec pentest-pod4 -n default -- bash -c "egrep -ir 'password|passwd|secret|token|key|jwt|bearer|access|minio' /" > pod4.txt

