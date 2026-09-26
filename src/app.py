import os

def main():
    print("=======================================")
    print("Bem-vindo ao ProdutiBot (Simulação CLI)")
    print("=======================================")
    print("Este é um protótipo de terminal. Na versão completa, ele se conectaria à API de um LLM (ex: OpenAI, Gemini).")
    print("Baseado no prompt definido em src/prompt.md e na base de conhecimento em data/base_conhecimento.md\n")

    print("ProdutiBot: Olá! Eu sou o ProdutiBot. Qual é o seu maior desafio de produtividade hoje?")
    
    while True:
        try:
            user_input = input("\nVocê: ")
            if user_input.lower() in ["sair", "exit", "quit"]:
                print("ProdutiBot: Até logo! Lembre-se: feito é melhor que perfeito. Um ótimo dia de foco para você!")
                break
            
            # Respostas hardcoded simulando a IA com base na nossa documentação
            if "começar" in user_input.lower() or "muita coisa" in user_input.lower() or "priorizar" in user_input.lower():
                print("ProdutiBot: Entendo como isso pode ser esmagador! Para muitas tarefas, eu recomendo a **Matriz de Eisenhower**. Vamos dividir suas tarefas e focar primeiro no que é 'Urgente e Importante'. Quer ajuda para classificar a sua primeira tarefa?")
            elif "foco" in user_input.lower() or "distração" in user_input.lower() or "distraio" in user_input.lower():
                print("ProdutiBot: Manter o foco pode ser difícil mesmo. Já tentou a **Técnica Pomodoro**? Consiste em trabalhar por 25 minutos sem interrupções e depois pausar por 5 minutos. Que tal escolhermos uma tarefa para o seu primeiro Pomodoro agora?")
            elif "rápido" in user_input.lower() or "pequena" in user_input.lower():
                print("ProdutiBot: Excelente! Para tarefas rápidas, use a **Regra dos 2 Minutos**: se leva menos de 2 minutos, faça agora mesmo. Isso evita acúmulo. Vai lá fazer e me avise quando terminar!")
            else:
                print("ProdutiBot: Entendi. Me conte mais um pouco sobre como você costuma organizar o seu dia a dia, para que eu possa recomendar a melhor estratégia (como Pomodoro ou a Matriz de Eisenhower).")

        except KeyboardInterrupt:
            print("\nProdutiBot: Até logo!")
            break

if __name__ == "__main__":
    main()
