#!/bin/sh

kubectl exec pentest-pod6 -n default -- bash -c "egrep -ir 'password|passwd|secret|token|key|jwt|bearer|access|minio' /" > pod6.txt

