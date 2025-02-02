# PDCA NL Project

Este é o projeto PDCA NL, desenvolvido para processar e analisar dados de planilhas usando Python. O projeto inclui scripts para preprocessamento de dados, treinamento de modelos e visualização de resultados.

## Estrutura do Projeto

```plaintext
G:\Meu Drive\Programação\PDCA_NL\PDCA_NL_Project
│
├── data
│   └── raw
│       └── planilhas
├── notebooks
├── src
│   ├── data_preprocessing
│   ├── models
│   └── visualization
├── tests
└── docs

data: Contém os dados do projeto.
raw: Armazena dados brutos, como planilhas.
notebooks: Contém Jupyter Notebooks para exploração e análise de dados.
src: Contém o código-fonte do projeto.
data_preprocessing: Scripts para limpeza e preparação dos dados.
models: Scripts para definição e treinamento dos modelos.
visualization: Scripts para visualização de dados e resultados.
tests: Contém testes automatizados.
docs: Documentação do projeto.
Requisitos
Python 3.9 ou superior
Instalação
Clone o repositório para o seu diretório local:

sh
git clone https://github.com/seu_usuario/PDCA_NL_Project.git
cd PDCA_NL_Project
Crie e ative um ambiente virtual:

sh
python -m venv venv
venv\Scripts\activate
Instale as dependências:

sh
pip install -r requirements.txt
Configuração do Ambiente
Certifique-se de que todas as bibliotecas necessárias estão instaladas no ambiente virtual. Aqui estão algumas das principais bibliotecas usadas neste projeto:

pandas
numpy
scikit-learn
matplotlib
seaborn
openpyxl
Executando os Testes
Para executar os testes unitários, use o comando:

sh
python -m unittest discover -s tests
Uso
Carregar e Preprocessar Dados
O arquivo principal do projeto (main.py) contém funções para carregar e preprocessar dados.

Python
import pandas as pd

def load_data(file_path):
    return pd.read_excel(file_path)

def main():
    data_path = 'G:\\Meu Drive\\Programação\\PDCA_NL\\1_Excel\\PDCA_Logic_Demandas.xlsx'
    df = load_data(data_path)
    print(df.head())

if __name__ == "__main__":
    main()
Scripts de Preprocessamento
Os scripts de preprocessamento estão localizados em src/data_preprocessing/preprocess.py. Aqui está um exemplo de como preprocessar os dados:

Python
import pandas as pd

def preprocess_data(df):
    # Convertendo colunas float64 para string antes de preencher valores nulos
    for column in df.select_dtypes(include=['float64']).columns:
        df[column] = df[column].astype(str)
    df.fillna('', inplace=True)
    return df
Contribuição
Sinta-se à vontade para contribuir com melhorias para o projeto. Por favor, envie um pull request com uma descrição clara do que foi adicionado ou modificado.

Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

Code
### Passos para adicionar o README ao GitHub:

1. **Crie o arquivo `README.md` no diretório raiz do seu projeto:**
   ```sh
   cd "G:\Meu Drive\Programação\PDCA_NL\PDCA_NL_Project"
   echo "# PDCA NL Project" > README.md
Abra o arquivo README.md no seu editor de texto favorito (como o VS Code) e copie o conteúdo acima para o arquivo.

Adicione, commit e faça o push do arquivo para o repositório remoto:

sh
git add README.md
git commit -m "Add README documentation"
git push origin master
Seguindo esses passos, você terá um README.md bem estruturado e informativo no seu repositório GitHub. Se precisar de mais alguma coisa ou tiver outras dúvidas, sinta-se à vontade para perguntar!
