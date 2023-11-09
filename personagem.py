import random

class Personagem:
    def __init__(self, nome, classe, vida, ataque, defesa):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.ataque_bonus = 0

    def atacar(self, alvo):
        dano = max(0, self.ataque + self.ataque_bonus - alvo.defesa)
        alvo.vida -= dano
        self.ataque_bonus += 1  # Incrementa o bônus de ataque
        return f"{self.nome} avança com fúria, atingindo {alvo.nome} e causando {dano} de dano!"

    def defender(self):
        self.defesa += 2
        return f"{self.nome} assume uma postura defensiva, aumentando sua defesa."

    def usar_habilidade(self, alvo):
        if self.classe == "Guerreiro":
            return self.atacar(alvo)
        elif self.classe == "Mago":
            return f"{self.nome} conjura uma bola de fogo ardente em direção a {alvo.nome}!"
        elif self.classe == "Ladino":
            return f"{self.nome} desaparece nas sombras e realiza um ataque furtivo em {alvo.nome}!"

    def ganhar_bonus(self):
        print(f"{self.nome} sente uma onda de poder e ganha um bônus de 5 pontos!")
        self.vida += 5
        self.ataque += 5
        self.defesa += 5

    def escolher_acao(self, alvo):
        print("\nEscolha a ação:")
        print("1. Atacar")
        print("2. Defender")
        print("3. Usar Habilidade")

        opcao_acao = input("Digite o número da ação desejada: ")

        if opcao_acao == "1":
            return self.atacar(alvo)
        elif opcao_acao == "2":
            return self.defender()
        elif opcao_acao == "3":
            return self.usar_habilidade(alvo)
        else:
            return f"{self.nome} fica indeciso e não realiza nenhuma ação."

    def mostrar_status(self):
        print("\nInformações do personagem:")
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque + self.ataque_bonus}")  # Mostra o ataque total considerando o bônus
        print(f"Defesa: {self.defesa}")
