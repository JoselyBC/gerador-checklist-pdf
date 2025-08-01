# Gerador de Checklist de Instrutores

Aplicação desktop simples para criar listas de presença em PDF de forma rápida e interativa.

![Interface do Programa](https://storage.googleapis.com/generativeai-assets/user-provided-content/images/Gerador_de_Checklist_de_Instrutores.png)

## 🚀 Tecnologias Utilizadas

*   **Python 3:** Linguagem principal do projeto.
*   **Tkinter:** Biblioteca padrão do Python para a criação da interface gráfica (GUI).
*   **ReportLab:** Biblioteca para a criação e manipulação de arquivos PDF.
*   **PyInstaller:** Ferramenta para empacotar a aplicação em um único arquivo executável (`.exe`).

## 🎯 O que o projeto faz?

Este programa oferece uma solução prática para a geração de listas de presença. Suas principais funcionalidades são:

*   **Gerar PDFs:** Cria um arquivo PDF profissional no formato A4 com uma lista de turmas.
*   **Checkboxes Interativos:** O PDF gerado contém checkboxes que podem ser marcados digitalmente, facilitando o controle de presença.
*   **Interface Gráfica Intuitiva:** Permite que o usuário visualize a lista de turmas.
*   **Gerenciamento em Tempo Real:** O usuário pode **adicionar** e **remover** turmas da lista diretamente pela interface antes de gerar o documento final.

## ⚙️ Como Rodar o Projeto

Existem duas maneiras de rodar o projeto, dependendo do seu objetivo.

### Para o Usuário Final (Uso Direto)

Esta é a forma mais simples, para quem apenas precisa usar o programa sem se preocupar com código.

1.  Baixe o arquivo `gerarpdf.exe`.
2.  Coloque o arquivo em uma pasta de sua preferência (Ex: `C:\Users\SeuNome\Documentos\Checklists`). **O PDF gerado será salvo nesta mesma pasta**.
3.  Dê um duplo-clique no arquivo `gerarpdf.exe` para iniciar o programa.

**Não é necessário instalar nada!**

### Para Desenvolvedores (Modificar ou Recriar)

Se você deseja alterar o código-fonte, adicionar turmas permanentemente ou recriar o executável.

1.  **Pré-requisitos:** Certifique-se de ter o [Python 3](https://www.python.org/) instalado em sua máquina.

2.  **Clone ou baixe** este projeto para o seu computador.

3.  **Crie e ative um ambiente virtual** (recomendado):
    ```bash
    # Cria o ambiente
    python -m venv venv

    # Ativa o ambiente no Windows
    .\venv\Scripts\activate

    # Ativa o ambiente no Linux/macOS
    source venv/bin/activate
    ```

4.  **Instale as dependências** necessárias:
    ```bash
    pip install reportlab pyinstaller
    ```

5.  **Para rodar a aplicação em modo de desenvolvimento:**
    ```bash
    python gerarpdf.py
    ```

6.  **Para gerar um novo arquivo executável:**
    ```bash
    pyinstaller --onefile --windowed gerarpdf.py
    ```
    *   `--onefile`: Agrupa tudo em um único arquivo `.exe`.
    *   `--windowed`: Impede que a janela de console (terminal) abra junto com o programa.
    *   O novo executável estará na pasta `dist` que será criada.

## 🧑‍💻 Autora

Projeto desenvolvido por **Josely Castro**.