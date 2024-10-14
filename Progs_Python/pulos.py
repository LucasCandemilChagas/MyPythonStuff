list_cores = []

# 1 - rosa 2 - roxo 3 - amarelo 4 - verde

def pulo_rec(n):
    if n == 0:
        return 1
    if n == 1:
        return 4
    
    return 3*pulo_rec(n-1)+2*pulo_rec(n-2)

print(pulo_rec(4))

