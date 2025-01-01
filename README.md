### README

# Jogo de Dados

Este é um jogo simples de dados para 2 a 4 jogadores. O objetivo do jogo é alcançar uma pontuação máxima (50 pontos, por padrão) antes dos outros jogadores. Durante o turno, os jogadores podem rolar o dado para acumular pontos, mas se tirarem o número 1, perdem todos os pontos acumulados no turno e sua vez termina!

## Como Funciona

1. O jogo solicita o número de jogadores (entre 2 e 4).
2. Cada jogador joga na sua vez:
   - Pode optar por rolar o dado ou finalizar o turno.
   - Ao rolar o dado:
     - Se o valor for **1**, o jogador perde todos os pontos acumulados no turno e passa a vez.
     - Caso contrário, o valor é somado aos pontos acumulados no turno.
   - Ao finalizar o turno, os pontos acumulados são adicionados à pontuação total do jogador.
3. O jogo termina quando um jogador atinge ou ultrapassa a pontuação máxima (50 pontos).
4. O jogador com a maior pontuação vence!

---

## Funcionalidades

- Suporte para 2 a 4 jogadores.
- Sistema de turnos com controle de pontuação individual.
- Restrições de entrada para evitar valores inválidos.
- Mensagens interativas para melhor acompanhamento do jogo.

---

## Requisitos

- Python 3.6 ou superior.

---

## Como Executar

1. Certifique-se de que o Python está instalado no seu computador.
2. Faça o download ou clone este repositório.
3. Execute o arquivo do jogo com o seguinte comando no terminal:
   ```bash
   python jogo_dados.py
   ```
4. Siga as instruções no terminal para iniciar e jogar.

---

## Exemplo de Execução

```plaintext
Quantos jogadores deseja? (2 - 4) 3
Jogador 1: 0
Seu turno começou, boa sorte!
Deseja rolar o dado? (s/n) s
Você tirou um 5. Pontuação atual: 5
Deseja rolar o dado? (s/n) s
Você tirou um 2. Pontuação atual: 7
Deseja rolar o dado? (s/n) n
Jogador 1 Sua pontuação atual: 7

Jogador 2: 0
Seu turno começou, boa sorte!
Deseja rolar o dado? (s/n) s
Você tirou um 1! Pontuação Zerada!
Turno finalizado!

... (continua até alguém alcançar 50 pontos)
Jogador 1 venceu com 52 pontos!
```

---

## Personalização

- **Alterar a Pontuação Máxima**: No código, ajuste a variável `pontuacao_maxima` para definir uma nova pontuação alvo.
- **Alterar o Intervalo do Dado**: Modifique `valor_minimo` e `valor_maximo` na função `rolar_dado` para usar diferentes intervalos.

---

## Licença

Este projeto é de uso livre para fins educativos e recreativos.

---

Divirta-se jogando! 🎲
