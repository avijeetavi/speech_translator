import os
import time

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from translate import Translator

FILE_NAME = 'translated_file.mp3'
DURATION = 5
'''
This code is used for speech translation from english to any language which is supported in https://en.wikipedia.org/wiki/ISO_639-1
       Examples: (e.g. en, ja, ko, pt, zh, zh-TW, ...)
This code capture english speech for 5 Seconds. It is configurable. One has to  just change the value of DURATION.
It takes speech as first input. and language code(as defined in https://en.wikipedia.org/wiki/ISO_639-1) as second input.
Using speech_recognition, speech gets converted in to text
Tranlator package is used to translate the text based on the second input
Once translation complets, that translated text will be save in a .mp3 file(in this code: FILE_NAME is translated_file.mp3) with the help of gTTS package
Lastly with the help of playsound package, translated_file.mp3 will be played back.
'''

def save_text_in_mp3(translated_word, lan):
    '''
    This funciton save the translated word in mp3 format
    :param translated_word: The word which got transalated
    :param lan: Language in which the translation is done
    :return: None
    '''
    mytext = translated_word
    myobj = gTTS(text=mytext, lang=lan, slow=False)
    myobj.save(FILE_NAME)
    #os.system("mpg321 translated_file.mp3")

def play_text_as_audio():
    '''
    This function play the .mp3 file
    :param: None
    :return: None
    '''
    playsound(FILE_NAME)
    time.sleep(0.10)
    os.remove(FILE_NAME)


def trans(word, lan):
    '''
    This function translate the word in any language
    :param word: Text word as input
    :param lan: Language in which translation is required: It supports all ISO_639-1_codes fomat: URL: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    :return: translated_word
    '''
    translated_word = Translator(to_lang=lan).translate(word)
    print(f'translate text: {translated_word}')
    return translated_word


def speech_recognisation():
    '''
    Speech recognisaiton function which is handled by  Google Speech Recognition API.
    :return: text and language in which translation is required
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print('Start speaking')
        audio_data = r.record(source, duration=DURATION)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        lan = input('Enter the language code in which translator is required: ')
        return text, lan

def main():
    text, language = speech_recognisation()
    translate_word = trans(text, language)
    save_text_in_mp3(translate_word, language)
    play_text_as_audio()

if __name__ == '__main__':
    main()