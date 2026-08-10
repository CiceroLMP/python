import requests


def obter_frase_motivacional():
    try:
        resposta = requests.get("https://api.adviceslip.com/advice", timeout=3)
        resposta.raise_for_status()
        dados = resposta.json()
        return dados.get("slip", {}).get("advice", "Continue firme nas suas tarefas!")
    except requests.RequestException:
        return "Continue firme nas suas tarefas!"
