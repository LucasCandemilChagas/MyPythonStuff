def saltos(s):
    if len(s) == 0:
        return -1
    if s[0] == '0':
        return -1
    if s[0] == '1':
        return 3
    
    return saltos(s[1:]) + saltos(s[2:])




percurso = 'm1m'

print(saltos(percurso))