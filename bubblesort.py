vetor = [9,8,7,6,5,4,3,2,1,0]
comparacoes = 0
trocas = 0

for l in range(0, len(vetor)-1):
    for i in range(0, (len(vetor) - 1) - l):
        comparacoes += 1  
        if(vetor[i] > vetor[i+1]):
            trocas +=1
            aux = vetor[i]
            vetor[i] = vetor[i+1]
            vetor[i+1] = aux
            
print("Vetor ordenado: ", vetor)
print("Quantidade de comparações: ", comparacoes)
print("Quantidade de trocas: ", trocas)
            
