perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },

    "Pergunta 2":{
        'pergunta': 'Quanto e 3x2',
        'respostas': {
            'a':'6',
            'b':'8',
            'c':'10',

        },
        'resposta_certa': 'a',
    }   
}

for pergunta, dados_perguntas in perguntas.items():
    print(f'{pergunta}: {dados_perguntas["pergunta"]}')

    print("Respostas: ")

    for resposta, dados_respostas in dados_perguntas["respostas"].items():
        print(f"[{resposta}]: {dados_respostas}")
    
    resposta_usuario = input("Digite sua resposta: ")

    if resposta_usuario == dados_perguntas["resposta_certa"]:
        print("Voce acertou")