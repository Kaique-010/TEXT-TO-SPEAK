from gtts import gTTS
from playsound import playsound

# Texto que será convertido em fala
texto = "Tenho o prazer de lhes apresentar a nossa ferramenta lalalalalallalalalalalalalallaalalalallalalalalalalalalalal"

# Escolher o idioma (por exemplo, 'pt' para português, 'en' para inglês)
tts = gTTS(text=texto, lang='pt', slow=False)

# Salva o áudio em um arquivo temporário
tts.save("fala.mp3")

# Reproduz o áudio
playsound("fala.mp3")