"""
Projeto: Construa seu Assistente Virtual com Inteligência Artificial
Descrição: assistente virtual simples em Python, com reconhecimento de intenções
por palavras-chave, respostas contextualizadas e histórico da conversa.
"""

from datetime import datetime


class AssistenteVirtual:
    def __init__(self, nome="AIA"):
        self.nome = nome
        self.historico = []

        self.intencoes = {
            "saudacao": ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"],
            "ajuda": ["ajuda", "help", "o que você faz", "o que voce faz"],
            "python": ["python", "programação", "programacao", "código", "codigo"],
            "ia": ["inteligência artificial", "inteligencia artificial", "ia", "machine learning"],
            "horario": ["hora", "horário", "horario"],
            "despedida": ["tchau", "até mais", "ate mais", "sair", "encerrar"],
        }

        self.respostas = {
            "saudacao": [
                "Olá! Eu sou seu assistente virtual. Como posso ajudar?",
                "Oi! Estou pronto para conversar. 😊",
            ],
            "ajuda": [
                "Posso conversar sobre Python, inteligência artificial e programação. "
                "Também posso informar a hora e encerrar a conversa."
            ],
            "python": [
                "Python é uma linguagem bastante utilizada em automação, análise de dados "
                "e inteligência artificial."
            ],
            "ia": [
                "Inteligência Artificial é um conjunto de técnicas que permite a sistemas "
                "realizar tarefas que normalmente exigiriam capacidades humanas, como "
                "classificação, previsão e geração de conteúdo."
            ],
            "horario": [
                f"Agora são {datetime.now().strftime('%H:%M:%S')}."
            ],
            "despedida": [
                "Até mais! Foi um prazer conversar com você.",
            ],
        }

    def identificar_intencao(self, mensagem):
        texto = mensagem.lower().strip()

        # Procura a intenção com maior número de palavras-chave encontradas.
        pontuacoes = {}
        for intencao, palavras in self.intencoes.items():
            pontuacoes[intencao] = sum(1 for palavra in palavras if palavra in texto)

        melhor = max(pontuacoes, key=pontuacoes.get)
        return melhor if pontuacoes[melhor] > 0 else "desconhecida"

    def responder(self, mensagem):
        intencao = self.identificar_intencao(mensagem)

        if intencao == "desconhecida":
            resposta = (
                "Ainda estou aprendendo. Não encontrei uma resposta específica para isso. "
                "Tente perguntar sobre Python, IA ou programação."
            )
        else:
            resposta = self.respostas[intencao][0]

        self.historico.append({
            "usuario": mensagem,
            "assistente": resposta,
            "intencao": intencao,
            "data": datetime.now().isoformat(timespec="seconds")
        })

        return resposta, intencao


def executar():
    assistente = AssistenteVirtual()

    print("=" * 55)
    print("      ASSISTENTE VIRTUAL COM INTELIGÊNCIA ARTIFICIAL")
    print("=" * 55)
    print("Digite 'sair' para encerrar.\n")

    while True:
        mensagem = input("Você: ")

        resposta, intencao = assistente.responder(mensagem)
        print(f"{assistente.nome}: {resposta}")
        print(f"[Intenção identificada: {intencao}]\n")

        if intencao == "despedida":
            break


if __name__ == "__main__":
    executar()
