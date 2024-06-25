#!/bin/sh

kubectl exec pentest-pod12 -n default -- bash -c "egrep -ir 'pass|passwd|secret|token|key|jwt|bearer' /" > pod12.txt
