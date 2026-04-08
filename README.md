# API Calculadora

Esta é uma API simples feita com Flask que realiza operações matemáticas básicas.

---

## Funcionalidades

A API permite:

- Somar dois números
- Subtrair dois números
- Multiplicar dois números
- Dividir dois números

---

## URL da API

http://127.0.0.1:5000/calcular

---

## Parâmetros

A API recebe os seguintes parâmetros pela URL:

- `a` → primeiro número
- `b` → segundo número
- `op` → operação

### Operações disponíveis:

- `%2B` → soma
- `-` → subtração
- `x` → multiplicação
- `/` → divisão

---

## Exemplo de uso
http://127.0.0.1:5000/calcular?a=10&b=5&op=%2B


---

## Exemplo de resposta

```json
{
  "a": 10,
  "b": 5,
  "operacao": "Adição",
  "resultado": 15
}

Como executar o projeto
1. Instalar o Flask
python -m pip install flask
2. Rodar o servidor
python app.py
3. Acessar no navegador
http://127.0.0.1:5000/

Autora: Maria Eduarda Silva Souza
