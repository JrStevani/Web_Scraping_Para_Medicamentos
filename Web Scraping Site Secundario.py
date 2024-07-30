import requests
from bs4 import BeautifulSoup
import pandas as pd


def captura_de_dados(row, col):
    row_value = str(row[col])

    url = f'https://farmaindex.com/busca?q={row_value}'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro na solicitação: {e}")
        return pd.Series({'Apresentação': '', 'Medicamento': '', 'Princípio ativo': '', 'Fabricante': ''})

    soup = BeautifulSoup(response.content, 'html.parser')

    apresentacao = ''
    medicamento = ''
    principio_ativo = ''
    fabricante = ''


    cards = soup.find_all('div', class_='MedicineCardstyles__DivBottomContent-sc-1wor19o-3 frzfOv')

    for card in cards:

        medicamento_info = card.find('div', class_='MedicineCardstyles__MedicineCardInfoWrap-sc-1wor19o-4 gwrazM')
        if medicamento_info:
            apresentacao = medicamento_info.find('h3').text.strip()
            medicamento = medicamento_info.find('strong').text.strip()

        fabricante_info = card.find('div', class_='MedicineCardstyles__PriceContainer-sc-1wor19o-5 gpNzXW')
        if fabricante_info:
            fabricante = fabricante_info.find('h4').text.strip()

        print(f"{row_value}: {apresentacao}, {medicamento}, {principio_ativo}, {fabricante}")
        break

    return pd.Series({'Apresentação': apresentacao, 'Medicamento': medicamento,
                      'Princípio ativo': principio_ativo, 'Fabricante': fabricante})


df = pd.read_excel('./gtins_nao_capturados.xlsx')

df_aplicado = df.apply(lambda x: captura_de_dados(x, f'EAN 4'), axis=1)

df = pd.concat([df, df_aplicado], axis=1)

df.to_excel(f'./tabela-4.xlsx', sheet_name=f'EAN 4', index=False)
