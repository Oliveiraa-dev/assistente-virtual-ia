# Assistente Virtual de Produtividade (ProdutiBot) 🚀

Este projeto é resultado do Lab **"Construa Seu Assistente Virtual Com Inteligência Artificial"** da plataforma DIO.

## 🎯 Objetivo
Criar um assistente virtual focado em ajudar usuários a organizar seu tempo, priorizar tarefas e aplicar técnicas de produtividade para evitar a procrastinação e a sobrecarga.

## 📂 Estrutura do Projeto

Os 6 passos fundamentais do desafio estão organizados na seguinte estrutura:

- **1. Base de Conhecimento:** [`data/base_conhecimento.md`](data/base_conhecimento.md) - Contém as técnicas de produtividade que o assistente pode recomendar (Pomodoro, Eisenhower, Regra dos 2 Minutos).
- **2. Documentação:** [`docs/documentacao_agente.md`](docs/documentacao_agente.md) - Define as regras de negócio, o objetivo, o público-alvo e o comportamento do assistente.
- **3. Prompts:** [`src/prompt.md`](src/prompt.md) - Instruções do sistema (System Prompt) para guiar o comportamento da IA.
- **4. Aplicação Funcional:** [`src/app.py`](src/app.py) - Um script Python simples simulando a interação (via CLI) com o assistente, demonstrando a lógica por trás das respostas.
- **5. Avaliação:** [`docs/avaliacao.md`](docs/avaliacao.md) - Métricas e critérios estabelecidos para testar a qualidade das respostas do assistente.
- **6. Pitch:** [`docs/pitch.md`](docs/pitch.md) - Resumo do problema, da solução e do valor que o assistente gera.

## 💻 Como testar a aplicação funcional

Você pode rodar o simulador CLI executando o seguinte comando no terminal:

```bash
python src/app.py
```

## 🛠️ Tecnologias e Conceitos Aplicados
- **Engenharia de Prompt**: Estruturação de instruções claras para IA.
- **Python**: Para criação da interface simulada no terminal.
- **Arquitetura da Informação**: Organização de bases de conhecimento e documentações essenciais.

---
*Projeto desenvolvido para o bootcamp da DIO. Aprendizado focado na criação estruturada de soluções baseadas em IA generativa.*
