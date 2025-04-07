import json
import os
import django
from api.models import Patrimonios

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

json_path = os.path.join(os.path.dirname(__file__), 'dados.json')

with open(json_path, 'r', encoding='utf-8') as file:
    dados = json.load(file)

for item in dados:
    try:
        localizacao = int(item['localizacao'])
        ni = int(item['ni']) if item['ni'] is not None else 0  
        descricao = item['descricao']

        Patrimonios.objects.create(
            localizacao=localizacao,
            ni=ni,
            descricao=descricao
        )
    except Exception as e:
        print(f"Erro ao importar item: {item} - Erro: {e}")
