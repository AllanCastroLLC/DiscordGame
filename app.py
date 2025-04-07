import discord
import random
import asyncio

TOKEN = 'API-BOT-DISCORD'

# IDs dos usuários
todos_os_usuarios = [
    123456789012345678,
    362712323827639718,
    362715816253816251,
    327327619358719023
    
]

# Pares de mensagens: [mensagem_padrão, mensagem_especial]
mensagens_em_pares = [

    ["O que te faz rir sem motivo?", "O que te deixa bravo rapidamente?"],

    ["Qual hábito matinal você não abre mão?", "O que você odeia fazer logo cedo?"],

    ["Com quem você passaria um dia inteiro?", "Com quem você evitaria até 5 minutos?"],

    ["Qual foi seu maior acerto até hoje?", "Qual decisão você gostaria de refazer?"],

    ["Qual música te define hoje?", "Qual música você pula toda vez que toca?"],

    ["Qual emoji você mais usa?", "Qual emoji você acha brega?"],

    ["Qual app você nunca apagaria?", "Qual app você só tem porque é obrigado?"],

    ["Qual foi o melhor presente que já ganhou?", "Qual foi o presente mais aleatório que já recebeu?"],

    ["Qual sua bebida favorita?", "Qual bebida você não consegue nem sentir o cheiro?"],

    ["Com qual celebridade você gostaria de conversar?", "Qual celebridade te irrita sem motivo?"],

    ["Qual festival ou evento você quer ir?", "Qual tipo de evento te dá preguiça?"],

    ["Qual habilidade você aprendeu sozinho?", "Qual coisa simples você nunca aprendeu?"],

    ["Qual desenho infantil marcou sua infância?", "Qual desenho infantil você não suportava?"],

    ["Qual videogame marcou sua vida?", "Qual videogame você nunca entendeu a graça?"],

    ["Qual animal selvagem você gostaria de ver de perto?", "Qual animal você não chegaria perto nem por dinheiro?"],

    ["Qual amigo te conhece melhor?", "Qual amizade te decepcionou?"],

    ["Qual seu maior orgulho pessoal?", "Qual parte de você quer melhorar?"],

    ["Qual profissão você teria em outra vida?", "Qual carreira nunca te atrairia?"],

    ["Qual seu maior medo irracional?", "O que você finge não ter medo, mas tem?"],

    ["Qual parte do seu dia você mais espera?", "Qual momento do dia te dá preguiça?"],

    ["Qual invenção você adoraria ter criado?", "Qual tecnologia nova você não entende?"],

    ["Qual hábito alheio você acha interessante?", "Qual mania dos outros te irrita profundamente?"],

    ["Qual conquista recente te deixou feliz?", "Qual meta você vive adiando?"],

    ["Qual perfume te traz boas lembranças?", "Qual cheiro te dá náusea?"],

    ["Qual momento da sua vida você reviveria?", "Qual fase da vida você não sente saudade?"],

    ["Qual expressão você mais usa?", "Qual gíria você evita usar?"],

    ["Qual seu talento escondido?", "O que você queria saber fazer e nunca conseguiu?"],

    ["Qual emoji define você hoje?", "Qual emoji você apagaria do teclado?"]
]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot logado como {client.user}')

    # Escolhe um par de mensagens
    mensagem_padrao, mensagem_especial = random.choice(mensagens_em_pares)

    # Escolhe aleatoriamente o usuário especial
    usuario_especial = random.choice(todos_os_usuarios)

    for user_id in todos_os_usuarios:
        user = await client.fetch_user(user_id)
        if user:
            try:
                if user_id == usuario_especial:
                    await user.send(mensagem_especial)
                    print(f"[ESPECIAL] Enviado para {user.name}: {mensagem_especial}")
                else:
                    await user.send(mensagem_padrao)
                    print(f"[PADRÃO] Enviado para {user.name}: {mensagem_padrao}")
            except Exception as e:
                print(f"Erro ao enviar mensagem para {user.name}: {e}")

    await client.close()

client.run(TOKEN)



