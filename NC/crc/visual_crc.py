
def xor(m, P, index = 0):
    for i in range(len(P)):
        if m[index+i] == '1' and P[i] == '1':
            m = m[:index+i]+'0'+m[index+i+1:]
        elif m[index+i] == '0' and P[i] == '0':
            m = m[:index+i]+'0'+m[index+i+1:]
        else:
            m = m[:index+i]+'1'+m[index+i+1:]
    return m


def division_steps(m, P):
    cur = m
    steps = [m]
    for i in range(len(m)-len(P)+1):
        if cur[i] == '1':
            cur = xor(cur, P, i)
            steps.append(' '*i+P)
            steps.append(' '*i+cur[i+1:])
    steps.append(cur)
    return steps



for s in division_steps("1100010111001", "111010"):
    print s

for s in division_steps("110001011", "111010"):
    print s

for s in division_steps("000010001001", "111010"):
    print s
