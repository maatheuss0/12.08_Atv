#tratamento de erros

try
  resultado = 10/0
except ZeroDivisionErro:
  print("Erro: Divisao por 0 nao é permitida")
  
  
#implemente um bloco try-except para capturar um dindice fora dos limites de uma lista
lista = [1,2,3]
try
  elemento = lista[5]
except IndexError:
  print("Erro: Indice fora dos limites da lista")
  

#implemente um bloco try-except para capturar uma chave inexistente em um dicionario
lista = {'A':1,'B':2,'C':3}
try
  dicionario = lista["C"]
except KeyError:
  print("Erro: Indice fora do dicionario")
  
  
#Exercicio extra
def main():
  try:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    
    resultado = num1/ num2
    
  except ZeroDivisionError as e:
    pint("Erro: Divisao por zero nao permitida")
  
  except ValueError as e:
    print("Erro: Vai diminiur uma letra?")
    
  except Exception as e:
    print(f"Ocorreu um erro inesperado{e}")
  else:
    print(f"O resultado da divisao é {resultado}")
    
  finally:
    print("Programa finalizado")
    
main()

#capture e trace um excecao ao converter uma string para um inteiro
string = "abc"
try:
  numero = int(string)
except ValueError as e:
  print(f"Erro ao converter a string para um inteiro)

  
#Capture e trate excecoes em operacoes de dicionario e listas aninhadas
dicionario = {'a':[1,2,3], 'b':[4,5,6]}
try:
  elemento = dicionario['c'][0]
except KeyError:
  print("Erro: Chave inexistente no dicionario")
except IndexError:
  print("Erro: Indice fora dos limites da lista")

