#!/bin/sh

kubectl exec pentest-pod2 -n default -- bash -c "egrep -ir 'password|passwd|secret|token|key|jwt|bearer' /" > pod2.txt
