# Lambda immo

Serverless API serving real estate price data

Works together with on https://github.com/slevin48/immo-search

`
!wget "https://raw.githubusercontent.com/slevin48/immo-search/main/data/75.csv?token=AC6XYQ73K4IWKQXRMV3ISA3ABXWXO"
`
## Test Flask

First activate the virtual env

`source env/bon/activate`

Then run flask in development mode (activate autoreload upon modification of `app.py`)

`export FLASK_APP=app.py` 

`export FLASK_ENV=development`

` flask run` 
 
## Zappa deploy

https://26yrburrn0.execute-api.eu-west-3.amazonaws.com/dev/dvf?code_commune=75114
