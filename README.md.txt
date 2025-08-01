📝 Gerador de Checklist de Instrutores
![alt text](https://img.shields.io/badge/Status-Ativo-brightgreen)
![alt text](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![alt text](https://img.shields.io/badge/License-MIT-green)
Uma ferramenta simples desenvolvida em Python com interface gráfica (Tkinter) para criar rapidamente listas de presença em PDF para instrutores. O programa permite visualizar, adicionar e remover turmas de uma lista antes de gerar um arquivo PDF profissional com checkboxes interativos.
<br>
![alt text](https://storage.googleapis.com/generativeai-assets/user-provided-content/images/Gerador_de_Checklist_de_Instrutores.png)
<br>
<details>
<summary><strong>Conteúdo</strong></summary>
<ol>
<li><a href="#-funcionalidades">Funcionalidades</a></li>
<li><a href="#-tecnologias-utilizadas">Tecnologias Utilizadas</a></li>
<li>
<a href="#rocket-guia-para-o-usuário-final">Guia para o Usuário Final</a>
<ul>
<li><a href="#como-baixar-e-usar">Como Baixar e Usar</a></li>
</ul>
</li>
<li>
<a href="#wrench-guia-para-desenvolvedores">Guia para Desenvolvedores</a>
<ul>
<li><a href="#pré-requisitos">Pré-requisitos</a></li>
<li><a href="#como-rodar-o-projeto">Como Rodar o Projeto</a></li>
<li><a href="#como-gerar-o-executável">Como Gerar o Executável</a></li>
<li><a href="#adicionar-turmas-permanentemente">Adicionar Turmas Permanentemente</a></li>
</ul>
</li>
<li><a href="#-licença">Licença</a></li>
</ol>
</details>
<br>
✨ Funcionalidades
Interface Gráfica Simples: Janela interativa para uma fácil utilização.
Geração de PDF: Cria arquivos PDF no formato A4 com cabeçalho e layout profissionais.
Checkboxes Interativos: O PDF gerado contém checkboxes que podem ser marcados digitalmente.
Gerenciamento de Turmas: Adicione ou remova turmas da lista em tempo real através da interface.
Executável Portátil: Pode ser compilado em um único arquivo .exe que não requer instalação de Python para rodar.
💻 Tecnologias Utilizadas
Python 3
Tkinter: Para a interface gráfica.
ReportLab: Para a geração dos arquivos PDF.
PyInstaller: Para a criação do arquivo executável.
🚀 Guia para o Usuário Final
Esta seção é para quem quer apenas usar o programa, sem se preocupar com código.
Como Baixar e Usar
Baixe o Programa: Vá para a seção de Releases deste repositório e baixe a versão mais recente do arquivo gerarpdf.exe.
Crie uma Pasta: Crie uma pasta em um local de fácil acesso (como a Área de Trabalho) e coloque o arquivo gerarpdf.exe dentro dela. Todos os PDFs serão salvos nesta mesma pasta.
Execute o Programa: Dê um duplo-clique no gerarpdf.exe.
Use as Funções:
Remover uma turma: Clique no nome da turma na lista e depois no botão Remover Selecionada.
Adicionar uma turma: Digite o nome no campo "Nova Turma" e clique em Adicionar.
Gerar o PDF: Quando a lista estiver pronta, clique no botão Gerar PDF com a Lista Acima.
Pronto! O arquivo PDF aparecerá na mesma pasta.
🔧 Guia para Desenvolvedores
Esta seção é para quem deseja modificar o código, estudar o projeto ou contribuir.
Pré-requisitos
Python 3.9+
Git
Como Rodar o Projeto
Clone o Repositório:
Generated bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
Use code with caution.
Bash
Crie e Ative um Ambiente Virtual (Recomendado):
Generated bash
# Criar ambiente
python -m venv venv

# Ativar no Windows
.\venv\Scripts\activate
Use code with caution.
Bash
Instale as Dependências:
Generated bash
pip install -r requirements.txt
```    > **Nota:** Se o arquivo `requirements.txt` não existir, você pode criá-lo com o comando: `pip freeze > requirements.txt` após instalar as bibliotecas (`pip install reportlab pyinstaller`).
Use code with caution.
Bash
Execute o Script:
Generated bash
python gerarpdf.py
Use code with caution.
Bash
Como Gerar o Executável
Com o ambiente ativado e as dependências instaladas, use o PyInstaller:
Generated bash
pyinstaller --onefile --windowed gerarpdf.py
Use code with caution.
Bash
O executável final estará na pasta dist/.
Adicionar Turmas Permanentemente
Para que uma nova turma sempre apareça ao iniciar o programa, você deve adicioná-la diretamente no código.
Abra o arquivo gerarpdf.py.
Localize a lista turmas no início do código.
Adicione a nova turma seguindo o formato existente:
Generated python
# Exemplo: Adicionando "Dev. 14"
turmas = [
    # ... outras turmas ...
    ("Dev. 13",  "Instrutor(a) em sala?"),
    ("Dev. 14",  "Instrutor(a) em sala?")  # <-- NOVA TURMA ADICIONADA AQUI
]
Use code with caution.
Python
Salve o arquivo e, se desejar, gere um novo executável para distribuir a versão atualizada.
📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
Feito com ❤️ por [Seu Nome]