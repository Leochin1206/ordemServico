import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import Gestores

caminho_excel = os.path.join(os.path.dirname(__file__), "Gestores.xlsx")

df = pd.read_excel(caminho_excel)

for _, row in df.iterrows():
    Gestores.objects.create(
        nome=row['nome'],
        ni=int(row['ni']),
        cargo=row['cargo'],
        area=row['area'],
        is_superUser=True,
        is_staff=True
    )

print("Importação concluída com sucesso.")
