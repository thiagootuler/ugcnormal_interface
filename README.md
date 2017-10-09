# ugcnormal_interface
Uma interface remota para utilização do normalizador de UGC (user-generated content) chamado [UGCNorm@l](https://github.com/avanco/UGCNormal).

## Requisitos
* beautifulsoup4: 4.4.1
* requests: 2.9.1
* python: 2.7

## Instalação
Baixe o módulo [ugcnormal.py](https://github.com/thiagootuler/ugcnormal_interface/blob/master/ugcnormal.py)

## Utilização
O arquivo `exemplouso.py` possui alguns exemplos de uso. Ex.:
```
>> from ugcnormal import Normalizador
>> normalidador = Normalizador()
>> texto = "no ultimo fds fiz uma conpra pela net de um smartfone"
>> resultado = normalidador.recebe_texto(6, 1, texto)
>> print resultado
```
