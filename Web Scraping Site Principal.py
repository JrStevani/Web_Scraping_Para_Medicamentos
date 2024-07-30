import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


def captura_de_dados(row, col):
    row_value = str(row[col])
    # URL que você deseja acessar
    url = f'https://pro.consultaremedios.com.br/busca?termo={row_value}'

    # Faça a solicitação GET para obter o conteúdo da página
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida
    except requests.RequestException as e:
        print(f"Erro na solicitação: {e}")
        return pd.Series({'Apresentação': '', 'Medicamento': '', 'Princípio ativo': '', 'Fabricante': ''})

    # Analise o conteúdo da página
    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find('div', {'data-react-class': 'SearchResults'})

    if div:
        # Extraia o conteúdo do atributo data-react-props
        data_react_props = div['data-react-props']

        # Decodifique o JSON contido no atributo data-react-props
        data = json.loads(data_react_props)

        # Acessar o dicionário decodificado
        collection = data['collection']

        # Inicialize as variáveis
        apresentacao = ''
        medicamento = ''
        principio_ativo = ''
        fabricante = ''

        # Exemplo de como acessar informações específicas
        for item in collection:
            apresentacao = str(f"{item['name']}")  # Apresentação
            medicamento = str(f"{item['product_name']}")  # Medicamento
            principio_ativo = str(f"{item['substance_name']}")  # Princípio ativo
            fabricante = str(f"{item['factory_commercial_name']}")  # Fabricante

        print(f"{row_value}: {apresentacao}, {medicamento}, {principio_ativo}, {fabricante}")

        return pd.Series({'Apresentação': apresentacao, 'Medicamento': medicamento,
                          'Princípio ativo': principio_ativo, 'Fabricante': fabricante})
    else:
        return pd.Series({'Apresentação': '', 'Medicamento': '',
                          'Princípio ativo': '', 'Fabricante': ''})


for c in range(1, 4):
    df = pd.read_excel('./tabelas.xlsx', sheet_name=f'EAN {c}')  # EAN 1

    # Aplique a função captura_de_dados a cada linha do DataFrame
    df_aplicado = df.apply(lambda x: captura_de_dados(x, f'EAN {c}'), axis=1)

    # Concatene os dados originais com os dados aplicados
    df = pd.concat([df, df_aplicado], axis=1)

    # Salve o DataFrame resultante em um novo arquivo .xlsx
    df.to_excel(f'./tabela-{c}.xlsx', sheet_name=f'EAN {c}', index=False)
