def coelhos_sem_rec(n):
    a = 0
    b = 0
    j = 1
    for i in range(2,n):
        ant_b = b
        b = j+a
        a += j
        j = ant_b

    return a,b,j


a,b,j = coelhos_sem_rec(40)      

print(f'Adultos - {a} Jovens - {j} Bebes - {b}')