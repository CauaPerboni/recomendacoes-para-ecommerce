# Recomendações Personalizadas para E-commerce com IA

Este projeto implementa um sistema de recomendações personalizadas para e-commerce, com foco em otimizar a experiência de usuários ao sugerir produtos relevantes. Utilizando técnicas de filtragem colaborativa, a aplicação é capaz de sugerir produtos com base nas interações anteriores de usuários.

## Funcionalidades

- Geração de recomendações de produtos personalizados para cada usuário.
- Interface gráfica desenvolvida com PyQt5 para interação intuitiva.
- Suporte a diferentes datasets de interações de usuários.
- Otimização de memória e performance com o uso de matrizes esparsas.

## Tecnologias e Bibliotecas Utilizadas

- **Python 3.12.6** - Linguagem de programação.
- **PyQt5** - Interface gráfica do usuário (GUI).
- **Pandas** - Manipulação e análise de dados.
- **Scipy** - Manipulação de matrizes esparsas.
- **Numpy** - Cálculos e operações numéricas.
- **Dataset Retail Rocket** - Dados de exemplo de um e-commerce para simular interações e recomendações.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt

3. Adicione o dataset Retail Rocket na pasta retailrocket com o nome retailrocket.csv.

## Como usar

1. Execute a aplicação a partir do interface.py:
    ```bash
    python interface.py

2. Digite um User ID válido e clique em "Get Recommendations" para receber sugestões de produtos.

3. Nota: Certifique-se de inserir um User ID presente no dataset para que as recomendações sejam geradas corretamente. Consulte os primeiros IDs com print(df['visitorid'].head()) para validar.

## Principais Funções

- create_interaction_matrix: Gera uma matriz de interações esparsas a partir do dataset.
- train_model: Treina o modelo de recomendações baseado na decomposição de matrizes.
- get_recommendations: Busca e exibe as recomendações personalizadas para um determinado User ID.

## Exemplo de DATASET
*Para garantir o funcionamento, o dataset deve conter as seguintes colunas*:

- visitorid: Identificação única do usuário.
- itemid: Identificação única do produto.
- event: Ação realizada pelo usuário (ex.: clique, compra).

