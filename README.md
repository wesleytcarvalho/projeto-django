<h1 align="center"> Projeto API em DJANGO </h1>

Para que possamos seguir no mesmo caminho, siga os passos abaixo!

Primeiro: você precisa saber que vamos trabalhar com ambiente virtual chamado VENV<br>
Segundo: você já precisa ter baixo o projeto em sua máquina.<br>
Terceiro: você já tenha que está com o venv instalado em sua máquina, senão estiver use link abaixo.<br>
https://stackoverflow.com/questions/49470367/install-virtualenv-and-virtualenvwrapper-on-macos<br>

## Acesse o projeto
```
cd projeto_django
``` 

## Criando projeto com o VENV
``` 
python3 -m venv .venv 
```

## Ativando o ambiente virtual
``` 
source .venv/bin/activate
```

Agora vamos instalar algumas coisas
```
pip install -r requeriments.txt
```

Agora acesse o diretorio ```meu_projeto```

Voce vai precisar criar as tabelas do banco entao use o comando abaixo
```
python manage.py migrate
python manage.py makemigrations meu_app

```

Execute o comando abaixo. 
```
python manage.py runserver
```
### NOTA: agora digite no seu navegador http://127.0.0.1:8000

Agora vamos abrir um outro terminal e rodar o comando abaixo
```
cd projeto_django
source .venv/bin/activate
```

## Testando nossa API
Digite seu nome onde está esta chaves {Seu nome aqui} que está no comando curl abaixo
```
curl -X POST -H "Content-Type: application/json" -d '{"titulo": "Meu Post", "conteudo": "Meu nome é {Seu nome aqui} e o seu?"}' http://localhost:8000/api/posts/
```

Agora veja seu navegador se precisar dê um f5 para atualizar a página.

## Visualizando conteúdo via curl
```
curl -X GET http://localhost:8000/api/posts/ | jq .
```