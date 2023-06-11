import asyncio
import configparser
import json
import random
import time
import traceback
from datetime import datetime
import spacy
from requests_html import AsyncHTMLSession
import pyttsx3
import requests
from requests_html import HTMLSession
from requests_html import HTML
from twitchio.ext import commands
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from twitchio.ext import pubsub
import twitchio
import pyautogui
from ahk import AHK

ahk = AHK()


chatbot = ChatBot('MeuBot')
trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("G:\\Meu Drive\\Programacao\\BotTwitch\\files\\sw.yml")


my_token = "ohk6cgcc7rjqoxrbhqaxow3s6qex05"
users_oauth_token = "jcm9esnhlv8uiskealh9nqdasjgm3b"
users_channel_id = 400295850

client = twitchio.Client("ohk6cgcc7rjqoxrbhqaxow3s6qex05", initial_channels=["mrquantum_br"])
client.pubsub = pubsub.PubSubPool(client)

#configurações dos filtros do Snap
solicitacoes_pendentes = []

async def event_pubsub_channel_points2(event: pubsub.PubSubChannelPointsMessage):
    global solicitacoes_pendentes
    
    # Adiciona a solicitação à fila de solicitações pendentes
    solicitacoes_pendentes.append(event)
    
    # Verifica se já existe uma solicitação em andamento
    if len(solicitacoes_pendentes) == 1:
        await executar_solicitacoes()

async def executar_solicitacoes():
    global solicitacoes_pendentes
    
    # Obtém a próxima solicitação da fila
    event = solicitacoes_pendentes[0]
    print(event.user.name, 'resgatou', event.reward.title)
    if event.reward.title == 'Criança':
       
            # Espera um pouco antes de enviar as teclas para dar tempo do usuário mudar de janela
            await asyncio.sleep(0.5)
            
            # Envia a combinação de teclas Alt + q
            pyautogui.hotkey('alt', '3')
            ahk.send_input('{Alt down}{7 down}')
            time.sleep(.01)
            ahk.send_input('{Alt up}{7 up}')

            await asyncio.sleep(30)

            pyautogui.hotkey('alt', '3')
            ahk.send_input('{Alt down}{8 down}')
            time.sleep(.01)
            ahk.send_input('{Alt up}{8 up}')

    elif event.reward.title == 'Gordo':
       
            # Espera um pouco antes de enviar as teclas para dar tempo do usuário mudar de janela
            await asyncio.sleep(0.5)
            
            # Envia a combinação de teclas Alt + q
            pyautogui.hotkey('alt', '0')

            await asyncio.sleep(30)

            pyautogui.hotkey('alt', '0')
    elif event.reward.title == 'Chorão':
       
            # Espera um pouco antes de enviar as teclas para dar tempo do usuário mudar de janela
            await asyncio.sleep(0.5)
            
            # Envia a combinação de teclas Alt + 1
            pyautogui.hotkey('alt', '1')

            await asyncio.sleep(30)

            pyautogui.hotkey('alt', '1')        
    elif event.reward.title == 'Diablo':
       
            # Espera um pouco antes de enviar as teclas para dar tempo do usuário mudar de janela
            await asyncio.sleep(0.5)
            
            pyautogui.hotkey('alt', '2')
            ahk.send_input('{Alt down}{5 down}')
            time.sleep(.01)
            ahk.send_input('{Alt up}{5 up}')

            await asyncio.sleep(30)

            pyautogui.hotkey('alt', '2')
            ahk.send_input('{Alt down}{6 down}')
            time.sleep(.01)
            ahk.send_input('{Alt up}{6 up}')

    # Remove a solicitação da fila de solicitações pendentes
    solicitacoes_pendentes.pop(0)
    
    # Verifica se há mais solicitações pendentes e executa se houver
    if solicitacoes_pendentes:
        await executar_solicitacoes()

with open("G:\\Meu Drive\\Programacao\\bot-twitch-python-master\\files\\commands.json", 'r', encoding='UTF-8') as file:
    namecommand = json.load(file)

class Bot(commands.Bot):

    
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        nick_bot = "QuantumGPT"
        super().__init__(token='ohk6cgcc7rjqoxrbhqaxow3s6qex05',
                         nick = nick_bot,
                         prefix='?',
                         initial_channels=['mrquantum_br'])
        
        self.pubsub = pubsub.PubSubPool(self)
      

    
    async def event_ready(self):
        channel = self.get_channel('mrquantum_br')
        await channel.send('!start')
        await channel.send('!iniciar_jogo')

        print(f'Logged in as | {bot.nick}')
        print(f'User id is | {self.user_id}')
        #inicia a autenticacao do client da api para verificacao de eventos no canal
        topics = [
            pubsub.channel_points(users_oauth_token)[users_channel_id],
            pubsub.bits(users_oauth_token)[users_channel_id],
        ]
        await self.pubsub.subscribe_topics(topics)#aguarda os ttopicos
        




    #aguarda o evento acontecer para chamar a função    
    @client.event()
    async def event_pubsub_channel_points(self, event: pubsub.PubSubChannelPointsMessage):
        await event_pubsub_channel_points2(event)

        
    
    async def event_message(self, ctx):
        "Roda toda vez que uma mensagem no chat é enviada."

        # remove do log as mensagens do streamer
        # if ctx.author.name.lower() == self.nick.lower():
        #     return

        if ctx.content.startswith("!"):
            # Separa o comando e os argumentos
            command = ctx.content.split()[0][1:]
            args = ctx.content.split()[1:]
            # Trata o comando
            if command == 'hello':
                await ctx.channel.send(f'Hello {ctx.author.name}!')

            elif command == 'traduzir':
                # Código para executar o comando
                 await self.fn_traduzir(ctx)

            elif command == 'transcrever':
                
                 await self.fn_transcrever(ctx)
            elif command == 'horoscopo':
                
                 await self.fn_horoscopo(ctx)
            elif command == 'clima':
                
                 await self.fn_climaTempo(ctx)

            elif command == 'piada':
                
                 await self.fn_piadas(ctx)
            
            elif command == 'audio':
                
                 await self.fn_msgAudio(ctx)

            elif command == 'runas':
                
                 await self.fn_runas(ctx)

            elif command == 'rta':
                
                 await self.fn_rta(ctx)

            elif command == 'quantumgpt':
                
                 await self.quantumgpt(ctx)

            
            elif command =='start':
                
                 await self.fn_start(ctx)

            elif command =='curiosidade':
                
                 await self.fn_curiosidades(ctx)
            
            elif command =='iniciar_jogo':
                
                 await self.fn_iniciar_jogo(ctx)
            elif command =='ranking':
                
                 await self.fn_ranking(ctx)



            else:
                # Comando não reconhecido
                await ctx.channel.send(f':) O comando "{command}" não foi reconhecido.')
        else:

            # TODO: quantas letras a pessoa escreveu no chat
            # pessoas_online.append(ctx.author.name)
            if "pokebola vai" in ctx.content.lower():
                await self.fn_pokemon(ctx)
            
            if "food supremo" in ctx.content.lower():
                await self.fn_sumonar(ctx)

            if "bom dia" in ctx.content.lower():
                await ctx.channel.send(f":) Bom dia, @{ctx.author.name}! Como você está?")

            elif "boa tarde" in ctx.content.lower():
                await ctx.channel.send(f":) Boa tarde, @{ctx.author.name}! Como você está?")

            elif "boa noite" in ctx.content.lower():
                await ctx.channel.send(f":) Boa noite, @{ctx.author.name}! Como você está?")

            elif "boa madrugada" in ctx.content.lower():
                await ctx.channel.send(
                    f":) Boa madrugada aeew, @{ctx.author.name}! Como você está?",
                )

            # culpa do @Super_Feliz - o teclado dele o trolou
            elif "boa note" in ctx.content.lower():
                await ctx.channel.send(
                    f":) Boa noite, @{ctx.author.name}! Como você está? Seu teclado te trolou...",
                )

            if "salve" in ctx.content.lower():
                await ctx.channel.send(f":) Ta salvado, @{ctx.author.name}! Como você está?")

            if "ctrl + s" in ctx.content.lower():
                await ctx.channel.send(f":) Ta salvado, @{ctx.author.name}! Como você está?")

            if "aoba" in ctx.content.lower():
                await ctx.channel.send(f":) Aoooba, @{ctx.author.name}! Como você está?")

            if "bolacha" in ctx.content.lower():
                await ctx.channel.send(
                    f":) @{ctx.author.name} o correto é Biscoito! SE MANDAR BOLACHA É BAN",
                )

            if "biscoito" in ctx.content.lower():
                await ctx.channel.send(
                    f":) @{ctx.author.name} Errado o correto é bolacha, BO-LA-CHA ",
                )
            if "ladrao" in ctx.content.lower():
                await ctx.channel.send(
                    f":) @{ctx.author.name} Errado, eu apenas cometo pequenos delitos ",
                )
            if "ladrão" in ctx.content.lower():
                await ctx.channel.send(
                    f":) @{ctx.author.name} Errado, eu apenas cometo pequenos delitos ",
                )

            if "time gigante" in ctx.content.lower() or "time de gigante" in ctx.content.lower():
                await ctx.channel.send(
                    f":) Opa @{ctx.author.name}! A equipe Dot de gigante inclui Lushen, Sath, Mellia e Tatu. Lushen deve jogar primeiro para limpar as ondas, seguido por Sath para colocar pontos de danos, depois as duas Mellias e finalmente Tatu para explodir os pontos de danos. Tatu deve ter pelo menos 169 de velocidade para superar o chefe do meio.",
                )

            if "quais os comandos?" in ctx.content.lower():
                await ctx.channel.send(":) Traduzir(!traduzir texto para portugues), transcrever(!transcrever texto para ingles), clima(!clima nomedacidade), runas(!runas nome do monstro em ingles), horoscopo(!horoscopo signo) e piada(!piada)")


    # traduzir texto
    async def fn_traduzir(self, ctx: commands.Context):
            # Pega o texto da mensagem
        texto = " ".join(ctx.content.split()[1:])
        
        if texto == "":
            await ctx.send("Você precisa fornecer um texto para traduzir!")
            return

        session = HTMLSession()
        url = "https://www.google.com/search?q=translate+to+english+"

        url_unificado = f"{url}{texto}"

        req_selecionada = session.get(url_unificado)
        texto_traduzido = req_selecionada.html.find("#tw-target-text")[0].text

        print(f"Traduzir: {texto}")
        print(f"Tradução: {str(texto_traduzido)}")

        await ctx.channel.send(f":) translate: 🫡 {texto_traduzido}")



    async def fn_transcrever(self, ctx: commands.Context):

        texto = " ".join(ctx.content.split()[1:])
        
        if texto == "":
            await ctx.send("Você precisa fornecer um texto para traduzir!")
            return

        # return 'qual o texto quer traduzir?' if texto = 'casadodev' else pass

        session = HTMLSession()
        url = "https://www.google.com/search?q=translate+to+portuguese+"

        url_unificado = f"{url}{texto}"

        req_selecionada = session.get(url_unificado)
        texto_traduzido = req_selecionada.html.find("#tw-target-text")[0].text

        #print(f"Traduzir: {texto}")
        #print(f"Tradução: {str(texto_traduzido)}")

        await ctx.channel.send(f":) translate: 🫡 {texto_traduzido}")


    async def fn_horoscopo(self, ctx: commands.Context):
    #"Mostra o signo solicitado, com base no site Capricho"
        signo = " ".join(ctx.content.split()[1:])
        session = HTMLSession()
        url_signos = "https://capricho.abril.com.br/horoscopo/signo-"

        req_selecionada = session.get(f"{url_signos}{signo}/")
        signo_selecionado = req_selecionada.html.find(".previsao_dia")[0].text

        await ctx.channel.send(f":) {signo}: {signo_selecionado}")

       
    async def fn_climaTempo(self, ctx: commands.Context):
        # Mostrar a previsão do tempo da região

        texto = " ".join(ctx.content.split()[1:])

        session = HTMLSession()

        req_selecionada = session.get(
            f"https://www.google.com.br/search?q=tempo+{texto}",
        )

        cidade_selecionada = req_selecionada.html.find(".BBwThe")[0].text
        temperatura_atual = req_selecionada.html.find("#wob_tm")[0].text
        horario_atual = req_selecionada.html.find("#wob_dts")[0].text
        tipo_clima = req_selecionada.html.find("#wob_dc")[0].text

        # as unidades são especificadas em spans, precisamos inspecionar qual está
        # visível
        spans_unidade = req_selecionada.html.find(".wob-unit > span.wob_t")
        unidade = "ºC"
        for span_unidade in spans_unidade:
            if span_unidade.attrs["style"] == "display:inline":
                unidade = span_unidade.text

        print(f":) Clima agora em {cidade_selecionada}: {temperatura_atual}")

        await ctx.channel.send(
            f"/me Agora na cidade {cidade_selecionada}, é {horario_atual} "
            f"e está {temperatura_atual}{unidade}, com um clima {tipo_clima}",
        )


    async def fn_piadas(self, ctx: commands.Context):
        with open('G:\\Meu Drive\\Programacao\\BotTwitch\\files\\trocadilhos.json',encoding='utf-8') as file:
            data = json.load(file)

        # Gera um índice aleatório para a pergunta e resposta
        index = random.randint(0, len(data)-1)

        # Acessa a pergunta e resposta correspondentes ao índice gerado aleatoriamente
        pergunta = data[index]['pergunta']
        resposta = data[index]['resposta']

        
        await ctx.channel.send(f":) Pergunta: {pergunta}")

        time.sleep(5)
        await ctx.channel.send(f":) Resposta: {resposta}")


    async def fn_msgAudio(self, ctx: commands.Context):
        mensagem = " ".join(ctx.content.split()[1:])
        # if not (ctx.author.is_subscriber | ctx.author.is_mod):
        #     return await ctx.channel.send("Comando liberado para subs!")

        mensagem = ctx.content.lower()[7:]
        print(f"@{ctx.author.name}: {mensagem}")

        moderando = input("Aceita a mensagem? ")

        if moderando == "s":
            print("Aceito...")
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            voice_id = "brazil"
            for voice in voices:
                if voice.languages and voice.languages[0] == "pt-br" and voice.id.split('.')[0] == voice_id:
                    engine.setProperty('voice', voice.id)
                    break
            engine.setProperty('rate', 130)
            engine.say(mensagem)
            engine.runAndWait()
            #return await ctx.channel.send("Agradecido Guys")
        else:
            print("não aceito")
            return await ctx.channel.send(f"@{ctx.author.name} seu audio não foi aceito. :(")
    
    async def fn_runas(self, ctx: commands.Context):

        session = HTMLSession()

        # Desabilita a verificação do certificado SSL
        session.verify = False

        resposta = session.get(
            f"https://summonerswarskyarena.info/monster-list/",

        )

        conteudo_html = resposta.html
        tabela = conteudo_html.find('.monster-list', first=True)

        monstro = " ".join(ctx.content.split()[1:]).capitalize()
        linha = tabela.find(f'tr:contains("{monstro}")', first=True)

        early_runes_celula = linha.find('.early-runes', first=True)
        late_runes_celula = linha.find('.late-runes', first=True)
        stat_priority_celula = linha.find('.stat-priority', first=True)

        early_runes = early_runes_celula.text
        late_runes = late_runes_celula.text
        stat_priority = stat_priority_celula.text

        print (early_runes)
        print (late_runes)
        print (stat_priority)

        await ctx.channel.send(
            f':) Fala @{ctx.author.name}! O {monstro} deverá usar ->  ' +
            f'Runas inciantes: {early_runes}. ' +
            f'Runas late game: {late_runes}. ' +
            f'Priorize os status de {stat_priority}, mas lembre-se isso é somente um dica de um bot abestado.')
        
    async def fn_pokemon(self, ctx: commands.Context):
        with open('G:\\Meu Drive\\Programacao\\BotTwitch\\files\\pokemon.json',encoding='utf-8') as file:
            data = json.load(file)

        
        random_pokemon = random.choice(data)

        # Acessa a pergunta e resposta correspondentes ao índice gerado aleatoriamente
        pokemon = random_pokemon
        
        
        await ctx.channel.send(f":) Parabéns @{ctx.author.name}, vc capturou um -> {pokemon}")
    
    async def fn_sumonar(self, ctx: commands.Context):

        session = HTMLSession()
                # Desabilita a verificação do certificado SSL
        session.verify = False

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'


        }

        resposta = session.get(
            f"https://summonerswarskyarena.info/monster-list/"

        )

        conteudo_html = resposta.html
        tabela = conteudo_html.find('.monster-list', first=True)
        linhas_com_5 = tabela.find('tr:contains("5")')

        if len(linhas_com_5) > 0:
            linha_aleatoria = random.choice(linhas_com_5)
            colunas_name = linha_aleatoria.find('.name')
            monstro = colunas_name[1].text


        await ctx.channel.send(
         f':) @{ctx.author.name}! Vc invocou o poder do food supremo e próximo Nat 5 que vai pegar é o(a) -> {monstro} .')
        
    async def fn_rta(self, ctx: commands.Context):

        session = AsyncHTMLSession()

        monstro = " ".join(ctx.content.split()[1:])
        await ctx.channel.send(f' @{ctx.author.name}! Estou carregando as informações...')
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        resposta = await session.get(
            f"https://swarena.gg/monster/{monstro}",headers=headers

        )
        await resposta.html.arender(timeout=12000)
            
        # extrair a tabela do HTML
        vitorias = resposta.html.xpath('/html/body/div[1]/div/div/div[1]/main/div/div/div/div[1]/div/div[4]/div[1]/div/div/span[2]')[0]
        partidas = resposta.html.xpath('/html/body/div[1]/div/div/div/main/div/div/div/div[1]/div/div[4]/div[2]/div/span[2]')[0]
        lider = resposta.html.xpath('/html/body/div[1]/div/div/div/main/div/div/div/div[1]/div/div[4]/div[3]/div/span[2]')[0]
        banido = resposta.html.xpath('/html/body/div[1]/div/div/div/main/div/div/div/div[1]/div/div[4]/div[4]/div/span[2]')[0]

        await ctx.channel.send(
             f':) Fala @{ctx.author.name}! O monstro {monstro} está presente em {partidas.text} das partidas de RTA, tem uma uma taxa de vitorias na season 25 de -> {vitorias.text}, é lider -> {lider.text} e é banido(a) -> {banido.text} das vezes.')
        

    async def fn_start(self, ctx: commands.Context):
    # Mostrando os comandos disponíveis no bot
        while True:
            msg_aleatoria = list(
                open(f'G:\Meu Drive\\Programacao\\BotTwitch\\files\\texto_engajamento.txt', encoding="utf-8"),
            
            )

            if len(msg_aleatoria) > 0:
                #"Mostrando mensagens de engajamento no chat"
                msg_selecionada = random.choice(msg_aleatoria)

                # await ws.send_privmsg(inicia_canal, msg_selecionada)
                await ctx.channel.send(f"{msg_selecionada}")
                await asyncio.sleep(300.0)

    async def fn_curiosidades(self, ctx: commands.Context):
                    curiosidades = list(
                        open(f'G:\Meu Drive\\Programacao\\BotTwitch\\files\\curiosidades.txt', encoding="utf-8"),
                    )
                    
                    if len(curiosidades) > 0:
                        curiosidade_selecionada = random.choice(curiosidades)

                        await ctx.channel.send(f":) {curiosidade_selecionada}")

    #incia o jogo de perguntas e respostas    
    async def fn_iniciar_jogo(self, ctx: commands.Context):
        pergunta_atual = None
        pergunta_respondida = False

        def carregar_perguntas():
            with open("G:\\Meu Drive\\Programacao\\BotTwitch\\files\\PerguntaseRepostas.txt", "r", encoding="utf-8") as file:
                conteudo = file.readlines()
            perguntas = [linha.strip().split(":") for linha in conteudo]
            return perguntas

        perguntas = carregar_perguntas()

        if len(perguntas) == 0:
            print("Não há perguntas disponíveis.")
            return

        pergunta_atual = random.choice(perguntas)

        async def enviar_pergunta():
            nonlocal pergunta_atual, pergunta_respondida

            pergunta_atual = random.choice(perguntas)
            await ctx.channel.send(f":) Pergunta: {pergunta_atual[0]} ")
            start_time = time.time()
            timeout = 60  # Tempo inicial de timeout em segundos

            while not pergunta_respondida:
                def carregar_pontuacoes():
                    pontuacoes = {}
                    with open("G:\\Meu Drive\\Programacao\\BotTwitch\\files\\pontuacoes.txt", "r") as arquivo:
                        linhas = arquivo.readlines()
                        for linha in linhas:
                            nick, pontos = linha.strip().split(":")
                            pontuacoes[nick] = int(pontos)
                    return pontuacoes
                def salvar_pontuacoes(pontuacoes):
                    with open("G:\\Meu Drive\\Programacao\\BotTwitch\\files\\pontuacoes.txt", "w") as arquivo:
                        for nick, pontos in pontuacoes.items():
                            arquivo.write(f"{nick}:{pontos}\n")


                try:
                    def check(m):
                        return "resposta" in m.content.lower()
                    resposta = await bot.wait_for('message',predicate=check, timeout=timeout)  # Aguardar uma mensagem do chat
                    #print (resposta[0].content.replace("resposta", "").strip().lower())
                    
                    if resposta[0].content.replace("resposta", "").strip().lower() == pergunta_atual[1].lower():
                        await ctx.channel.send(f":) @{resposta[0].author.name} Parabéns! Você acertou a resposta.")
                        pergunta_respondida = True
                        # Atualizar pontuação
                        pontuacoes = carregar_pontuacoes()
                        if resposta[0].author.name in pontuacoes:
                            pontuacoes[resposta[0].author.name] += 1
                        else:
                            pontuacoes[resposta[0].author.name] = 1
                        salvar_pontuacoes(pontuacoes)
    

                        await asyncio.sleep(360)
                    else:
                        await ctx.channel.send(f":) @{resposta[0].author.name} Incorreto.")
                        elapsed_time = time.time() - start_time
                        timeout = max(timeout - elapsed_time, 0)  # Reduzir o timeout pelo tempo decorrido
                        resposta = ""
                        continue
                except asyncio.TimeoutError:
                    await ctx.channel.send(f":) Tempo encerrado: A resposta correta era {pergunta_atual[1]} ")
                    pergunta_respondida = True
                    await asyncio.sleep(360)

            pergunta_respondida = False
            await enviar_pergunta()

        await enviar_pergunta()

    async def fn_ranking(self, ctx: commands.Context):
        def carregar_ranking():
            ranking = {}
            with open("G:\\Meu Drive\\Programacao\\BotTwitch\\files\\pontuacoes.txt", "r") as file:
                for linha in file:
                    nick, pontos = linha.strip().split(":")
                    ranking[nick] = int(pontos)
            return ranking

        ranking = carregar_ranking()

        if not ranking:
            await ctx.channel.send("Não há pontos registrados.")
            return

        # Ordenar o ranking com base nas pontuações em ordem decrescente
        ranking_ordenado = sorted(ranking.items(), key=lambda item: item[1], reverse=True)

        resposta = ":) Ranking de Pontuações:\n"
        for i, (nick, pontos) in enumerate(ranking_ordenado[:5], start=1):
            resposta += f"{i}. {nick}: {pontos} pontos\n"

        await ctx.channel.send(resposta)

            
bot = Bot()
bot.run()
#client.run(bot)