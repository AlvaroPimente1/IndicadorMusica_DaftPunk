import random

def programa():
    
    musicas = [
                ["Giorgio By Moroder","Vocal", "Futurista","Agitada", "Popular"],
                ["Short Circuit","naoVocal", "Futurista","Agitada", "Popular"],
                ["Robot Rock","naoVocal", "naoFuturista","Agitada", "Popular"],
                ["NightVision","naoVocal", "naoFuturista","naoAgitada", "Popular"],
                ["Nocturne","naoVocal", "naoFuturista","naoAgitada", "naoPopular"],
                ["Doin It Right","Vocal", "Futurista","Agitada", "naoPopular"],
                ["The Game Of Love","Vocal", "Futurista","naoAgitada", "naoPopular"],
                ["Within","Vocal", "naoFuturista","naoAgitada", "naoPopular"],
                ["Face to Face","Vocal", "naoFuturista","Agitada", "naoPopular"],
                ["Get Lucky","Vocal", "naoFuturista","Agitada", "Popular"],
                ["Touch","Vocal", "Futurista","naoAgitada", "Popular"],
                ["Something About Us","Vocal", "naoFuturista","naoAgitada", "Popular"],
                ["Contact","naoVocal", "Futurista","Agitada", "naoPopular"],
                ["Veridis Quo","naoVocal", "Futurista","Agitada", "Popular"],
                ["MotherBoard","naoVocal", "Futurista","naoAgitada", "naoPopular"],
                ["High Fidelity","naoVocal", "naoFuturista","Agitada", "naoPopular"],
                
                ]

    # Funções

    def adicionarMusica():   
        nomeAdicionada = str(input("Insira o nome da música que deseja adicionar:\n")).strip().title()

        perguntaVocal = str(input("A musica adicionada tem vocal? S/N\n")).strip().upper()
        if perguntaVocal == "S": vocalAdicionada = "Vocal"
        elif perguntaVocal == "N": vocalAdicionada = "naoVocal"
        else: tentarNovamente()

        perguntaFuturista = str(input("A musica adicionada é futurista? S/N\n")).strip().upper()
        if perguntaFuturista == "S": futuristaAdicionada = "Futurista"
        elif perguntaFuturista == "N": futuristaAdicionada = "naoFuturista"
        else: tentarNovamente()

        perguntaAgitada = str(input("A musica adicionada é agitada? S/N\n")).strip().upper()
        if perguntaAgitada == "S": agitadaAdicionada = "Agitada"
        elif perguntaAgitada == "N": agitadaAdicionada = "naoAgitada"
        else: tentarNovamente()

        perguntaPopular = str(input("A musica adicionada é popular? S/N\n")).strip().upper()
        if perguntaPopular == "S": popularAdicionada = "Popular"
        elif perguntaPopular == "N": popularAdicionada = "naoPopular"
        else: tentarNovamente()

        serieAdicionada = [nomeAdicionada, vocalAdicionada, futuristaAdicionada, agitadaAdicionada, popularAdicionada]
        musicas.append(serieAdicionada)

    def removerMusica():
            n = 0
            for x in musicas:
                print(str(n) + ". " + x[0])
                n += 1
            retirarMusica = input("Qual musica você quer tirar? (0 ate {str((len(musicas)) - 1)})")
            n = 0
            x = len(musicas)
            if int(retirarMusica) in range(x):
                musicas.pop(int(retirarMusica))
                for x in musicas:
                    print(str(n) + ". " + x[0])
                    n += 1
            else:
                print("Digite um numero valido")
                removerMusica()
            print("Ok,continuaremos")

    def tentarNovamente():
        replay = str(input("Deseja voltar ao menu? S/N\n")).strip().upper()
        if replay == "S":
            programa()
        elif replay == "N":
            print("-=-" * 20)
            print("FIM do programa")
        else:
            print("Valor não válido para a pergunta")
            tentarNovamente()

    def aleatorio():
        sugestaoAleatoria = random.choice(musicas)
        print("-=-" * 20)
        print(f"Sua música aleatória sugerida é {sugestaoAleatoria}\n")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    perguntaAdicionar = str(input("Deseja adicionar alguma música na lista? S/N\n")).strip().upper()
    if perguntaAdicionar == "S": adicionarMusica()
    else: print("OK\n")

    perguntaRemover = str(input("Deseja remover alguma musica? S/N\n")).strip().upper()
    if perguntaRemover == "S": removerMusica()
    else: print("OK\n")

    formaEscolha = str(input("Selecione 1 caso queira uma pesquisa detalhada\nSelecione 2 caso queira uma música aleatória\n")).strip()
    if formaEscolha == "2":
        aleatorio()
        replay = str(input("Deseja outra sugestão aleatória? S/N\n")).strip().upper()
        if replay == "S":
            while replay == "S":
                aleatorio()
                replay = str(input("Deseja outra sugestão aleatória? S/N\n")).strip().upper()
                if replay == "N":
                    print("-=-" * 20)
                    tentarNovamente()
                    break
                elif replay == "S":
                    continue
                else:
                    print("Valor não válido para a pergunta")
                    tentarNovamente()
        elif replay == "N":
            print("-=-" * 20)
            tentarNovamente()
        else:
            print("Valor não válido para a pergunta")
            tentarNovamente()
        
    #elif formaEscolha == "3":
    #    print(musicas)

    elif formaEscolha == "1":
        
        vocal = str(input("Quer uma musica com letra além de uma frase? S/N\n")).strip().upper()
        if vocal == "S": vocal = "Vocal"
        if vocal == "N": vocal = "naoVocal"
        
        futurista = str(input("Quer uma musica futurista? S/N\n")).strip().upper()
        if futurista == "S": futurista = "Futurista"
        if futurista == "N": futurista = "naoFuturista"
        
        agitada = str(input("Quer uma musica agitada? S/N\n")).strip().upper()
        if agitada == "S": agitada = "Agitada"
        if agitada == "N": agitada = "naoAgitada"
        
        popular = str(input("Quer uma musica popular? S/N\n")).strip().upper()
        if popular == "S": popular = "Popular"
        if popular == "N": popular = "naoPopular"


        y = [0] * len(musicas)
        n = 0
        indicar = []
        for x in musicas:
            if vocal == x[1]: 
                y[n] = y[n] + 1
            if futurista == x[2]: 
                y[n] = y[n] + 1
            if agitada == x[3]: 
                y[n] = y[n] + 1
            if popular == x[4]: 
                y[n] = y[n] + 1
            if y[n] == 3 :
                indicar.append(x[0])
            if y[n] == 4 :
                indicar.insert(0,x[0])
            n += 1
        if len(indicar) > 0: 
            print(f"A sua musica sugerida é: {(indicar[0])}")
        if len(indicar) == 0: 
            print("Não consegui recomendar uma música.")

programa()