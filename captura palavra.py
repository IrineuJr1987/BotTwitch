from vosk import Model, KaldiRecognizer
import pyaudio

model = Model(r'G:\Meu Drive\Programacao\auto\Chatgpt\Vosk pt-br')
recognizer = KaldiRecognizer(model, 16000)

#reconhecer mic
cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000,input=True, frames_per_buffer=8192)
stream.start_stream

while True:
    data = stream.read(16000)
    #print("Diga a mensagem:")
    if recognizer.AcceptWaveform(data):
        #print(recognizer.Result())
        
        mensagem = recognizer.Result()
        #mensagem.lower()
        print(mensagem)