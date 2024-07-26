import tkinter as tk
from tkinter import ttk
from functions import PasswordGenerator, InputValidator

class passwordGeneratorGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerador de Senhas")
        self.create_widgets()

    def create_widgets(self):
        """Cria os widgets da interface gráfica."""
        # Widgets de entrada
        self.create_label_and_entry("Quantidade:", 0)
        self.quant_entry = self.entries[0]

        self.create_label_and_entry("Tamanho:", 1)
        self.tam_entry = self.entries[1]

        # Opções de caracteres
        self.create_options_frame()

        # Botão de geração de senhas
        generate_button = ttk.Button(self.root, text="Gerar Senhas", command=self.generate_passwords)
        generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Caixa de texto para exibir as senhas geradas
        self.resultado_text = tk.Text(self.root, height=10, width=50)
        self.resultado_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def create_label_and_entry(self, text, row):
        """Cria um rótulo e uma entrada de texto."""
        ttk.Label(self.root, text=text).grid(row=row, column=0, padx=10, pady=5)
        entry = ttk.Entry(self.root)
        entry.grid(row=row, column=1, padx=10, pady=5)
        if not hasattr(self, 'entries'):
            self.entries = []
        self.entries.append(entry)

    def create_options_frame(self):
        """Cria o frame com as opções de caracteres."""
        options_frame = ttk.Frame(self.root)
        options_frame.grid(row=2, column=0, columnspan=2, pady=5)

        # Opções de caracteres
        self.incluir_maiusculas_var = self.create_checkbutton(
            options_frame, "Incluir letras maiúsculas", 0, 0)
        self.incluir_minusculas_var = self.create_checkbutton(
            options_frame, "Incluir letras minúsculas", 0, 1)
        self.incluir_numeros_var = self.create_checkbutton(
            options_frame, "Incluir números", 0, 2)
        self.incluir_especiais_var = self.create_checkbutton(
            options_frame, "Incluir caracteres especiais", 0, 3)

    def create_checkbutton(self, frame, text, row, column):
        """Cria um botão de seleção."""
        var = tk.BooleanVar(value=True)
        tk.Checkbutton(frame, text=text, variable=var).grid(row=row, column=column, padx=5)
        return var

    def generate_passwords(self):
        """Gera e exibe as senhas com base nas opções fornecidas."""
        # Obtém os valores das entradas e das opções
        try:
            quant = int(self.quant_entry.get())
            tam = int(self.tam_entry.get())
        except ValueError:
            self.resultado_text.delete(1.0, tk.END)
            self.resultado_text.insert(tk.END, "Erro: Quantidade e tamanho devem ser números inteiros.")
            return

        # Verifica se o usuário forneceu valores válidos
        if quant <= 0 or tam <= 0:
            self.resultado_text.delete(1.0, tk.END)
            self.resultado_text.insert(tk.END, "Erro: Quantidade e tamanho devem ser maiores que zero.")
            return

        # Cria o gerador de senhas
        generator = PasswordGenerator(
            quantity=quant,
            size=tam,
            include_lower=self.incluir_minusculas_var.get(),
            include_upper=self.incluir_maiusculas_var.get(),
            include_digits=self.incluir_numeros_var.get(),
            include_specials=self.incluir_especiais_var.get()
        )

        # Gera as senhas
        senha_list = generator.generate_passwords()

        # Exibe as senhas geradas
        self.resultado_text.delete(1.0, tk.END)  # Limpa o texto existente
        for senha in senha_list:
            self.resultado_text.insert(tk.END, senha + "\n")

    def run(self):
        """Inicia a interface gráfica."""
        self.root.mainloop()

if __name__ == "__main__":
    passwordGeneratorGUI().run()