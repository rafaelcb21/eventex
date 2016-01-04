# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/rafaelcb21/eventex.svg?branch=master)](https://travis-ci.org/rafaelcb21/eventex)
[![Code Climate](https://codeclimate.com/repos/568a6f67c569b51ab800036e/badges/c75157150dc1aabdb14e/gpa.svg)](https://codeclimate.com/repos/568a6f67c569b51ab800036e/feed)
## Como desenvolver?

1. Clone o reposit�rio.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as depend�ncias.
5. Configure a inst�ncia com o .env
6. Execute os testes.

```console
git clone git@github.com:rafaelcb21/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma inst�ncia no heroku.
2. Envie as configura��es para o heroku.
3. Defina uma SECRET_KEY segura para inst�ncia.
4. Defina DEBUG=False
5. Configure o servidor de email.
6. Envie o codigo para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```