
#Forma ruim
def ranks_ruim(list:list):
    
    ranks = []
    j_maior = list[0]
    i=0
    j=0
    
    for i in range(len(list)):
        print(f'Nota {list[i]}')
        for j in range(len(list)):
            if i != j:
                print(f'j_maior: {j_maior}, j = {list[j]}')
                if list[j] > j_maior:
                    j_maior = list[j]
                    rank += 1
                elif list[j] > list[i]:
                    rank+=1        
        ranks.append(rank)
        rank = 1
        print(f'rank = {rank} i = {list[i]}')
        
    return ranks

#Forma boa
def ranks_boa(list:list):
    
    dict_mem = {}
    set_sorted = sorted(set(list))[::-1]
    print(sorted(set(list)))
    
    #for r,i in enumerate(set_sorted): 
    #    dict_mem[i] = r+1
    
    #Abaixo tem mais clareza e simplicidade
    for r,i in enumerate(set_sorted,start=1): 
        dict_mem[i] = r
    
    return [dict_mem[i] for i in list]
list_nota = [10,2,11,10,19]

print(ranks_boa(list_nota))