#!/bin/sh

kubectl exec pentest-pod10 -n default -- bash -c "egrep -ir 'pass|password|secret|token|key|id|username|user' /" > pod10.txt
