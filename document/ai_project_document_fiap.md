
<img src="../assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=30% height=30%>

# AI Project Document - Módulo 1 - FIAP

## ## Grupo 18

#### Nomes dos integrantes do grupo

- <a href="https://www.linkedin.com/in/liquuid">Fernando Henrique Rodrigues da Silva</a>

## Sumário

[1. Introdução](#c1)

[2. Visão Geral do Projeto](#c2)

[3. Desenvolvimento do Projeto](#c3)

[4. Resultados e Avaliações](#c4)

[5. Conclusões e Trabalhos Futuros](#c5)

[6. Referências](#c6)

[Anexos](#c7)

<br>

# <a name="c1"></a>1. Introdução

## 1.1. Escopo do Projeto

### 1.1.1. Contexto da Inteligência Artificial

A inteligência artificial (IA) está revolucionando o agronegócio ao otimizar processos produtivos, aumentar a eficiência e promover a sustentabilidade. Tecnologias de IA são aplicadas em áreas como monitoramento de culturas, gestão de solo e irrigação inteligente, permitindo a análise de grandes volumes de dados capturados por sensores, drones e imagens de satélite. Sistemas de aprendizado de máquina ajudam a prever condições climáticas, detectar pragas e doenças em estágios iniciais, além de recomendar ações corretivas, como a aplicação precisa de fertilizantes e pesticidas. Essas inovações ajudam os agricultores a tomar decisões mais informadas, reduzindo desperdícios e maximizando a produção, enquanto mitigam o impacto ambiental.

### 1.1.2. Descrição da Solução Desenvolvida


O projeto desenvolvido, envolve a criação de um sistema para a gestão de sensores usando SQLAlchemy, se conecta ao contexto de IA, principalmente nas áreas de automação, coleta de dados e tomada de decisões baseadas em dados. 

Sensores, como os que estamos gerenciando no banco de dados, são uma peça fundamental em projetos que utilizam IA, especialmente no contexto de IoT (Internet das Coisas). Eles capturam informações ambientais, como temperatura, umidade, pressão, localização (GPS), entre outros dados. Esses dados podem ser processados por algoritmos de IA para:

* Tomar decisões automáticas com base em condições detectadas.
* Alimentar modelos de aprendizado de máquina para prever eventos futuros (prever clima, por exemplo).
* Monitorar sistemas e detectar anomalias (como problemas em máquinas ou sistemas físicos).

O gerenciamento de sensores automatizado (via CLI ) facilita a administração de uma rede de dispositivos que coletam dados automaticamente. Esses dados podem ser integrados em uma infraestrutura de IA que faz processamento em tempo real. 

O armazenamento de dados de sensores pode alimentar sistemas de aprendizado de máquina, que utilizam esses dados para ajustar comportamentos de sistemas controlados por IA, como otimizar a performance de uma fábrica ou sistema agrícola.

# <a name="c2"></a>2. Visão Geral do Projeto

## 2.1. Objetivos do Projeto

Esse projeto visa automatizar a gestão da umidade de solo, aplicando quantidades precisas de água em determinados setores usando IOT.

## 2.2. Público-Alvo

O público alvo vai desde o pequeno produtor ao grande, com as mudanças climátias é sabido que o preço e a disponibilidade de água serão um problema futuro.

## 2.3. Metodologia

Usando uma rede de sensores de humidade e atuadores, controlados por microcontroladoras como arduino, um sistema na nuvem pode monitorar e enviar comandos em tempo real, garantindo que todos os setores da lavoura estarão com a umidade correta no solo. 

# <a name="c3"></a>3. Desenvolvimento do Projeto

## 3.1. Tecnologias Utilizadas

Esse primeiro passo usei python com as bibliotecas Click, para gerenciar a CLI do programa, e SQLAlchemy para interagir com banco de dados.

## 3.2. Modelagem e Algoritmos

No projeto que desenvolvemos, não utilizamos diretamente um modelo de inteligência artificial (IA). O foco principal foi na criação de um CRUD (Create, Read, Update, Delete) para gerenciar sensores e armazenar dados utilizando SQLAlchemy, que facilita a interação com o banco de dados.


## 3.3. Treinamento e Teste

Ainda não foi modelado uma IA para esse projeto.

# <a name="c4"></a>4. Resultados e Avaliações

## 4.1. Análise dos Resultados

Não existem dados a serem analisados

## 4.2. Feedback dos Usuários

Não existe feedback, o projeto não foi apresentado a nenhum cliente.

# <a name="c5"></a>5. Conclusões e Trabalhos Futuros

Futuramente ele pode ajudar na economia de água de determinadas lavouras, melhorando o solo e sua produtividade.

