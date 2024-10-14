def a(x):
    soma = 0
    print(x)
    if x <= 1: 
        print(f"x <= 1 x{x}")
        return 1
    print("Entrou em Rec")
    print(f"Soma a = {soma}")
    soma = soma + x + a(x-1) + a(x-2)
    print(f"Soma d = {soma}")
    return soma


print(a(3))