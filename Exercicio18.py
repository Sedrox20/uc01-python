nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

if(media<4):
    print('Aluno reprovado')

elif(media>7):
    print('Aluno aprovado direto')

else:
    print(f'Aluno em recuperação com a nota {media}')
    notarec = float(input('Digite a nota de recuperação: '))
    if(notarec<5):
       print('Reprovado na recuperação')
    else:
       print('Aprovado na Recuperação')



