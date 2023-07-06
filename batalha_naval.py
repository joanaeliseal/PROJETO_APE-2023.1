# Alunas: Joana Elise, Letícia Leite, Maira Larissa e Thayná Rodrigues

#importando módulos
import random
import pickle

# Função para criar a matriz vazia
def criar_tabuleiro():
    COLUNAS = LINHAS = 8
    tabuleiro = [['~ ']*COLUNAS for i in range(LINHAS)]
    return tabuleiro

# Função para verificar se uma posição é válida
def posicao_valida(matriz, linha, coluna):
    for i in range(linha-1, linha+2):
        for j in range(coluna-1, coluna+2):
            if i >= 0 and i < 8 and j >= 0 and j < 8 and matriz[i][j] == '\033[32m'+'N '+'\033[m':
                return False
    return True

# Função para posicionar "N" em seis posições aleatórias na matriz
def posicionar_navios(matriz, navios):
    contador = 0
    while contador < navios:
        linha = random.randint(0, 7)
        coluna = random.randint(0, 7)
        if posicao_valida(matriz, linha, coluna):
            matriz[linha][coluna] = '\033[32m'+'N '+'\033[m'
            contador += 1
    return matriz

def imprimir_matriz(matriz):
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    LINHAS = COLUNAS = 8
    print('  A B C D E F G H ')
    for linha in range(LINHAS):
        print(f"{letras[linha]} ", end='')
        for coluna in range(COLUNAS):
            print(f"{matriz[linha][coluna]:2}", end="")
        print()

# Função para imprimir só os F e A, sem mostrar os navios N
def imprimir_matriz_FA(matriz):
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    LINHAS = COLUNAS = 8
    print('  A B C D E F G H ')
    for linha in range(LINHAS):
        print(f"{letras[linha]} ", end='')
        for coluna in range(COLUNAS):
            if matriz[linha][coluna] == '\033[32m'+'N '+'\033[m':
                print("~ ", end="")
            else:
                print(f"{matriz[linha][coluna]:2}", end="")
        print()

# Função para atacar o tabuleiro adversário
def atacar(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == '\033[32m'+'N '+'\033[m':
        print("\033[31m"+"\033[1m"+"FOGO!"+"\033[m")
        tabuleiro[linha][coluna] = '\033[31m'+'F '+'\033[m'
        return True
    else:
        if tabuleiro[linha][coluna] == '\033[32m'+'F '+'\033[m':
            print("Você já atirou aí!")
            return False
        elif tabuleiro[linha][coluna] == '\033[36m'+'A '+'\033[m':
            print("Você já atirou aí!")
            return False
        else:
            print("\033[36m"+"\033[1m"+"ÁGUA!"+"\033[m")
            tabuleiro[linha][coluna] = '\033[36m'+'A '+'\033[m'
        return False

# Função para verificar se todos os navios foram afundados
def todos_navios_afundados(tabuleiro):
    for linha in tabuleiro:
        if '\033[32m'+'N '+'\033[m' in linha:
            return False
    return True

# Função para salvar o estado do jogo em um arquivo
def salvar_jogo(tabuleiro_jogador1, tabuleiro_jogador2, jogador_atual):
    estado_jogo = {
        'tabuleiro_jogador1': tabuleiro_jogador1,
        'tabuleiro_jogador2': tabuleiro_jogador2,
        'jogador_atual': jogador_atual,
    }
    with open('jogo_salvo.pkl', 'wb') as arquivo:
        pickle.dump(estado_jogo, arquivo)

# Função para carregar o estado do jogo a partir de um arquivo
def carregar_jogo():
    try:
        with open('jogo_salvo.pkl', 'rb') as arquivo:
            estado_jogo = pickle.load(arquivo)
        return estado_jogo
    except FileNotFoundError:
        return None

# Função para exibir o menu e obter a escolha do jogador
def exibir_menu():
    print("\033[44m"+"\033[1m"+"\033[37m"+"\n=== BATALHA NAVAL ==="+"\033[m")
    print("1 - Novo Jogo")
    print("2 - Carregar Jogo Salvo")
    print("3 - Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def jogar_batalha_naval():
    while True:
        escolha = exibir_menu()

        if escolha == '1':
            # Novo Jogo
            tabuleiro_jogador1 = criar_tabuleiro()
            tabuleiro_jogador2 = criar_tabuleiro()
            print("Bem-vindo ao jogo Batalha Naval!")
            print("")

            # Solicitar a quantidade de navios
            quantidade_navios = int(input("Digite a quantidade de navios (máximo de 6): "))
            while quantidade_navios < 1 or quantidade_navios > 6:
                quantidade_navios = int(input("Quantidade inválida. Digite a quantidade de navios (máximo de 6): "))

            tabuleiro_jogador1 = posicionar_navios(tabuleiro_jogador1, quantidade_navios)
            tabuleiro_jogador2 = posicionar_navios(tabuleiro_jogador2, quantidade_navios)
            jogador_atual = 1

            while True:
                # Lógica do jogo
                letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                if jogador_atual == 1:
                    print("\nJogador 1:")
                    imprimir_matriz_FA(tabuleiro_jogador1)
                    print("\nSeu oponente:")
                    imprimir_matriz_FA(tabuleiro_jogador2)

                    #pergunta se o jogador quer ver seu tabuleiro
                    while True:
                      mostrar_navios = input("\033[1m"+"Deseja ver onde estão seus navios? [S/N]"+"\033[m")
                      if mostrar_navios not in 'sSnN':
                        print("Opção inválida.")
                        continue
                      else:
                        break
                    if mostrar_navios in "Ss":
                      imprimir_matriz(tabuleiro_jogador1)

                else:
                    print("\nJogador 2:")
                    imprimir_matriz_FA(tabuleiro_jogador2)
                    print("\nSeu oponente:")
                    imprimir_matriz_FA(tabuleiro_jogador1)

                    #pergunta se o jogador quer ver seu tabuleiro
                    while True:
                      mostrar_navios = input("\033[1m"+"Deseja ver onde estão seus navios? [S/N]"+"\033[m")
                      if mostrar_navios not in 'sSnN':
                        print("Opção inválida.")
                        continue
                      else:
                        break
                    if mostrar_navios in "Ss":
                      imprimir_matriz(tabuleiro_jogador2)



                while True:
                        letra_linha = input("\033[41m"+"\033[1m"+"Digite a linha que você quer atacar (A-H)"+"\033[m").upper()
                        letra_coluna = input("\033[41m"+"\033[1m"+"Digite a coluna que você quer atacar (A-H)"+"\033[m").upper()
                        if letra_linha not in letras or letra_coluna not in letras:
                            print("Coordenadas inválidas")
                            continue
                        else:
                            coordenada_linha = letras.index(letra_linha)
                            coordenada_coluna = letras.index(letra_coluna)
                            break


                # Realizar o ataque
                if jogador_atual == 1:
                    acertou = atacar(tabuleiro_jogador2, coordenada_linha, coordenada_coluna)  # Ataque do jogador 1 ao tabuleiro do jogador 2
                else:
                    acertou = atacar(tabuleiro_jogador1, coordenada_linha, coordenada_coluna)  # Ataque do jogador 2 ao tabuleiro do jogador 1


                # Verificar se todos os navios foram afundados
                if jogador_atual == 1 and todos_navios_afundados(tabuleiro_jogador2):
                    print("\033[4m"+"\033[1m"+"\033[32m"+"Parabéns! Jogador 1 venceu o jogo!"+"\033[0m")
                    break
                elif jogador_atual == 2 and todos_navios_afundados(tabuleiro_jogador1):
                    print("\033[4m"+"\033[1m"+"\033[32m"+"Parabéns! Jogador 2 venceu o jogo!"+"\033[0m")
                    break

                # Trocar de jogador apenas se o tiro não acertou um navio
                if not acertou:
                    jogador_atual = 1 if jogador_atual == 2 else 2



                opcao = input("\033[47m"+"\033[30m"+"Deseja salvar o jogo e sair? (S/N): "+"\033[0m").upper()
                if opcao == 'S':
                    salvar_jogo(tabuleiro_jogador1, tabuleiro_jogador2, jogador_atual)
                    print("Jogo salvo. Voltando ao menu.")
                    break  # Saia do loop interno e retorne ao menu principal

        elif escolha == '2':
            # Carregar Jogo Salvo
            estado_salvo = carregar_jogo()
            if estado_salvo is None:
                print("Nenhum jogo salvo encontrado.")
                continue
            else:
                tabuleiro_jogador1 = estado_salvo['tabuleiro_jogador1']
                tabuleiro_jogador2 = estado_salvo['tabuleiro_jogador2']
                jogador_atual = estado_salvo['jogador_atual']
                print("Jogo carregado.")

            while True:
                    # Lógica do jogo
                    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                    if jogador_atual == 1:
                        print("\nJogador 1:")
                        imprimir_matriz_FA(tabuleiro_jogador1)
                        print("\nSeu oponente:")
                        imprimir_matriz_FA(tabuleiro_jogador2)


                        #pergunta se o jogador quer ver seu tabuleiro?
                        while True:
                          mostrar_navios = input("\033[1m"+"Deseja ver onde estão seus navios? [S/N]"+"\033[m")
                          if mostrar_navios not in 'sSnN':
                            print("Opção inválida.")
                            continue
                          else:
                            break
                        if mostrar_navios in "Ss":
                          print("\nSeus navios:")
                          imprimir_matriz(tabuleiro_jogador1)

                    else:
                        print("\nJogador 2:")
                        imprimir_matriz_FA(tabuleiro_jogador2)
                        print("\nSeu oponente:")
                        imprimir_matriz_FA(tabuleiro_jogador1)

                        #pergunta se o jogador quer ver seu tabuleiro?
                        while True:
                          mostrar_navios = input("\033[1m"+"Deseja ver onde estão seus navios? [S/N]"+"\033[m")
                          if mostrar_navios not in 'sSnN':
                            print("Opção inválida.")
                            continue
                          else:
                            break
                        if mostrar_navios in "Ss":
                          print("\nSeus navios:")
                          imprimir_matriz(tabuleiro_jogador2)

                    while True:
                        letra_linha = input("\033[41m"+"\033[1m"+"Digite a linha que você quer atacar (A-H)"+"\033[m").upper()
                        letra_coluna = input("\033[41m"+"\033[1m"+"Digite a coluna que você quer atacar (A-H)"+"\033[m").upper()
                        if letra_linha not in letras or letra_coluna not in letras:
                            print("Coordenadas inválidas")
                            continue
                        else:
                            coordenada_linha = letras.index(letra_linha)
                            coordenada_coluna = letras.index(letra_coluna)
                            break

                    # Realizar o ataque
                    if jogador_atual == 1:
                        acertou = atacar(tabuleiro_jogador2, coordenada_linha, coordenada_coluna)  # Ataque do jogador 1 ao tabuleiro do jogador 2
                    else:
                        acertou = atacar(tabuleiro_jogador1, coordenada_linha, coordenada_coluna)  # Ataque do jogador 2 ao tabuleiro do jogador 1


                    # Verificar se todos os navios foram afundados
                    if jogador_atual == 1 and todos_navios_afundados(tabuleiro_jogador2):
                        print("\033[4m"+"\033[1m"+"\033[32m"+"Parabéns! Jogador 1 venceu o jogo!"+"\033[0m")
                        break
                    elif jogador_atual == 2 and todos_navios_afundados(tabuleiro_jogador1):
                        print("\033[4m"+"\033[1m"+"\033[32m"+"Parabéns! Jogador 2 venceu o jogo!"+"\033[0m")
                        break

                    # Trocar de jogador apenas se o tiro não acertou um navio
                    if not acertou:
                        jogador_atual = 2 if jogador_atual == 1 else 1

                    opcao = input("\033[47m"+"\033[30m"+"Deseja salvar o jogo e sair? (S/N): "+"\033[0m").upper()
                    if opcao == 'S':
                        salvar_jogo(tabuleiro_jogador1, tabuleiro_jogador2, jogador_atual)
                        print("Jogo salvo. Voltando ao menu.")
                        break  # Saia do loop interno e retorne ao menu principal

        elif escolha == '3':
            # Sair do jogo
            print("Obrigado por jogar! Até mais!")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")

# Iniciar o jogo
jogar_batalha_naval()
