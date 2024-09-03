import sys
import re
class Karatsuba:
    def __init__(self):
        pass

    def desloca_esquerda(self,m):
        deslocado = m + '0' * len(m)
        return deslocado

    def algoritmo_mult_num_longos(self,a,b):        
        
        if len(a) == 1 and len(b) == 1:
            return self.mult_bin_strings(a, b)
        
        m1a = a[:int(len(a)/2)]
        m2a = a[int(len(a)/2):]
        m1b = b[:int(len(b)/2)]
        m2b = b[int(len(b)/2):]
        print(f'A - {a} B - {b}')
        print(f"Metade 1 A - {m1a} Metade 1 B - {m1b}")
        print(f"Metade 2 A - {m2a} Metade 2 B - {m2b}")
        
        print('a1b1')
        a1b1 = self.mult_bin_strings(m1a,m1b)
        
        print('a2b2')
        a2b2 = self.mult_bin_strings(m2a,m2b)
        print('Entrou na recursao\n')
        z = self.algoritmo_mult_num_longos(self.sum_bin_strings(m1a,m1b),self.sum_bin_strings(m2a,m2b))
        print('Saiu da recursao')

        diff = self.diff_bin_strings(self.diff_bin_strings(z,a1b1),a2b2)
        
        diff_shift = self.desloca_esquerda(diff)
        a1b1_shift = self.desloca_esquerda(a1b1)
        
        return self.sum_bin_strings(self.sum_bin_strings(diff_shift,a1b1_shift),a2b2)

    def verifica_igualdade_bit(self,bit1,bit2):
        if bit1 == bit2:
            return True
        return False
    
    def verifica_carry(self,carry):
        if carry == '1':
            return True
        return False
        
    def verifica_ordm_0_1(self,bit1,bit2):
        if bit1 == '0' and bit2 == '1':
            return True
        return False
    
    def diff_bin_strings(self,x:str,y:str):
        if len(x) < len(y):
            novo_y = x
            x = y
            y = novo_y
            
        tam_max_x_y = max(len(x),len(y))
        
        xi = x.zfill(tam_max_x_y)[::-1]
        yi = y.zfill(tam_max_x_y)[::-1]
        
        carry = ''
        
        sub = ''
        
        for i in range(tam_max_x_y):
            if self.verifica_igualdade_bit(xi[i],yi[i]):
                if self.verifica_carry(carry):
                    sub += '1'
                else:
                    sub += '0'
            else:
                if self.verifica_ordm_0_1(xi[i],yi[i]):
                    if self.verifica_carry(carry):
                        sub += '0'
                    else:
                        sub += '1'
                        carry = '1'
                else:
                    if self.verifica_carry(carry):
                        sub += '0'
                        carry = '0'
                    else:
                        sub+='1'
               
        return sub[::-1].lstrip('0')
    
    def mult_bin_strings(self,x,y):
        print(f'Multiplica {x} com {y}')
        yi = y[::-1]
        result = ''
        for ind,i in enumerate(yi):
            if i == '1':
                desc = x + '0' * ind
                print(f'Result - {result} Desc - {desc} Index - {ind}')
                if result == '':
                    print(f'Resultado nao existia')
                    result = desc
                else:
                    result = self.sum_bin_strings(result, desc)
            else:
                desc = '0' * len(x)
                print(f'Result - {result} Desc - {desc}')
                result = self.sum_bin_strings(result,desc)
        print(f"Resultado da mult {result}")    
        return result
                
    
    def sum_bin_strings(self,x,y):
        print(f'Entrou na soma com x - {x} y - {y}')
        if x == '0' * len(x):
            print('Uma delas era tudo 0')
            return y
        elif y == '0' * len(y):
            print('Uma delas era tudo 0')
            return x
        
        tam_max_x_y = max(len(x),len(y))
        xi = x.zfill(tam_max_x_y)[::-1]
        yi = y.zfill(tam_max_x_y)[::-1]
        
        c = '0'
        sum = ''
        for i in range(tam_max_x_y):
            if self.verifica_igualdade_bit(xi[i],yi[i]):
                if xi[i] == '1':
                    if self.verifica_carry(c):
                        if i == tam_max_x_y-1:
                            sum += '11'
                        else:
                            sum += '1'
                    else:
                        if i == tam_max_x_y-1:
                            sum += '01'
                        else:
                            sum += '0'
                        c = '1'
                else:
                    if self.verifica_carry(c):
                        sum += '1'
                        c = '0'
                    else:
                        sum += '0'
            else:
                if self.verifica_carry(c):
                    if i == tam_max_x_y-1:
                        sum += '01'
                    else:
                        sum += '0'
                else:
                    sum+='1'
        print(f'Resultado da soma {sum[::-1]}')
        return sum[::-1]
        

k = Karatsuba()

if len(sys.argv) != 3:
    print("Digite: python karatsuba.py <bin1> <bin2>")
    sys.exit(1)

try:
    if not re.fullmatch(r'[01]+',sys.argv[1]) or not re.fullmatch(r'[01]+',sys.argv[2]):
        raise ValueError
except ValueError:
    print("Valores incorretos, numeros devem serem compostos exclusivamente de 0 e 1")
    sys.exit(1)
  

bin1 = sys.argv[1]
bin2 = sys.argv[2]

print(k.algoritmo_mult_num_longos(bin1,bin2))
#print(k.mult_bin_strings(bin1,bin2))
#print(k.diff_bin_strings(bin1,bin2))
#print(k.sum_bin_strings(bin1,bin2))

