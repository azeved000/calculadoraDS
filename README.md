# 🧮 Calculadora Python API

Uma API REST em Flask que fornece diferentes tipos de cálculos matemáticos.

## 📋 Funcionalidades

- **Calculator 1**: Divisão por números
- **Calculator 2**: Desvio padrão multiplicado por 11 elevado a 0.95
- **Calculator 3**: Inverso da variância com validação
- **Calculator 4**: Média aritmética

## 🛠️ Tecnologias

- **Python 3.11+**
- **Flask** - Framework web
- **NumPy** - Cálculos matemáticos
- **Pytest** - Testes unitários

## 🚀 Como executar

### 1. Clone o repositório
```bash
git clone <URL_DO_REPOSITORIO>
cd calculadora
```

### 2. Criar ambiente virtual
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# ou
source .venv/bin/activate  # Linux/Mac
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar testes
```bash
pytest -v
```

### 5. Executar aplicação
```bash
python run.py
```

## 📁 Estrutura do Projeto

```
calculadora/
├── src/
│   ├── calculators/           # Lógicas de cálculo
│   │   ├── calculator_1.py
│   │   ├── calculator_2.py
│   │   ├── calculator_3.py
│   │   ├── calculator_4.py
│   │   └── *_test.py         # Testes unitários
│   ├── drivers/              # Handlers de bibliotecas externas
│   │   └── numpay_handler.py
│   ├── errors/               # Tratamento de erros
│   └── main/                 # Configuração da aplicação
├── requirements.txt
└── README.md
```

## 🧪 Testes

Todos os calculadores possuem testes unitários e de integração:

```bash
# Executar todos os testes
pytest -v

# Executar teste específico
pytest src/calculators/calculator_4_test.py -v
```

## 📝 Licença

Este projeto foi desenvolvido como parte do curso da Rocketseat.