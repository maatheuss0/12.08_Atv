#tratamento de erros

tryCatch({
  resultado <- 10/0
}, error = function(e){
  print("Erro: Divisão por zero não é permitida")
})

#implemente um bloco try-except para capturar um dindice fora dos limites de uma lista
lista <- c(1,2,3)
tryCatch({
  elemento <- lista[5]
},error = function(e){
  print("Erro: Indice fora dos limites da lista")
})

#capture e trace um excecao ao converter uma string para um inteiro
string <- "abc"
tryCatch({
  numero <- as.integer(string)
}, warning = function(w){
  print("Erro: Conversao de string para inteiro falhou")
})

#Capture e trate excecoes em operacoes de dicionario e listas aninhadas
dicionario <- lista(a = c(1,2,3), b = c(4,5,6))
tryCatch({
  elemento <- dicionario[['c']][1]
}, error = function(e){
  if(inherits(e,"simpleError")){
    print("Error: Chave inexistente no dicionario ou indice fora dos limites da lista")
  }
})