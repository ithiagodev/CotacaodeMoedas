## Cotações de Moedas

Aplicação em Python que exibe as cotações de moedas como Dólar, Euro e Bitcoin em tempo real, com atualização a cada 30 segundos. As cotações são obtidas a partir de uma API pública e exibidas de maneira interativa em uma interface gráfica usando o Tkinter. Além disso, a data e hora são atualizadas a cada segundo e exibidas no canto inferior direito da janela.

## API UTILIZADA
https://docs.awesomeapi.com.br/api-de-moedas

## Requisitos
Este projeto é desenvolvido inteiramente em Python. Certifique-se de que a versão do Python em sua máquina seja compatível com o código utilizado.

### Instalação de dependências (se necessário):
Instale as dependências executando:
```bash
pip install requests
```

**Obs:** Este projeto depende da biblioteca `requests` para fazer requisições HTTP à API que fornece as cotações das moedas.

## Estrutura dos Arquivos
1. **Main Script (ex.: `index.py`)**: Arquivo principal que executa a aplicação e contém as funcionalidades de atualização das cotações e do horário.
2. **Funções Principais**:
   - **Obter Cotações**: Faz uma requisição à API pública para obter as cotações mais recentes do Dólar, Euro e Bitcoin.
   - **Exibição das Cotações**: Exibe as cotações das moedas em um formato amigável, com as cotações em tempo real.
3. **Interface Gráfica**:
   - Usando a biblioteca `Tkinter`, a interface exibe as cotações das moedas e a hora atual em tempo real.
   - O layout é simples e bem estruturado para facilitar a leitura.

## Como Executar
Certifique-se de ter o Python instalado na sua máquina e a biblioteca `requests` instalada.

No terminal, execute:
```bash
python index.py
```
A interface gráfica será exibida, mostrando as cotações das moedas e a hora atual. As cotações são atualizadas automaticamente a cada 30 segundos.

## Funcionalidades
1. **Exibição das Cotações**: Mostra a cotação do Dólar, Euro e Bitcoin em tempo real.
2. **Atualização Automática**: As cotações são atualizadas a cada 30 segundos.
3. **Interface Gráfica**: Exibe as informações de maneira clara e interativa usando o Tkinter.
4. **Layout Personalizável**: A interface tem um fundo escuro e fontes personalizadas para facilitar a leitura.

## Fluxo de Funcionamento
1. **Requisição de Cotações**: Ao iniciar, o programa faz uma requisição para a API e obtém as cotações do Dólar, Euro e Bitcoin.
2. **Exibição e Atualização**: As cotações e a hora são exibidas na interface gráfica e atualizadas conforme o tempo passa.
3. **Atualizações em Tempo Real**: As cotações são atualizadas a cada 30 segundos, garantindo que as informações sejam sempre precisas e atualizadas.