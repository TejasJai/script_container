#!/bin/sh

kubectl exec pentest-pod9 -n default -- bash -c "egrep -ir 'pass|password|secret|token|key|id|username|user' /" > pod9.txt
