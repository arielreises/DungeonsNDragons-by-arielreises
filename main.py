import random
from personagem import Personagem
from monstro import Monstro
from combate import realizar_combate, criar_monstro_esporadico

def criar_personagem():
    nome = input("Digite o nome do seu personagem: ")

    print("Escolha a classe do personagem:")
    print("1. Guerreiro")
    print("2. Mago")
    print("3. Ladino")

    opcao_classe = input("Digite o número da classe desejada: ")
    if opcao_classe == "1":
        classe = "Guerreiro"
        vida = random.randint(50, 100)
        ataque = random.randint(5, 15)
        defesa = random.randint(1, 10)
    elif opcao_classe == "2":
        classe = "Mago"
        vida = random.randint(30, 80)
        ataque = random.randint(10, 20)
        defesa = random.randint(1, 5)
    elif opcao_classe == "3":
        classe = "Ladino"
        vida = random.randint(40, 90)
        ataque = random.randint(8, 18)
        defesa = random.randint(3, 8)
    else:
        print("Opção inválida. Personagem será criado como Guerreiro padrão.")
        classe = "Guerreiro"
        vida = random.randint(50, 100)
        ataque = random.randint(5, 15)
        defesa = random.randint(1, 10)

    personagem = Personagem(nome, classe, vida, ataque, defesa)
    return personagem

def main():
    print("Bem-vindo ao jogo Dungeons & Dragons Simplificado!")

    while True:
        personagem = criar_personagem()
        vitorias = 0

        while True:
            monstro = criar_monstro_esporadico() if vitorias % 3 == 0 else Monstro(nome="Demônio", vida=40, ataque=18, defesa=8)
            personagem.mostrar_status()
            monstro.mostrar_status()

            continuar_combate = realizar_combate(personagem, monstro)

            if continuar_combate:
                vitorias += 1
            else:
                break

        print(f"\nTotal de vitórias: {vitorias}")

        opcao = input("\nEscolha a opção:\n1. Novo Jogo\n2. Encerrar o Jogo\nDigite o número da opção desejada: ")

        if opcao == "2":
            print("Jogo encerrado.")
            exit()

if __name__ == "__main__":
    main()
