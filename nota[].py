atividades  = []
#cadastre informacao de cinco aluno
for i in range (5):
    nome = input("digite o nome do aluno:")
    av1= float(input("avaliacao numero um:"))
    #flot (numero com virgula)
    av2 = float(input("avaliacao numero dois:"))
    #calcula a media
    media = (av1 + av2) / 2
    situacao="Aprovado" if media>=6 else "Reprovado"
    # adicione os dados coletados das atividades
    atividades.append([nome,av1,av2,media,situacao])
    
    print("/n---resutado final---")
    #inicia um novo loop que pecorre cada atividade na lista de atividades
    for atividade in atividades: 

     print(f"{atividade[0]} - atividade 1:{atividade[1]}|atividade 2:{atividade[2]}|media:{atividade[3]:.2f} Situação:{atividade[4]}")