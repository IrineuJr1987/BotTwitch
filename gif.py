import requests
import speech_recognition as sr
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import nltk
from nltk.tokenize import sent_tokenize
import json
import urllib.request
import random
import schedule
import time
from vosk import Model, KaldiRecognizer
import pyaudio
from nltk.sentiment import SentimentIntensityAnalyzer

# model = Model(r'G:\Meu Drive\Programacao\auto\Chatgpt\Vosk pt-br')
# recognizer = KaldiRecognizer(model, 16000)

# #reconhecer mic
# cap = pyaudio.PyAudio()
# stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000,input=True, frames_per_buffer=8192)
# stream.start_stream

# Função para buscar e fazer o download de um gif
def search_and_download_gif(termo):
    apikey = "AIzaSyBV47W40ze9BBtnT4Mkv8lzzYsngmD-dW8"  # Substitua pela sua chave de API
    lmt = 20
    ckey = "My Project"  # set the client_key for the integration and use the same value for all API calls
    country= "BR"

    # our test search
    search_term = termo

    # get the top 8 GIFs for the search term
    r = requests.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s&locale=pt_BR&media_filter=gif" % (search_term, apikey, ckey,  lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        featured_gifs = json.loads(r.content)
        
    else:
        featured_gifs = None

    random_number = random.randint(1, 5)

    gif_url = featured_gifs["results"][random_number]["media_formats"]["gif"]["url"]
    #print(gif_url)
    # Define o nome do arquivo para salvar o GIF
    gif_file_name = "gif.gif"

    # Faz o download do GIF e salva no disco
    urllib.request.urlretrieve(gif_url, gif_file_name)

# Solicita o nome do gif ao usuário
#gif_name = input("Digite o nome do gif: ")

# def download_nltk_resources():
#     nltk.download('punkt')
#     nltk.download('averaged_perceptron_tagger')
#     nltk.download('maxent_ne_chunker')
#     nltk.download('words')
#     nltk.download('stopwords')
#     nltk.download('vader_lexicon')

def capture_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #recognizer.adjust_for_ambient_noise(source)
        print("Diga algo...")
        audio = r.listen(source)
    return audio
    #reconhecer mic
    # cap = pyaudio.PyAudio()
    # stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000,input=True, frames_per_buffer=8192)
    # stream.start_stream
    # audio = stream.read(16000)
    # #print(audio)
    # return audio

def process_audio(audio):
    r = sr.Recognizer()
    try:
        text = r.recognize_google(audio, language="pt-BR")
        text2 = text.split()
        if len(text2) > 5:
            text = text2[-5:]  # Retorna as últimas 5 palavras
            text = ' '.join(text)
        return text
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o áudio.")
    except sr.RequestError as e:
        print("Erro durante a solicitação ao serviço de reconhecimento de fala: {0}".format(e))
    return ""
    # recognizer.AcceptWaveform(audio)
    # result = recognizer.Result()
    # result_dict = json.loads(result)
    # text = result_dict.get("text")
    # return text

def preprocess_text(text):
    treated_text = text.lower()
    stop_words = set(stopwords.words("portuguese"))
    treated_text = " ".join([word for word in treated_text.split() if word.isalpha() and word not in stop_words])
    return treated_text

def extract_main_sentence(text):
    sentences = sent_tokenize(text, language='portuguese')
    if sentences:
        return sentences[0]
    else:
        return "Aguardando"

def extract_main_word(text):
    tagged_words = pos_tag(word_tokenize(text))
    main_word = ""
    for word, tag in tagged_words:
        if tag.startswith("N"):
            main_word = word
            break
    if not main_word:
        main_word2 = tagged_words[0][0] if tagged_words else "N/A"
    return main_word

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores

def main():

    # Download dos recursos do NLTK
    #download_nltk_resources()
    # Captura de áudio
    audio = capture_audio()
    
    # Processamento do áudio
    text = process_audio(audio)
    
    # Tratamento da frase
    #treated_text = preprocess_text(text)

    main_sentence = extract_main_sentence(text)
    
        
    # Extração da palavra principal
    main_word = extract_main_word(text)

    # Análise de sentimento
    #sentiment_scores = analyze_sentiment(text)
    
    # Exibição dos resultado
    
# Realiza a busca e reprodução do gif
    search_and_download_gif(main_sentence)
    #print("Análise de sentimento:", sentiment_scores),
    print("Principal sentença:", main_sentence)
    print("Frase capturada:", text)
    print("Palavra principal:", main_word)

if __name__ == "__main__":
    main()

# Função para agendar a execução da função main() a cada 30 segundos
def schedule_job():
    schedule.every(1).seconds.do(main)

# Agendar o job inicial
schedule_job()

# Loop para manter o programa em execução
while True:
    schedule.run_pending()
    time.sleep(1)

