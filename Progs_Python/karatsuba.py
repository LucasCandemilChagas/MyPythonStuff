class Karatsuba:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a
    
    @a.setter
    def a(self, novo_a):
        self.__a = novo_a

    @property
    def b(self):
        return self.__b
    
    @b.setter
    def num2(self, novo_b):
        self.__b = novo_b

    def __desloca_esquerda(self,m):
        mbin = m.lstrip('0')
        deslocado = mbin + '0' * len(m)
        return deslocado

    def algoritmo_mult_num_longos(self):
        m1a = self.a[:int(len(self.a)/2)]
        m2a = self.a[int(len(self.a)/2):]
        
        m1b = self.a[:int(len(self.a)/2)]
        m2b = self.a[int(len(self.a)/2):]

        a1 = self.__desloca_esquerda(m1a)
        a2 = self.__desloca_esquerda(m1a)
        b1 = self.__desloca_esquerda(m1a)
        b2 = self.__desloca_esquerda(m1a)


        return 


k = Karatsuba('100010101', '10001111')

print(k.algoritmo_mult_num_longos())