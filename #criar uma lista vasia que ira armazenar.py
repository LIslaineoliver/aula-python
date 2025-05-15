#criar uma lista vasia que ira armazenar os dados da comissoes dos funcionarios
comissoes=[]

#loop que, que neste caso,roda apenas 1 vez(poderia ser aumentado para mais fucionarios)
for i in range(1):
    nome =input("digite o nome do funcionario:")
    comissaoum = float(input("digite sua comissao no primeiro mes:"))
    #float (numero com virgula)
    comissaodois = float(input("digite sua comissao no segundo mes"))
    #calcula a media
    media = (comissaoum + comissaodois)/2
    #adicione os dados coletados a lista'comissoes'no formato de dicionario
    comissoes.append({
    "nome": nome,
    "comissao 1":comissaoum,
    "comissao 2":comissaodois,
    "media": media
    })

print("/n---resultado final---")
#inicia um novo loop que percorre cada comissao da lista de comissoes
for comissao in comissoes:
 print(f"{comissao['nome']}-comissao 1:{comissao['comissao 1']}|comissao 2:{comissao['comissao 2']}|media:{comissao['media']:.2f}")
