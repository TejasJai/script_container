#!/bin/sh

kubectl exec pentest-pod11 -n default -- bash -c "egrep -ir 'pass|passwd|secret|token|key|jwt|bearer' /" > pod11.txt
