def p(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    return p(n-1)+p(n-2)

def p_list(n):
    p = [1,1]
    for i in range(2,n):
        p.append(p[i-1]+p[i-2])
    return p[n-1]

def p_sem_list(n):
    a = 1
    b = 1
    c = 0
    for i in range(2,n):
        c = a+b
        a = b
        b = c
    return c


print(p_sem_list(40))
