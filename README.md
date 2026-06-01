# Global Solution: Pensamento Computacional e Automação com Python

## Explicação do Programa

### Propósito

O programa foi criado para simular um sistema de controle de uma missão espacial que consegue: analizar e armazenar dados de uma missão, criar niveís de risco para informar o usuario sobre problemas, gerar alertas e soluções, e exibir um relatório cheio de informação usavél para proximas missões.

### Dados da Missão 

A parte central do programa é os dados inseridos na variável 'dados_missao'. Em ordem, contém: *Temperatura, Comunicações, Energia, Oxigenio, e Estabilidade*.

Esses 5 dados são inseridos 6 vezes na variável 'dados_missao' para simular 6 'ciclos', 6 estagios diferente de uma missão real. No fim, é possivél entender os dados de tal forma:

| Ciclo | Temperatura (°C) | Comunicação (%) | Bateria (%) | Oxigênio (%) | Estabilidade (%) | Cenário |
|---|---|---|---|---|---|---|
| 1 | 22 | 95 | 91 | 97 | 92 | Início da missão |
| 2 | 25 | 83 | 70 | 93 | 85 | Estabilização dos sistemas |
| 3 | 29 | 35 | 63 | 91 | 71 | Queda parcial de comunicação |
| 4 | 34 | 42 | 31 | 83 | 53 | Alerta de energia |
| 5 | 40 | 24 | 18 | 74 | 32 | Risco operacional |
| 6 | 32 | 53 | 31 | 84 | 51 | Tentativa de recuperação |

### Análise de Ciclos

Quando os dados forem inseridos por um usúario, o programa irá rodar a análise desses dados usando a função 'analise()'. Cada dado tem sua própria parametrização para o programa poder criar um nível de risco para os dados, junto com um valor de risco.

Se a de um ciclo temperatura for menor que 18°C ou entre 30°C e 35°C, é dado um valor de *1*, e a classificação de risco 'ATENÇÃO'. Se ela for maior que 35°C, então sera dada um valor de *2* e a classificação de risco 'CRÍTICO'. Se o dado não equivaler a nenhum dos dois, é dado um valor de *0*, e a classificação de risco 'NORMAL'. Assim e diante, cada um com seus proprios parâmetros.

### Classificação de Risco

Com os riscos analisados da função 'analise()', o programa em seguinte executa 'classificacao()'. Ele junta todos os valores emitidos pelos 5 dados da análise, e cria um 'score'. 

Se o score for menor que 2, mostra 'MISSÃO ESTAVEL'. Se o score for entre 3 e 5, mostra 'MISSÃO EM ATENÇÃO'. Se o score for maior que 6, mostra 'MISSÃO CRÍTICA'.

### Recomendação de Solução

Após classificar o risco da missão, roda por um sistema que ira escolher a recomendação do que fazer para solucionar o maior problema. Há uma prioridade de qual ele pedira para arrumar primeiro.

```Oxigênio -> Temperatura -> Estabilidade -> Comunicação -> Energia```

Dependendo se for 'Crítico' ou 'Em Atenção' a solução relacionada muda. 

### Relatório final

Após análisar os 6 ciclos, mostrando toda informação acima cada vez, o programa vai para o estágio do relatório final. No relatório, ele mostra várias informações:

- Média de todos os dados de dados_missao durante os 6 ciclos
- Qual ciclo teve o score maior
- Quanto esse score foi
- O score médio de todos ciclos
- Se a missão teve uma tendência para piora ou melhorar
- A pontuação de risco acumulada para todos dados
- Qual área foi mais afetada de todos dados
- A classificação final da missão dependendo da média do score

### Exemplo do output:

```
============================================================
MISSION CONTROL AI
============================================================
Missão: Erebus Test Alpha
Equipe: Equipe Nyx
Quantidade de ciclos analisados: 6
============================================================

CICLO 1
------------------------------------------------------------
Temperatura (22°C) | NORMAL | Temperatura estável
Comunicação (95%) | NORMAL | Comunicação estável
Energia (91%) | NORMAL | Energia estável
Oxigenio (97%) | NORMAL | Oxigênio adequado
Estabilidade (92%) | NORMAL | Estabilidade operacional adequada

Pontuação de risco do Ciclo: 0
Classificação do Ciclo: MISSÃO ESTÁVEL
Manter operação normal e continuar monitoramento.

CICLO 2
------------------------------------------------------------
Temperatura (25°C) | NORMAL | Temperatura estável
Comunicação (83%) | NORMAL | Comunicação estável
Energia (70%) | NORMAL | Energia estável
Oxigenio (93%) | NORMAL | Oxigênio adequado
Estabilidade (85%) | NORMAL | Estabilidade operacional adequada

Pontuação de risco do Ciclo: 0
Classificação do Ciclo: MISSÃO ESTÁVEL
Manter operação normal e continuar monitoramento.

CICLO 3
------------------------------------------------------------
Temperatura (29°C) | NORMAL | Temperatura estável
Comunicação (35%) | ATENÇÃO | Comunicação instável
Energia (63%) | NORMAL | Energia estável
Oxigenio (91%) | NORMAL | Oxigênio adequado
Estabilidade (71%) | NORMAL | Estabilidade operacional adequada

Pontuação de risco do Ciclo: 1
Classificação do Ciclo: MISSÃO ESTÁVEL
[COMUNICAÇÃO EM ATENÇÃO]: Tentar restabelecer contato com a base.

CICLO 4
------------------------------------------------------------
Temperatura (34°C) | ATENÇÃO | Temperatura elevada
Comunicação (42%) | ATENÇÃO | Comunicação instável
Energia (31%) | ATENÇÃO | Bateria abaixo do recomendado
Oxigenio (83%) | ATENÇÃO | Oxigênio abaixo do ideal
Estabilidade (53%) | ATENÇÃO | Estabilidade operacional reduzida

Pontuação de risco do Ciclo: 5
Classificação do Ciclo: MISSÃO EM ATENÇÃO
[OXIGÊNIO EM ATENÇÃO]: Monitores de O2 em alerta. Verificar taxa de fluxo.

CICLO 5
------------------------------------------------------------
Temperatura (40°C) | CRÍTICO | Risco de superaquecimento
Comunicação (24%) | CRÍTICO | Comunicação com base em nível crítico
Energia (18%) | CRÍTICO | Bateria em nível crítico
Oxigenio (74%) | CRÍTICO | Oxigênio em nível crítico
Estabilidade (32%) | CRÍTICO | Estabilidade operacional crítica

Pontuação de risco do Ciclo: 10
Classificação do Ciclo: MISSÃO CRÍTICA
[OXIGÊNIO CRÍTICO]: Acionar protocolo de suporte à vida.

CICLO 6
------------------------------------------------------------
Temperatura (32°C) | ATENÇÃO | Temperatura elevada
Comunicação (53%) | ATENÇÃO | Comunicação instável
Energia (31%) | ATENÇÃO | Bateria abaixo do recomendado
Oxigenio (84%) | ATENÇÃO | Oxigênio abaixo do ideal
Estabilidade (51%) | ATENÇÃO | Estabilidade operacional reduzida

Pontuação de risco do Ciclo: 5
Classificação do Ciclo: MISSÃO EM ATENÇÃO
[OXIGÊNIO EM ATENÇÃO]: Monitores de O2 em alerta. Verificar taxa de fluxo.

============================================================
RELATÓRIO FINAL DA MISSÃO
============================================================
Missão: Erebus Test Alpha
Equipe: Equipe Nyx

Quantidade de ciclos analisados: 6

Média de temperatura: 30.33 °C
Média de comunicação: 55.33%
Media de bateria: 50.67%
Média de oxigênio: 87.0%
Média de estabilidade: 64.0%

Ciclo mais crítico: Ciclo 5
Maior pontuação de risco: 10
Risco médio da missão: 3.5
Quantidade de ciclos criticos: 1

Tendencia da missão:
A missão apresentou tendência de piora.

Pontuação acumulada por área:
Temperatura interna: 4 pontos
Comunicação com a base: 5 pontos
Sistema de energia: 4 pontos
Suporte de oxigênio: 4 pontos
Estabilidade operacional: 4 pontos

Area mais afetada:
Comunicação com a base

Classificação final da missão:
MISSÃO EM ATENÇÃO
```
