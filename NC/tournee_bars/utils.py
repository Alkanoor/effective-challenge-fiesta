def print_t(p, title):
    print(title)
    for i in range(len(p)):
        print("Item i "+str(i)+" : ")
        for j in range(len(p[i])):
            print("- "+str(p[i][j]))

def print_probas_go_i_to_j(proba_go_i_to_j):
    print_t(proba_go_i_to_j, "======= Probas moving from bar i to bar j =======")

def print_probas_consume_k_in_i(proba_consume_k_in_i):
    print_t(proba_consume_k_in_i, "======= Probas consumming drink k in bar i =======")

def convert_to_proba(distances_i_to_j, zero_fo_identity=True):
    proba_go_i_to_j = []
    for i in range(len(distances_i_to_j)):
        proba_go_i_to_j.append([])
        for j in range(len(distances_i_to_j[i])):
            if zero_fo_identity:
                if i != j:
                    proba_go_i_to_j[i].append(1.0/float(distances_i_to_j[i][j]))
                else:
                    proba_go_i_to_j[i].append(0.0)
            else:
                proba_go_i_to_j[i].append(1.0/float(distances_i_to_j[i][j]))

        sum = 0.0
        for s in proba_go_i_to_j[i]:
            sum += s

        for j in range(len(distances_i_to_j[i])):
            proba_go_i_to_j[i][j] /= sum
    return proba_go_i_to_j
