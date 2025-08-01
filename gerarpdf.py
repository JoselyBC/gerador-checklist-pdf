import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import datetime

# Lista inicial de turmas (Editável)
turmas = [
    ("Re/start 1 + IA - BRSAO175", "Instrutor(a) em sala?"),
    ("Re/start 1 + IA - BRSAO176", "Instrutor(a) em sala?"),
    ("Re/start 2 + IA - BRSAO191", "Instrutor(a) em sala?"),
    ("Re/start 2 + IA - BRSAO192", "Instrutor(a) em sala?"),
    ("Re/start 2 + IA - BRSAO193", "Instrutor(a) em sala?"),
    ("Re/Start 2 + IA - BRSAO194", "Instrutor(a) em sala?"),
    ("Re/Start 2 + IA - BRSAO198", "Instrutor(a) em sala?"),
    ("Re/Start 2 + IA - BRSAO199", "Instrutor(a) em sala?"),
    ("Dev. 09",  "Instrutor(a) em sala?"),
    ("Dev. 10",  "Instrutor(a) em sala?"),
    ("Dev. 11",  "Instrutor(a) em sala?"),
    ("Dev. 12",  "Instrutor(a) em sala?"),
    ("Dev. 13",  "Instrutor(a) em sala?")
]

def gerar_pdf(lista_turmas):
    """Função para gerar o PDF com a lista de turmas fornecida."""
    if not lista_turmas:
        messagebox.showerror("Erro", "A lista de turmas está vazia. Adicione uma turma antes de gerar o PDF.")
        return

    data_hoje = datetime.today().strftime('%Y%m%d')
    nome_arquivo = f"checklist_instrutores_{data_hoje}.pdf"
    titulo = "Lista de Presença - Instrutores"
    largura, altura = A4
    margem = 50
    linha_altura = 30

    c = canvas.Canvas(nome_arquivo, pagesize=A4)

    def desenhar_cabecalho():
        c.setFont("Helvetica-Bold", 16)
        c.drawString(margem, altura - margem - 10, titulo)
        c.setFont("Helvetica", 12)
        c.drawString(margem, altura - margem - 35, "Marque o checkbox se o instrutor está presente em aula:")
        c.setFillColor(colors.lightgrey)
        c.rect(margem, altura - margem - 60, largura - 2 * margem, 25, fill=1)
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(margem + 10, altura - margem - 45, "Turma")
        c.drawString(margem + 160, altura - margem - 45, "Instrutor(a) em sala?")
        c.drawString(largura - margem - 80, altura - margem - 45, "Presente?")
        return altura - margem - 85

    y_atual = desenhar_cabecalho()

    for i, (turma, instrutor) in enumerate(lista_turmas):
        if y_atual < 80:
            c.showPage()
            y_atual = desenhar_cabecalho()

        c.setFont("Helvetica", 10)
        c.drawString(margem + 10, y_atual + 10, turma)
        c.drawString(margem + 160, y_atual + 10, instrutor)
        c.acroForm.checkbox(
            name=f"presenca_{i}",
            tooltip=f"Presença - {turma}",
            x=largura - margem - 60,
            y=y_atual + 4,
            size=12,
            borderColor=colors.red,
            fillColor=colors.white,
            textColor=colors.black,
            checked=False
        )
        c.setStrokeColor(colors.grey)
        c.line(margem, y_atual, largura - margem, y_atual)
        y_atual -= linha_altura

    c.save()
    messagebox.showinfo("Sucesso", f"PDF gerado com sucesso: {nome_arquivo}")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Checklist de Instrutores")
        self.root.geometry("500x500")

        # Frame da lista
        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(pady=10, padx=10, fill="both", expand=True)
        self.label_lista = tk.Label(self.frame_lista, text="Turmas Atuais:")
        self.label_lista.pack()
        self.listbox_turmas = tk.Listbox(self.frame_lista, height=15)
        self.listbox_turmas.pack(fill="both", expand=True)

        # Frame de ações (Adicionar/Remover)
        self.frame_acoes = tk.Frame(root)
        self.frame_acoes.pack(pady=5, padx=10, fill="x")

        self.label_nova_turma = tk.Label(self.frame_acoes, text="Nova Turma:")
        self.label_nova_turma.pack(side="left", padx=(0, 5))
        self.entry_nova_turma = tk.Entry(self.frame_acoes)
        self.entry_nova_turma.pack(side="left", fill="x", expand=True, padx=5)
        self.btn_adicionar = tk.Button(self.frame_acoes, text="Adicionar", command=self.adicionar_turma)
        self.btn_adicionar.pack(side="left", padx=5)
        
        # Botão de remoção
        self.btn_remover = tk.Button(self.frame_acoes, text="Remover Selecionada", command=self.remover_turma, bg="#FF7F7F")
        self.btn_remover.pack(side="left", padx=5)
        
        # Botão principal para gerar PDF
        self.btn_gerar_pdf = tk.Button(root, text="Gerar PDF Com a Lista Acima", command=self.chamar_gerador_pdf, bg="#ADD8E6", height=2)
        self.btn_gerar_pdf.pack(pady=10, padx=10, fill="x")

        # Preenche a lista inicial
        self.atualizar_listbox()

    def atualizar_listbox(self):
        self.listbox_turmas.delete(0, tk.END)
        for turma, _ in turmas:
            self.listbox_turmas.insert(tk.END, turma)

    def adicionar_turma(self):
        nova_turma_nome = self.entry_nova_turma.get()
        if nova_turma_nome:
            turmas.append((nova_turma_nome, "Instrutor(a) em sala?"))
            self.atualizar_listbox()
            self.entry_nova_turma.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "O nome da turma não pode estar vazio.")
            
    def remover_turma(self):
        selected_indices = self.listbox_turmas.curselection()
        if not selected_indices:
            messagebox.showwarning("Atenção", "Selecione uma turma na lista para remover.")
            return
        
        # Pega o primeiro índice selecionado
        index = selected_indices[0]
        
        # Remove da lista de dados e atualiza a interface
        turmas.pop(index)
        self.atualizar_listbox()

    def chamar_gerador_pdf(self):
        gerar_pdf(turmas)

# Bloco principal para iniciar o programa
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()