# Usando ugcnormal localmente
Neste diretório encontra-se os arquivos necessarios para levantar um servidor de serviços para fornecer as funcionalidades do normalizador UGCNorm@l localmente.

## Requisitos
* Flask: 0.12.2
* Flask-RESTful: 0.3.6
* requests: 2.18.4
* python: 2.7


## Instalação
Para utilizar este normalidador localmente, deve-se obter seu código fonte no [repositório oficial](https://github.com/avanco/UGCNormal) e executar o script `./configure.sh` para instalar suas dependências.
Em seguida, baixe o [api_server.py](https://github.com/thiagootuler/ugcnormal_interface/blob/master/local_webservice/api_server.py), instale as dependencias solicitadas no tópico anterior e execute-o por meio do seguinte comando.
```
$ python api_server.py
```

## Utilização
Nesta versão implementada, cada uma das etapas do processo de normalização pode ser solicitada separadamente, contudo, esta executará as etapas anteriores para satizfazer suas exigências.
No arquivo `exemplo_uso.py` possui um exemplo de solicitação de serviços. Ex.:
```
>> #!/usr/bin/python
>> # -*- coding: utf-8 -*-
>> import requests
>> root_url = 'http://127.0.0.1:5000'
>> action_url = root_url + '/proper_noun'
>> headers = {'content-type': 'application/json'}
>> data = u'{"text": "no último fds fiz uma conpra pela net de um smartfone da microsoft e uma tv da lg. jah to usando o cel :) eh incrivel a tecnologia dele: tem wifi, blutoth, etc....."}'
>> response = requests.post(action_url, headers=headers, data=data.encode('utf-8'))
>> print response.texto
```
