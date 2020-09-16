from random import randint
from time import sleep
nome = input('Insira seu nome: ').strip()
while True:
	print('=' * 20)
	print('    Jogos V2.0.1')
	print('=' * 20)
	jogo = int(
	    input(
	        '[1] Para Jogo da adivinhação\n[2] Para JoKenPo\n[3] Para Par ou Ímpar\n[4] Para fechar o programa\n--------------> '
	    ))
	if jogo == 1:
		print('=' * 31)
		print('      Jogo Da Adivinhação')
		print('=' * 31)
		Nvl = 0
		dnvadv = 1
		while True:
			while Nvl == 0:
				niveladv = int(
				    input(
				        'Selecione o nivel que quer jogar: \n\033[32m[1]\033[m Para facil\n\033[33m[2]\033[m Para Medio\n\033[31m[3]\033[m Para Dificil\n-----------------> '
				    ))
				if niveladv == 1:
					n2 = 2
					Nvl = 1
				elif niveladv == 2:
					n2 = 3
					Nvl = 1
				elif niveladv == 3:
					n2 = 4
					Nvl = 1
				else:
					print('\033[31mNivel Inválido!\n\033[m')
				break
			while dnvadv == 1:
				computadoradv = randint(1, n2)
				print(
				    f'Pensarei em um número de 1 à {n2}, se você acertar, você venceu!'
				)
				sleep(0.5)
				print('Pensando...')
				sleep(0.5)
				jogadoradv = int(input('Em qual número eu pensei? '))
				print('-' * 31)
				print(f'Eu pensei no número {computadoradv}')
				if jogadoradv == computadoradv:
					print('Acertou, você me venceu!')
					print('-' * 31)
					print(f'\03[32m{nome}\033[m Vence!')
				else:
					print('Você errou, Você perdeu!')
					print('-' * 31)
					print('\033[31mComputador\033[m Vence!')
				print('=' * 31)
				break
			dnvadv = int(
			    input(
			        '[1] Para jogar novamente\n[2] Para Alterar a dificuldade\n[3] Para Voltar ao Menu\n--------------> '
			    ))
			if dnvadv == 2:
				Nvl = 0
			elif dnvadv == 3:
				break
	elif jogo == 2:
		lista = ['Pedra', 'Papel', 'Tesoura']
		dnvppt = 1
		print('=' * 13)
		print('   JoKenPo')
		print('=' * 13)
		while True:
			while dnvppt == 1:
				computadorjkp = randint(0, 2)
				jogadorjkp = int(
				    input(
				        '[1] Para Pedra\n[2] Para Papel\n[3] Para Tesoura\n-----------------> '
				    ))
				sleep(0.5)
				print('    JO', end=' ')
				sleep(0.5)
				print('KEN', end=' ')
				sleep(0.5)
				print('PO')
				print('-' * 20)
				print(f'\033[31mComputador\033[m jogou {lista[computadorjkp]}')
				print(f'\033[32m{nome}\033[m Jogou {lista[jogadorjkp - 1]}')
				print('-' * 20)
				if jogadorjkp - 1 == computadorjkp:
					print('       \033[33mEMPATE!\033[m')
				elif jogadorjkp == 1 and computadorjkp == 2 or jogadorjkp == 2 and computadorjkp == 1 or jogadorjkp == 3 and computadorjkp == 1:
					print(f'\033[32m{nome}\033[m Vence!')
				else:
					print('\033[31mComputador\033[m Vence!')
				print('-' * 20)
				dnvppt = int(
				    input(
				        '[1] Para jogar novamente\n[2] Para Voltar ao Menu\n----------> '
				    ))
			break
	elif jogo == 3:
		print('=' * 20)
		print('    Par ou Ímpar')
		print('=' * 20)
		dnvpoi = 1
		while True:
			while dnvpoi == 1:
				computadorpoi = randint(1, 10)
				while True:
					jogadorpoi = int(input('Diga um número de 1 a 10: '))
					if jogadorpoi >= 1 and jogadorpoi <= 10:
						break
					else:
						print('Número Inválido!')
				while True:
					jogadorpoi2 = input('Par Ou Ímpar? [P/I]: ').upper()
					if jogadorpoi2 in 'PI':
						break
					else:
						print('Entrada Inválida!')
				print('-' * 20)
				print('   PAR ', end='')
				sleep(0.5)
				print('OU ', end='')
				sleep(0.5)
				print('ÍMPAR')
				print('-' * 20)
				s = jogadorpoi + computadorpoi
				print(f'\033[32m{nome}\033[m jogou {jogadorpoi}')
				print(f'\033[31mComputador\033[m jogou {computadorpoi}')
				print('-' * 20)
				if s % 2 == 0 and jogadorpoi2 == 'P':
					print(f'     {s} é Par!')
					print('-' * 20)
					print(f'\033[32m{nome}\033[m Vence!')
				elif s % 2 != 0 and jogadorpoi2 == 'I':
					print(f'     {s} é Par!')
					print('-' * 20)
					print(f'\033[32m{nome}\033[m Vence!')
				else:
					print(f'     {s} é Ímpar!')
					print('-' * 20)
					print('\033[31mComputador\033[m Vence!')
				print('-' * 20)
				dnvpoi = int(
				    input(
				        '[1] Para jogar de novo\n[2] Para Voltar ao Menu\n---------> '
				    ))
				if dnvpoi == 2:
					dnvpoi = 0
			break
	if jogo == 4:
		print('\033[31mSaindo...\033[m ')
		sleep(1)
		break
