import random

class Monstro:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        alvo.vida -= dano
        return f"{self.nome} investe contra {alvo.nome} e inflige {dano} de dano!"

    def usar_habilidade(self, alvo):
        if self.nome == "Goblin":
            return f"{self.nome} joga uma poção venenosa em {alvo.nome}!"
        elif self.nome == "Ogro":
            return f"{self.nome} desfere um golpe esmagador em {alvo.nome}!"

    def ganhar_bonus(self):
        print(f"{self.nome} parece ter ficado mais forte e ganha um bônus de 5 pontos!")
        self.vida += 5
        self.ataque += 5
        self.defesa += 5

    def escolher_acao(self, alvo):
        opcao_acao = random.choice(["Atacar", "Usar Habilidade"])

        if opcao_acao == "Atacar":
            return self.atacar(alvo)
        elif opcao_acao == "Usar Habilidade":
            return self.usar_habilidade(alvo)
        else:
            return f"{self.nome} fica indeciso e não realiza nenhuma ação."

    def mostrar_status(self):
        print("\nInformações do monstro:")
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")
        print(f"Defesa: {self.defesa}")
