# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 22:04:27 2021

@author: xuz16
"""
import time
def kruskal(filename):
    f = open(filename, "r")
    weights=dict()
    parents=dict()
    ranks=dict()
    nodes=set()
    for line in f:
        u,v,w=line.split(' ',2)
        u=int(u)
        v=int(v)
        w=int(w[0:-1:])
        weights[(u,v)]=w
        nodes.add(u)
        nodes.add(v)
    
    for n in nodes:
        ranks[n]=0
        parents[n]=n

    X=set()
    E=dict(sorted(weights.items(), key=lambda item: item[1]))  

    for item in E:
        u=item[0]
        v=item[1]

        findu=find(u,parents)
        findv=find(v,parents)

        if findu!=findv:
            X.add((u,v,E[(u,v)]))
            union(findu,findv,ranks,parents)
    ws=0

    for x in X:
        ws+=x[2]
    
    maxcount=0
    root = find(u,parents)
    for n in nodes:
        count=1
        while parents[n]!=root:
            count+=1
            n=parents[n]
        if count>maxcount:
            maxcount=count
    
    maxrank=0
    for r in ranks:
        if ranks[r]>maxrank:
            maxrank=ranks[r]
    print("MST cost",ws,maxrank,maxcount)
  

def find(u,parents):
    if u!=parents[u]:
        parents[u]=find(parents[u],parents)
    return parents[u]
'''         

def find(u,parents):
    upar=u
    while parents[upar]!=upar:
        upar=parents[upar]
    return upar
'''   
def union(u,v,ranks,parents):
    if ranks[u]==ranks[v]:
        parents[v]=u
        ranks[u]+=1
    else:
        if ranks[u]<ranks[v]:
            parents[u]=v
        else:
            parents[v]=u

print("Path Compression")
files=["kruskal_graph100.txt","kruskal_graph1000.txt","kruskal_graph10000.txt"]
for f in files:
    print(f,":")
    start = time.perf_counter()        
    kruskal(f)
    end = time.perf_counter()
    print("time",end-start)
        
        
        