#!/bin/sh 
kubectl exec pentest-pod1 -n default -- sh -c "egrep -ir 'password|passwd|secret|token|key|jwt|bearer' /" > isdpod1.txt
