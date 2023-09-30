# Dashboard com Dash e Dash Mantine Components

Este é um projeto de exemplo que demonstra como criar um painel interativo usando a biblioteca Dash e componentes do Dash Mantine Components. O painel exibe um gráfico interativo com dados do Gapminder e permite aos usuários escolher entre diferentes métricas (população, expectativa de vida e PIB per capita).

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter as seguintes bibliotecas instaladas:

- Python 3.x
- Dash
- Dash Mantine Components
- Plotly Express
- Dash Iconify (opcional)

Você pode instalar as dependências executando o seguinte comando:

```bash 
pip install -r requirements.txt 
```

## Configurando o Ambiente Virtual (Opcional)
Recomendamos o uso de um ambiente virtual para isolar as dependências do projeto. Siga estas etapas para configurar e ativar um ambiente virtual:

Crie um ambiente virtual (substitua myenv pelo nome de sua escolha):

```bash 
python3 -m venv dash_env
```
Ative o ambiente virtual (Windows):

```bash 
dash_env\Scripts\activate
```
Ative o ambiente virtual (Linux/macOS):

```bash 
source dash_env/bin/activate
```
Executando o Projeto
Para iniciar o aplicativo, execute o seguinte comando no terminal:

```bash 
python app.py
```

Isso iniciará o servidor de desenvolvimento e você poderá acessar o painel no seu navegador em http://localhost:8050.

Encerrando o Ambiente Virtual
Quando você terminar de usar o projeto, pode encerrar o ambiente virtual. Execute o seguinte comando no terminal:
```bash 
deactivate
```
Isso desativará o ambiente virtual e retornará ao ambiente padrão do Python.

## Uso
O painel exibe um gráfico interativo no lado direito e um seletor de métricas no lado esquerdo. Você pode escolher entre "pop", "lifeExp" e "gdpPercap" para visualizar diferentes métricas no gráfico.

## Estrutura do Projeto
- `app.py`: O arquivo principal que inicializa o aplicativo Dash.
- `layout.py`: Define o layout do aplicativo, incluindo os componentes da interface do usuário.
- `callbacks.py`: Define os callbacks que controlam a lógica do aplicativo.
- `requirements.txt`: Lista as dependências do projeto.

## Contribuindo
Sinta-se à vontade para contribuir para este projeto enviando problemas ou solicitações de pull. Estamos abertos a melhorias e feedback.
