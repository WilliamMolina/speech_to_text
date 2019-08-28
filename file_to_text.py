import speech_recognition as sr

# obtain path to "audio.wav" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio.wav")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Google Speech Recognition
try:
    print("el audio dice: \"{}\"".format(r.recognize_google(audio, language='es-ES')))
except sr.UnknownValueError:
    print("Google Speech Recognition no puede entender el audio")
except sr.RequestError as e:
    print("no se puede obtener la petición del servicio de Google Speech Recognition {0}".format(e))
