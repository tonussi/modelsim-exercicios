# Modelagem e Simulação Lib
>Mini Pacote para Modelagem e Simulação em Python

Trabalho para INE5425-06208 (20171) - Modelagem e Simulação

# Autor

Lucas Tonussi [Python GIS Programmer & R&D at agrosatelite.com.br] - @[lpton](twitter.com/lpton).

# Execução

Para executar você precisa ter Python 2.7+ na sua máquina.
É preciso também instalar as bibliotecas numpy, matplotlib.

## Windows

1. Instalar https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tar.xz (Python 2.7)
+ Instalar get-pip.py (https://bootstrap.pypa.io/get-pip.py)
    + Para instalar o get-pip você precisa através acessar seu terminal
    + No windows você acessar através do Power Shell, depois vá até o diretório onde você baixou o get-pip.py
    + Instale o get-pip.py usando o comando python get-pip.py
+ Agora você precisa colocar o Python e o Scripts do Python no PATH do Windows.
+ ![Python Path no Windows](http://pythonbrasil.github.io/wiki/images/instalacao-windows/add-python-to-path.png)
+ Abra o painel de controle e navegue até as configurações de sistema
+ Selecione as configurações avançadas do sistema
+ Clique em variáveis de ambiente
+ Procure nas variáveis do sistema pela variável Path
+ Clique em editar
+ Verifique se os valores `C:\Python27` e `C:\Python27\Scripts` existem no campo de valor da variável, caso não exista adicione ao final dos valores separando cada valor com ;. O Python34 neste exemplo é referente a pasta onde o python foi instalado no seu sistema, este valor pode ser diferente caso esteja instalando outra versão do python por exemplo se for a versão 2.7 o valor será Python27. Verifique o destino da sua instalação e subistitua por este valor.
+ Clique em OK
+ Agora que você já configurou o PATH faça
+ pip install numpy
+ pip install scipy
+ pip install simpy
+ pip install matplotlib
+ Vídeo ensinando a instalar numpy, scipy, e matplotlib no Windows (https://www.youtube.com/watch?v=-llHYUMH9Dg).

## Linux / Ubuntu

1. sudo apt install python
+ sudo apt install python-pip
+ sudo pip install numpy
+ sudo pip install scipy
+ sudo pip install simpy
+ sudo pip install matplotlib
+ Pronto tudo já configurado.

# Libs Pages

1. Simpy https://simpy.readthedocs.org/en/latest/index.html
+ Scipy http://www.scipy.org
+ Numpy http://www.numpy.org
+ Matplotlib http://matplotlib.org/
