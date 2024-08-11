# Web_Scraping_Para_Medicamentos

<a href="">Projeto detalhado</a>

<strong>Descrição do Projeto: Captura e Análise de Dados de Medicamentos</strong>

Este projeto visa capturar e analisar dados de medicamentos a partir dos sites "Consulta Remédios" e "Farmaindex" utilizando Python. Através de uma combinação de web scraping com as bibliotecas <strong>`BeautifulSoup`</strong> e requisições HTTP com a biblioteca <strong>`requests`</strong>, os scripts buscam informações detalhadas sobre medicamentos com base em seus códigos EAN presentes em um arquivo Excel. 

<strong>Funcionalidades do Projeto:</strong>
- <strong>Leitura de Dados:</strong> Os scripts lêem os códigos EAN de medicamentos de uma planilha em um arquivo Excel.
- <strong>Web Scraping:</strong> Utilizam a biblioteca <strong>`BeautifulSoup`</strong> para extrair dados específicos dos sites "Consulta Remédios" e "Farmaindex" como apresentação, nome do medicamento, princípio ativo e fabricante.
- <strong>Tratamento de Dados:</strong> Os dados extraídos são organizados em um DataFrame do Pandas para fácil manipulação e análise.
- <strong>Exportação de Dados:</strong> Os resultados são salvos em novas planilhas Excel, permitindo uma análise estruturada e comparativa dos dados.

<strong>Etapas do Processo:</strong>
1. <strong>Requisição HTTP:</strong> Realiza uma solicitação GET para a URL do medicamento com base no código EAN.
2. <strong>Análise HTML:</strong> Utiliza <strong>`BeautifulSoup`</strong> para analisar o conteúdo HTML e encontrar as divs específicas contendo os dados necessários.
3. <strong>Extração de Dados:</strong> Decodifica o JSON contido nos atributos HTML (no caso do "Consulta Remédios") ou extrai diretamente os textos das tags HTML (no caso do "Farmaindex") para obter informações detalhadas sobre cada medicamento.
4. <strong>Organização dos Dados:</strong> Estrutura os dados extraídos em um DataFrame do Pandas e concatena com os dados originais.
5. <strong>Exportação:</strong> Salva o DataFrame resultante em um novo arquivo Excel para cada conjunto de códigos EAN processados.

<strong>Scripts Utilizados:</strong>
- <strong>Web_Scraping_Site_principal.py:</strong> Focado na captura de dados do site "Consulta Remédios".
- <strong>Web_scraping_site_Secundario.py:</strong> Complementa a captura de dados para medicamentos cujas descrições não foram obtidas do site principal, buscando informações no site "Farmaindex".

Este projeto demonstra utilização de:
- <strong>Web scraping e análise de dados com Python.</strong>
- <strong>Manipulação e processamento de dados com Pandas.</strong>
- <strong>Interação e integração de dados entre diferentes fontes e formatos.</strong>
  
O código fornece uma solução automatizada e eficiente para a coleta e análise de informações de medicamentos, potencializando a capacidade de obtenção de dados precisos e atualizados para diferentes aplicações na área da saúde e farmacêutica.