#### Clique na imagem.
[![Funcionalidades Htkbot-v1](htkbotimg.png)](https://www.youtube.com/watch?v=qSEuwE75lIA "Funcionalidades Htkbot-v1")



## HatakeBot
   <p> 
       Coleta informações sobre o covid19 atraves do site do governo. O bot realiza o scrapping do site coleta as informações e armazena em uma base de dados automaticamente. Ele também possui recursos de audio que informa qual operação esta sendo executada no momento. Como também possui funcionalidades para execução com cronograma. Isso mesmo, voce pode deixar ele executando de tempos em tempos. 
   </p>
* Using execute.py

## Table of content
- [Getting Started]
- [Requirements](
- [How to Build]
- [How to Run]

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Requirements

For building and running the application you need:

- Localize requeriments.txt 
- apply this comand pip3 install -r requeriments.txt

- Localize the archive install_dep_pygame.sh
- aplly ./install_dep_pygame.sh

- Localize the folder 'drives/firefox' and copy geckodriver
- apply copy geckodriver to /usr/local/bin

#### Environment Variables

- DATABASE_NAME=covid19_brasil
- DATABASE_HOST=localhost
- DATABASE_USER=postgres
- DATABASE_PASSWORD=admin
- DATABASE_PORT=5434
- PATH_SAVE_CSV=/home/osvaldoairon/
- PATH_BINARY_FIREFOX='usr/bin/firefox'
- SITE_EXAMPLE=https://covid.saude.gov.br



### How to Run

  * Help
         -> python3 execute.py --help

### Example helper

![Screenshot](htkbot.png 'Exemplo helper')
