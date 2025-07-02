def construct_B_from_yL(y, L):
    sorted_y = ''.join(sorted(y))
    B = [sorted_y]
    L_list = [y[i] + sorted_y[i] for i in range(len(y))]
    
    for _ in range(len(y) - 1):
        s1 = "L: {}".format(L_list)
        print(s1.replace('"', '').replace("'", ""))
        L_list = sorted(L_list)
        s2 = "sorted_L: {}".format(L_list) 
        print(s2.replace('"', '').replace("'", ""))
        B.append(''.join([item[-1] for item in L_list]))
        L_list = [y[i] + L_list[i] for i in range(len(y))]
    
    return B

y = 'bbbcbacaa'
L = 0
B = construct_B_from_yL(y, L)
for row in B:
    print(row)

