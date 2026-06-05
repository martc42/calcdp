import math 

def dpamostral(*args):
 
 #calcula a média dos numeros
 media = (sum(args) / len(args))

 # calcula o desvio de cada numero e eleva ao quadrado, formando lista
 desvios = [(num - media) ** 2 for num in args]

 # soma os desvios
 somadesvios = sum(desvios)

 # calcula o desvio padrao amostral final
 dpfinal = math.sqrt(somadesvios / (len(args) - 1))

 print(f"Média: { media } ")

 return dpfinal


print(f"Desvio Padrão: {dpamostral(0.805, 0.8488, 0.9015, 0.8978, 0.8819, 0.8816, 0.875, 0.8758)}")


