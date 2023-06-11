# import twitchio
# from twitchio.ext import pubsub


# my_token = "ohk6cgcc7rjqoxrbhqaxow3s6qex05"
# users_oauth_token = "jcm9esnhlv8uiskealh9nqdasjgm3b"
# users_channel_id = 400295850

# client = twitchio.Client("ohk6cgcc7rjqoxrbhqaxow3s6qex05", initial_channels=["mrquantum_br"])
# client.pubsub = pubsub.PubSubPool(client)


# async def event_pubsub_channel_points2(event: pubsub.PubSubChannelPointsMessage):
#     print('Redemption by ', event.user.name, 'of reward', event.reward.title, 'with text', event.reward.prompt,
#           'done')

# @client.event()
# async def event_message(message):
#     if message.echo:
#         return
#     print(message.content)

# @client.event()
# async def event_ready():
#     print(f"Ready | {client.nick}")
#     topics = [
#     pubsub.channel_points(users_oauth_token)[users_channel_id],
#     pubsub.bits(users_oauth_token)[users_channel_id],]
#     await client.pubsub.subscribe_topics(topics)


# @client.event()
# async def event_pubsub_bits(event: pubsub.PubSubBitsMessage):
#     pass # do stuff on bit redemptions

# @client.event()
# async def event_pubsub_moderation_action(event: pubsub.PubSubModerationAction):
#     print(event)
#     print(event.action)

# @client.event()
# async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
#     await event_pubsub_channel_points2(event)

# client.run()pip install "ahk[binary]"

###############################################################################################
# from ahk import AHK
# import time
# import pyautogui

# ahk = AHK()
# pyautogui.hotkey('alt', '2')
# ahk.send_input('{Alt down}{5 down}')
# time.sleep(.01)
# ahk.send_input('{Alt up}{5 up}')#
############################################################################
from gtts import gTTS
import pygame
from io import BytesIO

# Cria um objeto de fala com uma voz feminina em português do Brasil
tts = gTTS('Olá, eu sou um bot.', lang='pt-br', slow=False, tld='com.br', speed=1.5)

# Salva o áudio em um buffer de memória
audio_bytes = BytesIO()
tts.write_to_fp(audio_bytes)
audio_bytes.seek(0)

# Inicializa o pygame
pygame.init()

# Carrega o áudio a partir do buffer de memória
pygame.mixer.music.load(audio_bytes)

# Toca o áudio
pygame.mixer.music.play()

# Aguarda a reprodução terminar
while pygame.mixer.music.get_busy():
    continue

# Finaliza o pygame
pygame.quit()
