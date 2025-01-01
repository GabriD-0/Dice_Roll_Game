import random

def rolar_dado():
    valor_minimo = 1
    valor_maximo = 6
    
    roll = random.randint(valor_minimo, valor_maximo)
    
    return roll


while True:
    try:
        jogadores = int(input("Quantos jogadores deseja? (2 - 4) "))
        #print(jogadores)
        if 2 <= jogadores <= 4:
            break
        else:
            print("Deve ser entre 2 - 4 jogadores.")
    
    except ValueError:
        print("Digite um número válido.")

pontuacao_maxima = 50
pontuacao_Jogador = [0 for i in range(jogadores)]

while max(pontuacao_Jogador) < pontuacao_maxima:
    for jogador_index in range(jogadores):
        print(f"Jogador {jogador_index+1}: {pontuacao_Jogador[jogador_index]}")
        print("Seu turno começou, boa sorte!")
        pontuacao_atual = 0
        
        while True:
            should_roll = input("Deseja rolar o dado? (s/n) ")
            if should_roll.lower() != "s":
                break
            
            value = rolar_dado()
            if value == 1:
                print(f"Você tirou um {value}! pontuação Zerada!")
                print("\nTurno finalizado!")
                current_score = 0
                break
                
            else:
                pontuacao_atual += value
                print(f"Você tirou um {value}. Pontuação atual: {pontuacao_atual}")
            
            print("Sua pontuaçao atual: ", pontuacao_atual)
            
        pontuacao_Jogador[jogador_index] += pontuacao_atual
        print(f"Jogador {jogador_index + 1} Sua pontuação atual: {pontuacao_Jogador[jogador_index]} \n")

pontuacao_maxima = max(pontuacao_Jogador)
jogador_vencedor = pontuacao_Jogador.index(pontuacao_maxima)
print(f"Jogador {jogador_vencedor + 1} venceu com {pontuacao_maxima} pontos!")