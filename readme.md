# Gerador de Senhas em Python

Este projeto é um gerador de senhas em Python com uma interface gráfica simples usando o Tkinter. Ele permite que os usuários escolham a quantidade e o tamanho das senhas, bem como os tipos de caracteres que desejam incluir (letras maiúsculas, letras minúsculas, números e caracteres especiais).

## 🚀 Começando

Estas instruções ajudarão você a obter uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implantação)** para saber como implantar o projeto.

### 📋 Pré-requisitos

Você precisará ter o Python 3.x instalado na sua máquina para executar o gerador de senhas. Para verificar se o Python está instalado e qual versão, você pode usar o seguinte comando no terminal:

```bash
python --version
```
Se o Python não estiver instalado, você pode baixá-lo do [site oficial do Python](https://www.python.org/downloads/).

### 🔧 Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento e executar o projeto:

#### 1. **Clone o repositório:**

```
git clone https://github.com/MayconWork/passwordGenerator.git
cd passwordGenerator
```

#### 2. **(Opcional) Crie um ambiente virtual:**

É uma boa prática criar um ambiente virtual para gerenciar as dependências do projeto.

```
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

#### 3. **Execute o Gerador de Senhas:**

```
python main.py
```

### 🛠️ Funcionalidades

* Gerar Senhas Aleatórias: Gera uma lista de senhas com base nas preferências do usuário.
* Opções Personalizáveis: Permite escolher o número de senhas, o comprimento das senhas e os tipos de caracteres a serem incluídos.
* Interface Gráfica de Usuário (GUI): Interface amigável e fácil de usar.

### 📋 Estrutura do Projeto

* main.py: Ponto de entrada principal do aplicativo que inicializa e executa a interface gráfica do usuário.
* interface.py: Arquivo principal com a interface gráfica do usuário.
* functions.py: Contém as classes PasswordGenerator e InputValidator, responsáveis pela lógica de geração de senhas e validação de entradas.
* README.md: Este arquivo, que fornece informações sobre o projeto.

### 📦 Implantação

Este projeto é simples e pode ser executado em qualquer sistema com Python instalado. Para implantar em um sistema ativo, siga os passos de instalação em qualquer máquina com Python.

### 🧩 Como Funciona o Código

#### 📝 Detalhes do Código

##### 1. **Importações e Configuração**
No início dos arquivos passwordGeneratorGUI.py e functions.py, são importadas as bibliotecas necessárias. Utilizamos tkinter para a GUI e importamos funções de functions.py.

##### 2. **Classes e Funções**

* PasswordGenerator: Gera senhas baseadas nas configurações fornecidas pelo usuário.
* InputValidator: Valida as entradas do usuário, garantindo que sejam números inteiros.
* PasswordGeneratorGUI: Gerencia a interface gráfica do usuário, incluindo campos de entrada, botões e exibição de resultados.

##### 3. **Execução do Aplicativo**

O arquivo main.py inicializa o aplicativo criando uma instância de PasswordGeneratorGUI e chamando seu método run() para iniciar a interface gráfica.

```
def main():
    app = PasswordGeneratorGUI()
    app.run()

if __name__ == "__main__":
    main()
```

#### ⚙️ Executando o Projeto

Para executar o programa, basta seguir os passos de instalação. O usuário pode então inserir suas preferências e gerar senhas conforme desejado.


