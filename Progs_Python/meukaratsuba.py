import sys
import re


#Nome : Lucas Candemil Chagas

class Karatsuba:
    
    @staticmethod
    def algoritmo_karatuba(a,b):
        
        a,b = Karatsuba.iguala_tamanhos(a,b)
        n = len(a)
        
        meio = n - n//2
        
        if n == 1:
            return Karatsuba.mult_de_bins_1bit(a,b)  
        
        ah , al , bh , bl = Karatsuba.divide_strings_bin(a,b)
        
        a1b1 = Karatsuba.algoritmo_karatuba(ah,bh)
        a2b2 = Karatsuba.algoritmo_karatuba(al,bl)
        z = Karatsuba.algoritmo_karatuba(Karatsuba.sum_strings_bin(ah,al),Karatsuba.sum_strings_bin(bh,bl))
        
        sub = Karatsuba.sub_strings_bin(Karatsuba.sub_strings_bin(z,a1b1),a2b2) 
        
        sub_shiftado = Karatsuba.desloca_esquerda(sub,n-meio)

        a1b1_shiftado = Karatsuba.desloca_esquerda(a1b1,2*(n-meio))
        
        soma_interna = Karatsuba.sum_strings_bin(a1b1_shiftado,sub_shiftado)
        soma_total = Karatsuba.sum_strings_bin(soma_interna,a2b2)
        
        return soma_total
        
    @staticmethod
    def desloca_esquerda(x,k):
        return x + '0' * k
    
    @staticmethod
    def mult_de_bins_1bit(x,y):
        if x == '0' or y == '0':
            return '0'
        else:
            return '1'

    
    @staticmethod
    def sub_strings_bin(x,y):
        if len(x) < len(y):
            novo_y = x
            x = y
            y = novo_y
        
        carry = '0'
        
        x,y = Karatsuba.iguala_tamanhos(x,y)
        
        xr = x[::-1]
        yr = y[::-1]
        
        sub = ''
        
        for ind,bin in enumerate(xr):
            bin2 = yr[ind]
            if bin == bin2:
                if Karatsuba.verifica_carry(carry):
                    sub += '1'
                else:
                    sub += '0'
            else:
                if Karatsuba.verifica_ordm_0_1(bin,bin2):
                    if Karatsuba.verifica_carry(carry):
                        sub += '0'
                    else:
                        sub += '1'
                        carry = '1'
                else:
                    if Karatsuba.verifica_carry(carry):
                        sub += '0'
                        carry = '0'
                    else:
                        sub+='1'
                        
        return sub[::-1].lstrip('0')                 
    
    @staticmethod
    def sum_strings_bin(x,y):
        if x == '0' * len(x):
            return y
        elif y == '0' * len(y):
            return x
        
        x,y = Karatsuba.iguala_tamanhos(x,y)
        
        xr = x[::-1]
        yr = y[::-1]
        
        carry = '0'
        
        sum = ''
        
        for ind,bin in enumerate(xr):
            if bin == yr[ind]:
                if bin == '1':
                    if Karatsuba.verifica_carry(carry):
                        if ind == len(xr)-1:
                            sum += '11'
                        else:
                            sum += '1'
                    else:
                        if ind == len(xr)-1:
                            sum += '01'
                        else:
                            sum += '0'
                        carry = '1'
                else:
                    if Karatsuba.verifica_carry(carry):
                        sum+= '1'
                        carry = '0'
                    else:
                        sum += '0'
            else:
                if Karatsuba.verifica_carry(carry):
                    if ind == len(xr)-1:
                        sum += '01'
                    else:
                        sum += '0'
                else:
                    sum += '1'
        
        return sum[::-1].lstrip('0')              
    
    @staticmethod
    def divide_strings_bin(x,y):
        
        xh = Karatsuba.primeira_metade(x)
        xl = Karatsuba.segunda_metade(x)
        
        yh = Karatsuba.primeira_metade(y)
        yl = Karatsuba.segunda_metade(y)
        
        return xh,xl,yh,yl
    
    @staticmethod
    def primeira_metade(x):
        primeira_metade = len(x) - (len(x)//2)
        return x[:int(primeira_metade)]
    
    @staticmethod
    def segunda_metade(x):
        if len(x) % 2 == 0:
            return x[int(len(x)/2):]
        else: 
            return x[int(len(x)/2)+1:]
    
    @staticmethod
    def iguala_tamanhos(x,y):
        max_tam = max(len(x),len(y))
        x = '0' * (max_tam - len(x))+x
        y = '0' * (max_tam - len(y))+y
        return x,y
    
    @staticmethod
    def verifica_carry(carry):
        if carry == '1':
            return True
        return False
    
    @staticmethod
    def verifica_ordm_0_1(bit1,bit2):
        if bit1 == '0' and bit2 == '1':
            return True
        return False
    
if len(sys.argv) != 3:
    print("Digite: python meukaratsuba.py <bin1> <bin2>")
    sys.exit(1)

try:
    if not re.fullmatch(r'[01]+',sys.argv[1]) or not re.fullmatch(r'[01]+',sys.argv[2]):
        raise ValueError
except ValueError:
    print("Valores incorretos, numeros devem serem compostos exclusivamente de 0 e 1")
    sys.exit(1)
  

bin1 = sys.argv[1]
bin2 = sys.argv[2]  

print(Karatsuba.algoritmo_karatuba(bin1, bin2))