"""
GUESS THE NUMBER

Pedir ao utilizador para inserir o nome

IA: GERAR NÚMERO 0-20

UTILIZADOR:
6 TENTATIVAS PARA ACERTAR

IA: APENAS RESPONDE SUPERIOR OU INFERIOR
IA: NÚMERO DE TENTATIVAS RESTANTES
 ----------------
VITÓRIA
IA: MENSAGEM DE SUCESSO
IA: NÚMERO NECESSÁRIO PARA ACERTAR

-----------------
Jogar outra vez?

-----------------
Pensar em Scoreboard
Guardar a informação do Jogador Vencedor e número de tentativas utilizado
"""
import random

nome = input("Insira o seu nome: ")
print("Estou a pensar em um número entre 0 e 20")
numero = random.randint(0,20)
tentativas = 0
while tentativas < 6:
  tentativas += 1
  print(f"Tentativa {tentativas}")
  escolha = int(input("Insira um número: "))
  if escolha == numero:
    print(f"Parabéns {nome}!acertas-te em {tentativas} tentativas!")
    break
  elif escolha > numero:
    print("É menor")
  elif escolha < numero:
    print("É maior")
if tentativas == 6:
  print(f"Perdes-te! O número era {numero}")
