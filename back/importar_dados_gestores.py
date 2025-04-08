import os
import django
import pandas as pd

# Configura o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import Gestores

# Caminho absoluto baseado na localização do script
caminho_excel = os.path.join(os.path.dirname(__file__), "Gestores.xlsx")

# Lê os dados do Excel
df = pd.read_excel(caminho_excel)

# Percorre cada linha do DataFrame e cria um objeto Gestores
for _, row in df.iterrows():
    Gestores.objects.create(
        nome=row['nome'],
        ni=int(row['ni']),
        cargo=row['cargo'],
        area=row['area']
    )

print("Importação concluída com sucesso.")
