# C214 Lab Project

Este repositório é dedicado ao projeto desenvolvido para o laboratório da disciplina C214 - Engenharia de Software. O objetivo principal é fornecer uma aplicação que permite aos usuários gerenciar arquivos de forma eficiente, incluindo funcionalidades de upload, download e compartilhamento.

Equipe:

- Marcos Henrique Barbosa Pereira - Matrícula 1847 - <marcoshbp71@gmail.com>
- Pedro Augusto Barbosa Aparecido - Matrícula 170 - <pedr.augustobarbosa.aparecido@gmail.com>

## Funcionalidades

- **Upload de Arquivos**: Os usuários podem fazer upload de arquivos para a plataforma.
- **Download de Arquivos**: Permite que os usuários baixem arquivos previamente enviados.
- **Compartilhamento de Arquivos**: Os usuários podem compartilhar arquivos, definindo se o compartilhamento é público ou restrito a quem possui o link.
  - **Permissões de Acesso**: É possível definir permissões de editor e/ou visualizador para os arquivos compartilhados.
- **Autenticação de Usuário**: Funcionalidades de login e criação de conta para acesso seguro à aplicação.

## Requisitos Não Funcionais

- **Paginação**: A aplicação suporta paginação com limites de 10, 15 ou 20 itens por página.
- **Tecnologia**: Desenvolvida em Python utilizando o framework Flask, com uma arquitetura totalmente orientada a classes.
- **Documentação**: Utilização de GraphQL para a API, facilitando a consulta e manipulação de dados.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `c214_lab_project/`: Contém o código-fonte principal da aplicação.
- `tests/`: Inclui os testes automatizados para garantir a qualidade do código.
- `.github/`: Arquivos de configuração para integração contínua e outros fluxos de trabalho do GitHub.
- `docker-compose.yml`: Arquivo de configuração para orquestração de containers Docker.
- `pyproject.toml` e `poetry.lock`: Arquivos de configuração do Poetry para gerenciamento de dependências.

## 1. Configuração e Execução

Para configurar e executar a aplicação localmente:

**Clone o repositório**:
```bash
git clone https://github.com/MarcosHenriqueBarbosaPereira/C214-lab-project.git
cd C214-lab-project
```

## 2. Instalação do Poetry

O Poetry é uma ferramenta para gerenciamento de dependências e empacotamento em Python. Para instalá-lo, execute o seguinte comando no terminal:

```bash
pip install poetry
```

Este comando baixa e executa o instalador do Poetry. Para mais detalhes, consulte a [documentação oficial do Poetry](https://python-poetry.org/docs/).

## 3. Criação e Ativação do Ambiente Virtual

O Poetry cria automaticamente um ambiente virtual para o projeto ao instalar as dependências. Para ativar o ambiente virtual, utilize:

```bash
poetry shell
```

Para desativar o ambiente virtual, basta digitar `exit`.

## 4. Instalação de Dependências

Para instalar todas as dependências listadas no arquivo `pyproject.toml`, utilize:

```bash
poetry install
```


Seguindo esses passos, você terá um ambiente virtual configurado e gerenciado pelo Poetry, facilitando o desenvolvimento e a gestão de dependências em seus projetos Python. 
