# runner de escritório do Mestre Ruan

1. Crie um ambiente virtual:
```bash
python3 -m venv venv
```
2. Ative o ambiente virtual:
```bash
source ./venv/bin/activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Execute o script com os argumentos:
```bash
python main.py --secret=blabla --adm-id=123456 --pc-host=blabla --exp-days=30
```
5. O script irá imprimir o token no console
