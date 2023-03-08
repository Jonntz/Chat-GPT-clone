import openai
from get_env import print_env

#Enviroment variable
env = print_env(['API_KEY'])

# Configuring enviroment
openai.api_key = env['API_KEY']

# Model engine
model_engine = 'gpt-3.5-turbo'

# Chat implementation
while True:
    print(50*'-')
    prompt = input('Pergunte o que quiser:\n (Caso deseje encerrar sua consulta escreva o comando ENCERRAR) \n \n')

    if prompt == 'encerrar' or prompt == 'ENCERRAR':
        break

    print('.')
    print('..')
    print('...')
    print('Aguarde enquando vou atrás da sua resposta...')
    print(50*'-')

    # Configurando resposta
    completion = openai.ChatCompletion.create(
        model = model_engine,
        messages= [
            {"role":"user", "content":prompt},
            {"role":"system", "content":prompt},
            {"role":"assistant", "content":prompt}
        ],
        max_tokens = 4000,
        n=1,
        stop=None,
        temperature = 0.5
    )

    # print(completion)

    print(50*'-')
    response = completion.choices[0].message.content
    print('\n')
    print(response)


    