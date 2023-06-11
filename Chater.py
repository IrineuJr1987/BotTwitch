from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
# isso aqui só precisa para corrigir o bug
from spacy.cli import download

# download("en_core_web_sm")

# class ENGSM:
#     ISO_639_1 = 'en_core_web_sm'

# chatbot = ChatBot('Ron Obvious', tagger_language=ENGSM)
chatbot = ChatBot('Irinelson')

trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("chatterbot.corpus.portuguese")
trainer.train("G:\\Meu Drive\\Programacao\\BotTwitch\\files\\sw.yml")

#conversa = ["Coe", "E ai blz?", "Tranquilo",]
#trainer = ListTrainer(chatbot)
#trainer.train(conversa)

while True:
    mensagem = input("Mande uma msg para o chatbot:")
    if mensagem =="parar":
        break
    resposta = chatbot.get_response(mensagem)
    print(resposta)