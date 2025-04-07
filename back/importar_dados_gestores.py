import os
import django
import pandas as pd

# Configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  # Ajuste o nome do seu projeto se for diferente
django.setup()

from api.models import Gestores

# Caminho do arquivo Excel
caminho_excel = 'Gestores.xlsx'

# Lê o Excel usando pandas
df = pd.read_excel(caminho_excel)

# Limpa a tabela antes de inserir (opcional)
Gestores.objects.all().delete()

# Itera sobre as linhas do DataFrame e salva no banco
for _, row in df.iterrows():
    Gestores.objects.create(
        nome=row['nome'],
        ni=int(str(row['ni']).replace(",", "").strip()),
        cargo=row['cargo'],
        area=row['area']
    )

print("Importação concluída com sucesso!")
