from random import randint
from operator import itemgetter
from time import sleep

jogadores = {'jogador_1': randint(1, 6), 'jogador_2': randint(1, 6),
             'jogador_3': randint(1, 6), 'jogador_4': randint(1, 6)}
print('====Numeros Sorteados====')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('_='*20)
print("====º_Ranking_º====")
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
