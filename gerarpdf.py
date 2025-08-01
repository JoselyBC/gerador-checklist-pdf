import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import datetime

# Lista inicial de turmas (Pode ser editada para adicionar turmas permanentemente)
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

        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(pady=10, padx=10, fill="both", expand=True)

        self.label_lista = tk.Label(self.frame_lista, text="Turmas Atuais:")
        self.label_lista.pack()

        self.listbox_turmas = tk.Listbox(self.frame_lista, height=15)
        self.listbox_turmas.pack(fill="both", expand=True)

        for turma, _ in turmas:
            self.listbox_turmas.insert(tk.END, turma)

        self.frame_botoes = tk.Frame(root)
        self.frame_botoes.pack(pady=5)

        self.label_nova_turma = tk.Label(self.frame_botoes, text="Nova Turma:")
        self.label_nova_turma.pack(side="left", padx=5)

        self.entry_nova_turma = tk.Entry(self.frame_botoes, width=30)
        self.entry_nova_turma.pack(side="left", padx=5)

        self.btn_adicionar = tk.Button(self.frame_botoes, text="Adicionar Turma", command=self.adicionar_turma)
        self.btn_adicionar.pack(side="left", padx=5)

        self.btn_gerar_pdf = tk.Button(root, text="Gerar PDF", command=self.chamar_gerador_pdf, bg="lightblue")
        self.btn_gerar_pdf.pack(pady=10)

    def adicionar_turma(self):
        nova_turma_nome = self.entry_nova_turma.get()
        if nova_turma_nome:
            turmas.append((nova_turma_nome, "Instrutor(a) em sala?"))
            self.listbox_turmas.insert(tk.END, nova_turma_nome)
            self.entry_nova_turma.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "O nome da turma não pode estar vazio.")

    def chamar_gerador_pdf(self):
        if turmas:
            gerar_pdf(turmas)
        else:
            messagebox.showerror("Erro", "Nenhuma turma na lista para gerar o PDF.")

# ESTE BLOCO É ESSENCIAL PARA INICIAR A JANELA GRÁFICA
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()