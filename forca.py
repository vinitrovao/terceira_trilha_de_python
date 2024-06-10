import random

times_de_futebol = ["Fluminense", "Flamengo",
                    "Palmeiras", "Real Madrid", "Chelsea", "Manchester City",
                    "Bayern de Munique", "Borussia Dortmund",
                    "Paris Saint-Germain", "Inter de Milão", "Juventus",
                    "Porto", "Benfica", "Atlético de Madrid", "River Plate",
                    "Boca Juniors"]
palavras_aleatorias = ["Casa", "Computador",
                       "Carro", "Bicicleta", "Cachorro", "Montanha",
                       "Cadeira", "Faca", "Dente", "Vaso", "Ladeira"]
quimica = ["Ligação", "Molécula", "Reação",
           "Elemento", "Composto", "Hidrogênio", "Oxigênio", "Elétron"]
linguagem_de_programacao = ["Python", "JavaScript",
                            "Java", "CSharp", "Ruby", "HTML", "CCS", "PHP"]


def escolher_palavra(categoria):
    if categoria == 1:
        return random.choice(times_de_futebol)
    elif categoria == 2:
        return random.choice(palavras_aleatorias)
    elif categoria == 3:
        return random.choice(quimica)
    elif categoria == 4:
        return random.choice(linguagem_de_programacao)
    else:
        return None


def jogo_da_forca():
    print("Bem-vindo ao jogo da forca!")
    print("Escolha uma categoria:")
    print("1. Times de Futebol")
    print("2. Palavras Aleatórias")
    print("3. Química")
    print("4. Linguagem de Programação")

    categoria = int(input("Digite o número da categoria escolhida: "))
    palavra = escolher_palavra(categoria).upper()
    letras_adivinhadas = []
    tentativas = 10
    palavra_oculta = ["_"] * len(palavra)

    while tentativas > 0 and "_" in palavra_oculta:
        print("\nPalavra:", " ".join(palavra_oculta))
        print(f"Tentativas restantes: {tentativas}")
        letra = input("Digite uma letra: ").upper()

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        letras_adivinhadas.append(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas -= 1
            print(f"Letra {letra} não está na palavra.")

    if "_" not in palavra_oculta:
        print("\nParabéns! Você adivinhou a palavra:", palavra)
    else:
        print("\nVocê perdeu! A palavra era:", palavra)


jogo_da_forca()
