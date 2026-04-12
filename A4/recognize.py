# Installation:
#  Make sure we have up-to-date versions of pip, setuptools and wheel
# In CMD: 
# python -m pip install --upgrade pip setuptools wheel
# pip install --upgrade pocketsphinx
# 
# If you will use PyCharm install pocketsphinx for you venv

import os
from pocketsphinx import AudioFile, get_model_path

model_path = get_model_path()

config = {
    'verbose': False,
    'audio_file': 'A4\\Al_page_13_78_16k.wav',
    'hmm': get_model_path('en-us'),
    'lm': get_model_path('en-us.lm.bin'),
    'dict': get_model_path('cmudict-en-us.dict')
}

audio = AudioFile(**config)
# Frames per Second
fps = 100
for phrase in audio:
    print(phrase)

    print('-' * 28)
    print('| %5s |  %3s  |   %4s   |' % ('start', 'end', 'word'))
    print('-' * 28)
    for s in phrase.seg():
        print('| %4ss | %4ss | %8s |' % (s.start_frame / fps, s.end_frame / fps, s.word))
    print('-' * 28)
