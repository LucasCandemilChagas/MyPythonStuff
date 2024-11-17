def t(n):
    if n == 0:
        return 0
    if n ==1:
        return 1
    return 4* t(n-1)


def l(n):
    if n == 0:
        return 0
    if n == 1:
        return 3
    return 3 * l(n-1) + l(n-2)
print(t(4))
print(l(4))