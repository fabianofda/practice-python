# Practice Python Project

Este repositório contém um projeto básico de automação de testes usando Python, Selenium e Pytest. A estrutura é organizada para facilitar a manutenção de testes de diferentes páginas, com arquivos dedicados para testes e páginas específicas.

## Estrutura do Projeto

practice-python │ ├── page │ ├── login_page.py # Elementos e ações da página de login │ ├── my_account_page.py # Elementos e ações da página da conta do usuário │ └── shop_page.py # Elementos e ações da página de compras │ ├── tests │ ├── init.py # Configuração do path para facilitar imports │ ├── base_test.py # Base para testes │ ├── login_test.py # Testes de login │ └── shop_test.py # Testes de funcionalidades da loja │ ├── .env # Variáveis de ambiente (ignorado pelo Git) ├── .gitignore # Arquivos e diretórios ignorados pelo Git └── requirements.txt # Dependências do projeto


## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- Um navegador suportado (ex: Chrome, Firefox)

## Instalação

1. Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/practice-python.git

## Navegue até o diretório do projeto:

> cd practice-python

## Instale as dependências necessárias:

> pip install -r requirements.txt

## Executando os Testes

> pytest tests/

Ou rodar testes específicos, como os de login:

> pytest tests/login_test.py

## Tecnologias Utilizadas
- *Python*: Linguagem de programação principal
- *Selenium*: Ferramenta de automação de navegadores
- *Pytest*: Framework de testes
- *Faker*: Gerador de dados fictícios para testes

## Licença
- **Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.**

### O que incluir no README:
- **Introdução**: O que é o projeto.
- **Estrutura**: Explicação da estrutura do projeto e onde cada parte está localizada.
- **Pré-requisitos**: O que o usuário precisa instalar antes de rodar o projeto.
- **Instalação**: Passos para configurar o projeto localmente.
- **Execução dos testes**: Como rodar os testes.
- **GitHub Actions**: Descrição da pipeline CI/CD.
- **Tecnologias**: As principais tecnologias usadas no projeto.
- **Contribuição**: Como contribuir.
- **Licença**: A licença do projeto, se aplicável.
