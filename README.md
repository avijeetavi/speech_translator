# speech_translator
This code is used for speech translation from english to any language which is supported in https://en.wikipedia.org/wiki/ISO_639-1
       Examples: (e.g. en, ja, ko, pt, zh, zh-TW, ...)
This code capture english speech for 5 Seconds. It is configurable. One has to  just change the value of DURATION.
It takes speech as first input. and language code(as defined in https://en.wikipedia.org/wiki/ISO_639-1) as second input.
Using speech_recognition, speech gets converted in to text
Tranlator package is used to translate the text based on the second input
Once translation complets, that translated text will be save in a .mp3 file(in this code: FILE_NAME is translated_file.mp3) with the help of gTTS package.
Lastly with the help of playsound package, translated_file.mp3 will be played back.
