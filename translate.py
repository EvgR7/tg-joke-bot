from deep_translator import GoogleTranslator
import requests

def trans(text):
    answer = GoogleTranslator(source='auto', target="ru").translate(text)
    return answer


def get_def(word):
    try:
        base_url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
        data = requests.get(base_url)
        meanings = data.json()[0]['meanings']
        return meanings
    except:
        return 'Somthing goes wrong'

def to_dict(world):

    prim_dic = get_def(world)
    if prim_dic == 'Somthing goes wrong':
        return 'Somthing goes wrong'
    final = []

    for part in prim_dic:
        part_of_speach = part['partOfSpeech']
        definition = part['definitions'][0]['definition']
        final.append({'part':part_of_speach, 'defin':definition})
    return (final)

def str_to_word(some_str):
    final = []
    words = some_str.split()
    check = ['!', '?', '.', ':', ';', ',', '"',"'"]
    for word in words:
        word = word.strip()
        word = word.lower()
        for sign in check:
            word = word.replace(sign,'')
        final.append(word)
    return final

def dictionary(message):
    words = set(str_to_word(message))
    final = ''

    for word in words:
        final = final + word.upper() + '\n'
        dic = to_dict(word)
        if dic != 'Somthing goes wrong':
            for get_part_def in dic:
                final = final + get_part_def['part'] + ': ' + get_part_def['defin'] + '\n'
    return final


