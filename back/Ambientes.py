import os
import django
import sys
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__))) 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  

django.setup()

from api.models import Ambientes, Responsaveis

df = pd.read_excel('Ambientes.xlsx')

for _, row in df.iterrows():
    nome_resp = str(row['responsavel']).strip().upper()

    responsavel = Responsaveis.objects.filter(nome__iexact=nome_resp).first()

    if not responsavel:
        print(f"Responsável '{nome_resp}' não encontrado.")
        continue

    try:
        ambiente = Ambientes.objects.create(
            sig=int(str(row['sig']).replace(",", "").replace(".", "")),
            descricao=row['descricao'],
            ni=int(''.join(filter(str.isdigit, str(row['ni'])))),
            responsavel=responsavel
        )
        print(f"Ambiente criado: {ambiente.descricao}")
    except Exception as e:
        print(f"Erro ao criar ambiente '{row['descricao']}': {e}")
