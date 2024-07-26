from random import choice
from tkinter import simpledialog, messagebox
import string
from time import sleep

class InputValidator:

    @staticmethod
    def get_integer(prompt: str) -> int:
        while True:
            try:
                return int(simpledialog.askstring("Input", prompt))
            except:
                print("\033[0;31mERRO! Digite apenas números inteiros!\033[m")

class PasswordGenerator:

    def __init__(self, quantity: int, size: int, include_lower: bool, include_upper: bool, include_digits:bool, include_specials: bool):
        self.quantity = quantity
        self.size = size
        self.include_lower = include_lower
        self.include_upper = include_upper
        self.include_digits = include_digits
        self.include_specials = include_specials
        self.allowed_chars = self.generate_allowed_chars()

    def generate_allowed_chars(self) -> str:
        chars = ''
        if self.include_lower:
            chars += string.ascii_lowercase
        if self.include_upper:
            chars += string.ascii_uppercase
        if self.include_digits:
            chars += string.digits
        if self.include_specials:
            chars += "!@#$%^&*()_-+=<>?"
        
        return chars
    
    def generate_password(self) -> str:
        """Gera uma única senha com base nos caracteres permitidos e no tamanho especificado."""
        if not self.allowed_chars:
            messagebox.showerror("Erro", "Nenhuma opção de caracteres selecionada.")
            return ''
        
        return ''.join(choice(self.allowed_chars) for _ in range(self.size))
    
    def generate_passwords(self) -> list:
        """Gera uma lista de senhas."""
        if not self.allowed_chars:
            return []
        
        return [self.generate_password() for _ in range(self.quantity)]
   
def main():
    # Exemplos de como usar as classes
    validator = InputValidator()
    quantity = validator.get_integer("Quantidade de senhas:")
    size = validator.get_integer("Tamanho das senhas:")
    
    # Configurações de geração de senha
    include_lower = True
    include_upper = True
    include_digits = True
    include_specials = True
    
    # Cria o gerador de senhas
    generator = PasswordGenerator(quantity, size, include_lower, include_upper, include_digits, include_specials)
    passwords = generator.generate_passwords()
    
    for password in passwords:
        print(password)
    sleep(1)

if __name__ == "__main__":
    main()