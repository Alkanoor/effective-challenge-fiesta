#!/usr/bin/python

from parse import *
from utils import *
from dijkstra import *
import numpy as np
import math


distances_i_to_j = []
prices_k_in_i = []

print("Positions : "+str(positions))
print("Costs : "+str(costs))
print("Drinks in order : "+str(drinks_id))
print("First bar : "+str(first_bar))

x = 0
for i in positions:
    y = 0
    distances_i_to_j.append([])
    for j in positions:
        distances_i_to_j[x].append(abs(positions[i][0]-positions[j][0])+abs(positions[i][1]-positions[j][1]))
        y += 1
    x += 1

proba_go_i_to_j = convert_to_proba(distances_i_to_j)
print(distances_i_to_j)
print_probas_go_i_to_j(proba_go_i_to_j)

proba_consume_k_in_i = convert_to_proba(costs, False)
print(proba_consume_k_in_i)
print_probas_consume_k_in_i(proba_consume_k_in_i)

N = len(proba_go_i_to_j)


def hash(t, b):
    return t*1000000+b

def unhash(t):
    return (t//1000000, t%1000000)

url = str(int(first_bar))
cur_bar = int(first_bar)-1
bars = [cur_bar]
aretes = []
g = Graph()
initial = (0,cur_bar)
nodes = []
nodes.append(initial)
g.add_vertex((0,cur_bar))
for k in range(1,len(drinks_id)):
    for j in range(N):
        g.add_vertex((k,j))
        nodes.append((k,j))
    for b in range(len(bars)):
        cur_bar = bars[b]
        probas = np.asarray([0.0]*N)
        for j in range(N):
            if j != cur_bar:
                g.add_edge((k-1,cur_bar), (k,j), 10000000-math.log(proba_go_i_to_j[cur_bar][j]*proba_consume_k_in_i[j][drinks_id[k]]))
                probas[j] = proba_go_i_to_j[cur_bar][j]*proba_consume_k_in_i[j][drinks_id[k]]
            else:
                probas[j] = 0.0

        # print(probas)
        # print(probas.max())
        # print(probas.argmax()+1)

        aretes.append((-probas.max(), k-1, cur_bar, probas.argmax()))
    bars = [i for i in range(N)]

tmp = dijkstra(g,g.get_vertex((initial[0],initial[1])),g.get_vertex((len(drinks_id)-2,1)))

m = -1.0
for i in range(N):
    target = g.get_vertex((len(drinks_id)-1,i))
    if target.get_distance() < m or m < 0.0:
        m = target.get_distance()
        index = i
    print("N = "+str(i)+" => "+str(target.get_distance()))

target = g.get_vertex((len(drinks_id)-1,index))
path = [target.get_id()]
shortest(target, path)

url = ''
for u,v in path[::-1]:
    if (u,v) != initial:
        url += '-'+str(v+1)
    else:
        url += str(v+1)

print(url)

c.setopt(c.URL, 'https://www.newbiecontest.org/epreuves/prog/tournee_des_bars/validation.php?sequence='+url)
c.perform()

body = body_buffer.getvalue()
header = header_buffer.getvalue()

clear(body_buffer)
clear(header_buffer)

print(body)
