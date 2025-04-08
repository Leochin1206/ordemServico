import pandas as pd
from django.core.wsgi import get_wsgi_application
import os

# Configurar o ambiente Django para rodar scripts fora do manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
application = get_wsgi_application()

from api.models import Responsaveis, Gestores  # Importe seus models

def importar_responsaveis():
    """
    Lê os dados do arquivo RESPONSÁVEIS AMBIENTES 2024.xlsm,
    usando a segunda linha como cabeçalho,
    cria instâncias do model Responsaveis e as salva no banco de dados.
    """
    print(f"Diretório de trabalho atual: {os.getcwd()}")
    try:
        df = pd.read_excel('RESPONSÁVEIS AMBIENTES 2024.xlsm', header=1)  # Usar a segunda linha como cabeçalho

        for index, row in df.iterrows():
            nome_responsavel = row['Responsável pelo ambiente']
            ni = int(row['NI'])  # Garante que NI seja um inteiro

            # Criar o email com o padrão nome + @senai.com.br
            email = nome_responsavel.lower().replace(' ', '') + '@senai.com.br'

            # Tentar encontrar o gestor pelo nome (assumindo que a tabela Gestores já está populada)
            gestor_nome = row['Gestor do ambiente']
            gestor = None  # Inicializa gestor como None
            if pd.notna(gestor_nome):  # Verifica se o valor não é NaN
                try:
                    gestor = Gestores.objects.get(nome=gestor_nome)
                except Gestores.DoesNotExist:
                    print(f"Aviso: Gestor '{gestor_nome}' não encontrado. Definindo como None para {nome_responsavel}.")

            # Criar e salvar o objeto Responsaveis
            responsavel = Responsaveis(nome=nome_responsavel, email=email, ni=ni, gestor=gestor)
            responsavel.save()

        print("Dados de Responsáveis importados com sucesso!")

    except FileNotFoundError:
        print("Erro: O arquivo RESPONSÁVEIS AMBIENTES 2024.xlsm não foi encontrado na raiz da pasta back.")
    except ValueError as ve:
        print(f"Erro de valor ao processar os dados: {ve}. Verifique os tipos de dados na planilha.")
    except KeyError as ke:
        print(f"Erro de chave ao acessar a coluna: {ke}. Verifique os nomes das colunas na planilha (lembre-se que os cabeçalhos estão na segunda linha).")
    except Exception as e:
        print(f"Ocorreu um erro durante a importação: {e}")

if __name__ == '__main__':
    importar_responsaveis()