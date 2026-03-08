from deep_translator import GoogleTranslator

def trans(text):
    answer = GoogleTranslator(source='auto', target="ru").translate(text)
    return answer

