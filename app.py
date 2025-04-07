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

    ["Qual emoji define você hoje?", "Qual emoji você apagaria do teclado?"],

    ["Qual lugar da sua cidade você ama?", "Qual parte da sua cidade você evita?"],

    ["Qual tarefa doméstica você curte?", "Qual tarefa doméstica você odeia?"],

    ["Qual superstição você leva a sério?", "Qual superstição você acha engraçada?"],

    ["Qual aplicativo te salva no dia a dia?", "Qual app você só usa em emergências?"],

    ["Qual presente você adoraria dar para alguém?", "Qual presente você daria só por obrigação?"],

    ["Qual piada você nunca esquece?", "Qual piada te dá vergonha alheia?"],

    ["Qual cheiro te acalma?", "Qual cheiro te irrita?"],

    ["Qual animal representa sua personalidade?", "Qual bicho você não entende como alguém gosta?"],

    ["Qual horário do dia você rende mais?", "Qual hora você quer desaparecer do mundo?"],

    ["Qual professor te inspirou?", "Qual aula você queria ter pulado pra sempre?"],

    ["Quantos reais vc gastaria em um ONLY FANS?","escolha um numero entre 1 real e 100k reais"],

    ["Quantos reais vc gastaria no seu casamento?","Quantos reais vc gastaria em um ONLY FANS"],
   
    ["Quantos Filhos você teria?","Escolha um numero entre 0 a 100"],

    ["Escolha um numero entre 0 a 20","Escolha um numero entre 0 a 20"],

    ["Qual a idade ideal para o primeiro namorado(a)?", "Com quantos anos você teve seu primeiro crush?"],

    ["qual a idade ideal para casar", "escolha um numero de 1 a 20"],

    ["limite de filhos por familia (numero)", "escolha um numero de 1 a 20"],

    ["legalizacao das drogas: sim ou nao", "escolha entre sim ou não"],

    ["cotas raciais sao justas?: sim ou não", "escolha entre sim ou não"],

    ["tortura deve ser usado em casos extremos?: sim ou não", "escolha entre sim ou não"],

    ["Qual seu filme favorito?", "Qual filme todo mundo ama e você odeia?"],

    ["Qual sua comida favorita?", "O que você odeia que todo mundo ama comer?"],

    ["Qual livro marcou sua vida?", "Qual livro famoso você acha superestimado?"],

    ["Qual sua viagem dos sonhos?", "Qual lugar você nunca visitaria?"],

    ["Qual habilidade você gostaria de ter?", "Qual talento comum você inveja?"],

    ["Qual app você mais usa no celular?", "Qual rede social você detesta?"],

    ["Qual estilo musical define você?", "Qual gênero musical você não suporta?"],

    ["Qual seria seu superpoder ideal?", "Qual poder você acha mais inútil?"],

    ["Qual assunto você domina?", "Sobre quala assunto você nunca falaria?"],

    ["Qual série você maratonaria?", "Qual série famosa você não aguenta?"],

    ["Qual esporte você gostaria de praticar?", "Qual atividade física você evita?"],

    ["Qual presente você adoraria ganhar?", "Qual presente você já jogou fora?"],

    ["Qual profissão você admira?", "Qual trabalho você nunca faria?"],

    ["Qual década te fascina?", "Qual época histórica você detestaria?"],

    ["Qual animal você teria como pet?", "Qual animal você tem medo?"],

    ["Qual hábito seu é incomum?", "Qual mania alheia te irrita?"],

    ["Qual elogio você mais recebe?", "Qual crítica te machuca?"],

    ["Qual idioma você quer aprender?", "Qual língua acha desinteressante?"],

    ["Qual invenção mudou sua vida?", "Qual tecnologia você dispensaria?"],

    ["Qual memória de infância te faz sorrir?", "Qual lembrança te envergonha?"],

    ["Qual personagem fictício é seu 'alter ego'?", "Qual protagonista você detesta?"],

    ["Qual conselho você daria a si mesmo do passado?", "Qual erro você não cometeria de novo?"],

    ["Qual hobby relaxa você?", "Qual passatempo você acha chato?"],

    ["Qual evento social você adora?", "Qual tipo de festa você evita?"],

    ["Qual cantor(a) você veria ao vivo?", "Qual artista você não pagaria para ver?"],

    ["Qual mito você gostaria que fosse real?", "Qual lenda te assusta?"],

    ["Qual fenômeno natural te encanta?", "Qual desastre da natureza te apavora?"],

    ["Qual chefe você admirou?", "Qual chefe foi seu pesadelo?"],

    ["Qual aula você nunca faltava?", "Qual matéria você dormia na escola?"],

    ["Qual meme você nunca esquece?", "Qual trend da internet você acha sem graça?"],

    ["Qual frase te motiva?", "Qual clichê você odeia ouvir?"],

    ["Qual doce você não resiste?", "Qual sobremesa famosa você não gosta?"],

    ["Qual sensação física você ama?", "Qual toque físico você não suporta?"]
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



