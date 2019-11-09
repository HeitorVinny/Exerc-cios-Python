jogador=0
computador=0

while (jogador<3 and computador<3):
  import random
  print('jogador= {}' .format(jogador))
  print('computador= {}' .format(computador))

  print("Escolha: 1-pedra 2-papel 3-tesoura")

  jogo = int(input("Escolha a opção: "))
  cpu = random.randint(1,3)

  if(jogo==1):

    if(cpu==1):
        print('Empate')
    elif(cpu==2):
        print('voce perdeu! Papel cobre pedra!')
        c+=1
    elif(cpu==3):
        print('voce ganhou! Pedra quebra tesoura!')
        jogador+=1
  elif(jogo==2):
      if(cpu==1):
        print('voce ganhou! Papel cobre pedra!')
        jogador+=1
      elif(cpu==2):
        print('empate')
      elif(cpu==3):
        print('voce perdeu! Perdeu tesoura corta papel!')
        computador+=1
  elif(jogo==3):
    if(cpu==1):
        print('voce perdeu! Pedra quebra tesoura!')
        computador+=1
    elif(cpu==2):
        print('voce ganhou! Tesoura Corta Papel!')
        jogador+=1
    elif(cpu==3):
        print('empate')
  if(jogador==3):
      print('parabens, voce venceu o jogo!!')
  elif(computador==3):
      print('Nao foi dessa vez...')