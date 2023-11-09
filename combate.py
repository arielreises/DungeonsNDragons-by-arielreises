import random
from personagem import Personagem
from monstro import Monstro

def criar_monstro_esporadico():
    opcao_monstro = random.choice(["Dragão", "Demônio"])
    if opcao_monstro == "Dragão":
        return Monstro(nome="Dragão", vida=50, ataque=15, defesa=10)
    elif opcao_monstro == "Demônio":
        return Monstro(nome="Demônio", vida=40, ataque=18, defesa=8)

def realizar_combate(personagem, monstro):
    print("\n--- Início do Combate ---")
    while personagem.vida > 0 and monstro.vida > 0:
        print("\nTurno do jogador:")
        acao_jogador = personagem.escolher_acao(monstro)
        print(acao_jogador)
        monstro.mostrar_status()

        if monstro.vida <= 0:
            print(f"{monstro.nome} foi derrotado!")
            personagem.ganhar_bonus()
            break

        print("\nTurno do monstro:")
        acao_monstro = monstro.escolher_acao(personagem)
        print(acao_monstro)
        personagem.mostrar_status()

        if personagem.vida <= 0:
            print(f"{personagem.nome} foi derrotado!")
            break

        opcao = input("\nEscolha a opção:\n1. Continuar o Combate\n2. Próximo Combate\n3. Voltar ao Menu Inicial\n4. Encerrar o Jogo\nDigite o número da opção desejada: ")

        if opcao == "2":
            return True  # Sinaliza que o jogador quer ir para o próximo combate
        elif opcao == "3":
            return False  # Sinaliza que o jogador quer voltar ao menu inicial
        elif opcao == "4":
            print("Jogo encerrado.")
            exit()

    if personagem.vida <= 0:
        print(f"{personagem.nome} está caído no chão, derrotado!")
    elif monstro.vida <= 0:
        print(f"{monstro.nome} cai perante a força avassaladora de {personagem.nome}!")

    print("--- Fim do Combate ---")
    return False
