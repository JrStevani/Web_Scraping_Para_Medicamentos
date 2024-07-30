import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


def captura_de_dados(row, col):
    row_value = str(row[col])

    url = f'https://pro.consultaremedios.com.br/busca?termo={row_value}'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro na solicitação: {e}")
        return pd.Series({'Apresentação': '', 'Medicamento': '', 'Princípio ativo': '', 'Fabricante': ''})

    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find('div', {'data-react-class': 'SearchResults'})

    if div:
        data_react_props = div['data-react-props']

        data = json.loads(data_react_props)

        collection = data['collection']

        apresentacao = ''
        medicamento = ''
        principio_ativo = ''
        fabricante = ''

        for item in collection:
            apresentacao = str(f"{item['name']}")
            medicamento = str(f"{item['product_name']}")
            principio_ativo = str(f"{item['substance_name']}")
            fabricante = str(f"{item['factory_commercial_name']}")

        print(f"{row_value}: {apresentacao}, {medicamento}, {principio_ativo}, {fabricante}")

        return pd.Series({'Apresentação': apresentacao, 'Medicamento': medicamento,
                          'Princípio ativo': principio_ativo, 'Fabricante': fabricante})
    else:
        return pd.Series({'Apresentação': '', 'Medicamento': '',
                          'Princípio ativo': '', 'Fabricante': ''})


for c in range(1, 4):
    df = pd.read_excel('./tabelas.xlsx', sheet_name=f'EAN {c}')

    df_aplicado = df.apply(lambda x: captura_de_dados(x, f'EAN {c}'), axis=1)

    df = pd.concat([df, df_aplicado], axis=1)

    df.to_excel(f'./tabela-{c}.xlsx', sheet_name=f'EAN {c}', index=False)
