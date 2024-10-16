# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# SoilControl

## Grupo 18

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/liquuid">Fernando Henrique Rodrigues da Silva</a>


## 👩‍🏫 Professores:

### Tutor(a) 
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a/">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>

## 📜 Descrição

*SoilControl* é um sistema de gerenciamento de solo, focado na aplicação precisa na quantida de de água, coletando informações de sensores e enviando para atuadores o tempo de abertura de água. 


## 📁 Estrutura de pastas

- <b>config</b>: Configurações.
- <b>src</b>: Aqui fica o código fonte do projeto. 


## 🔧 Como executar o código

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# altere o json em config/config.json
python src/soilcli.py # para receber a lista de comandos

# para gerar sensores aleatórios
python src/soilcli.py populate --quantidade 10 

# para adicionar um sensor
python src/soilcli.py create

# para remover um sensor
python src/soilcli.py delete

# para recolher os dados dos sensores, listando os ultimos valores do campo
python src/soilcli.py get-data

# para irrigar o setor, levando em conta as particularidades daquele solo, quantidade máxima de humidade suportada, mínima etc. Caso o valor esteja fora dos parâmetros configurados ele exibe um alerta.
python src/soilcli.py irrigar


```


## 🗃 Histórico de lançamentos

* 0.1.0 - 15/10/2024
    

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


