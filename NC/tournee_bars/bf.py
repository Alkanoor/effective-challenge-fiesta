#!/usr/bin/python
#coding: utf8

import io
import re
import time
import pycurl
import StringIO
from urllib import urlencode
from utils import *
import numpy as np


def clear(o):
    o.truncate(0)
    o.seek(0)

body_buffer = StringIO.StringIO()
header_buffer = StringIO.StringIO()


c = pycurl.Curl()
c.setopt(c.SSL_VERIFYHOST, 0)
c.setopt(c.WRITEFUNCTION, body_buffer.write)
c.setopt(c.HEADERFUNCTION, header_buffer.write)

c.setopt(c.COOKIE, 'PHPSESSID=8bd6a6df13dcc4e612b5a79499a7b93a; SMFCookie89=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2263127%22%3Bi%3A1%3Bs%3A40%3A%228f76ee4e57b4cb44bc9082e26c5dd7be554dbd81%22%3Bi%3A2%3Bi%3A1666111888%3Bi%3A3%3Bi%3A0%3B%7D')

found = False
n = 0
while not found:
    c.setopt(c.URL, 'https://www.newbiecontest.org/epreuves/prog/tournee_des_bars/progtournee.php')
    c.perform()

    body = body_buffer.getvalue()
    header = header_buffer.getvalue()

    clear(body_buffer)
    clear(header_buffer)

    with open('tmp.html', 'wb') as f:
        f.write(body)

    split1 = body.split('<tr class="col">')[1:]
    last_part = split1[len(split1)-1].split('</table>')
    split1[len(split1)-1] = last_part[0]
    second_part = last_part[1]

    y = len(split1)

    positions = {}
    bars = [[] for _ in range(y)]
    print(len(bars))
    for i in range(y):
        split2 = split1[i].split('<td class="lig">')[1:]
        x = len(split2)
        for j in range(x):
            tmp = split2[j].split('</td>')[0]
            if len(tmp)>0 and tmp != ' ':
            #    bars[i].append(int(tmp))
                positions[int(tmp)] = (j,i)
            # else:
            #     bars[i].append(-1)

    #print(bars)
    #print(positions)

    drinks = []
    split2 = second_part.split('<li>')[1:]
    for s in split2:
        drinks.append(s.split('</li>')[0])

    bars = ''.join(last_part).split('<span class="no_bar">')
    first_bar = bars[0].split('<span class="bar_initial">')[1].split('</span>')[0]
    bars = bars[1:]

    costs = [[] for _ in range(len(bars))]
    corresp = {}
    inv = {}
    n_bar = 0
    for b in bars:
        tmp = b.split('</span>')
        costs[int(tmp[0])-1] = {}
        boissons = []
        boisson = tmp[1].split('<td class="boisson">')[1:]
        cur = 0
        for b in boisson:
            boissons.append(b.split('</td>')[0])
            if corresp.get(b.split('</td>')[0]) is None:
                corresp[b.split('</td>')[0]] = cur
                inv[cur] = b.split('</td>')[0]
            elif corresp[b.split('</td>')[0]] != cur:
                print("OUCH, bad corresp "+b.split('</td>')[0]+" instead of "+str(cur))
                exit()
            cur += 1

        prices = {}
        prix = tmp[1].split('<td class="prix">')[1:]
        for p in range(len(prix)):
            prices[corresp[boissons[p]]] = int(prix[p].split('</td>')[0].split(' ')[0])

        costs[n_bar] = [prices[a] for a in range(len(prices))]
        n_bar += 1

    drinks_id = [corresp[d] for d in drinks]

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
    probas = [0.0]*N
    probas[int(first_bar)-1] = 1.0
    bars_index = [int(first_bar)-1]
    url = str(int(first_bar))

    for k in range(1,len(drinks_id)):
        probas_next = np.asarray([0.0]*N)
        for i in range(N):
            new_proba = 0.0
            for j in range(N):
                new_proba += proba_go_i_to_j[j][i]*probas[j]
            new_proba *= proba_consume_k_in_i[i][drinks_id[k]]
            probas_next[i] = new_proba

        sum = 0.0
        for s in probas_next:
            sum += s

        for j in range(len(probas_next)):
            probas_next[j] /= sum

        for j in range(len(probas_next)):
            if j == probas_next.argmax():
                probas[j] = 1.0
            else:
                probas[j] = 0.0

        print(probas_next)
        print(probas_next.max())
        print(probas_next.argmax()+1)
        bars_index.append(probas_next.argmax()+1)
        url += '-'+str(probas_next.argmax()+1)


    print(url)

    c.setopt(c.URL, 'https://www.newbiecontest.org/epreuves/prog/tournee_des_bars/validation.php?sequence='+url)
    c.perform()

    body = body_buffer.getvalue()
    header = header_buffer.getvalue()

    clear(body_buffer)
    clear(header_buffer)

    print(body)
    if len(body.split('Erreur')) <= 1:
        print("FOUND ! at n="+str(n))
        found = True
        exit()

    n += 1

    time.sleep(0.5)
