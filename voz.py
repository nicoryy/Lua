from time import sleep
from pygame import mixer
from gtts import gTTS
from mutagen.mp3 import MP3


def falar(fala, nome_arquivo='assistente'):

    # pygame.mixer.init(frequency=mp3.info.sample_rate)

    s = gTTS(f"{fala}", lang='pt', tld='pt', slow=False)
    s.save(f'{nome_arquivo}.mp3')
    audio = MP3(f"{nome_arquivo}.mp3")
    tempo = audio.info.length
    tempo = round(tempo)
    try:
        mixer.init()
        mixer.music.load(f'{nome_arquivo}.mp3')
    except:
        mixer.init()
        mixer.music.load(fR'C:\Users\pedro\Desktop\nicory\{nome_arquivo}.mp3')
    mixer.music.play()
    sleep(tempo)
    mixer.music.stop()
    mixer.quit()


if __name__ == '__main__':
    falar('abacaxi')
