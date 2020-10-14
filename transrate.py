#日本語から英語への変換
from googletrans import Translator
translator = Translator()

#英語
def translate_ja_en(sentence):
    trans_sentence = translator.translate(sentence, dest='en', src='ja')
    return trans_sentence.text

#英語→日本語
def translate_en_ja(sentence):
    trans_sentence = translator.translate(sentence, dest='ja', src='en')
    return trans_sentence.text

#ラテン語
def translate_ja_la(sentence):
    trans_sentence = translator.translate(sentence, dest='la', src='ja')
    return trans_sentence.text

#フランス語
def translate_ja_fr(sentence):
    trans_sentence = translator.translate(sentence, dest='fr', src='ja')
    return trans_sentence.text

#ドイツ語
def translate_ja_de(sentence):
    trans_sentence = translator.translate(sentence, dest='de', src='ja')
    return trans_sentence.text

#イタリア語
def translate_ja_it(sentence):
    trans_sentence = translator.translate(sentence, dest='it', src='ja')
    return trans_sentence.text

#ロシア語
def translate_ja_ru(sentence):
    trans_sentence = translator.translate(sentence, dest='ru', src='ja')
    return trans_sentence.text

#韓国語
def translate_ja_ko(sentence):
    trans_sentence = translator.translate(sentence, dest='ko', src='ja')
    return trans_sentence.text

#ヘブライ語
def translate_ja_he(sentence):
    trans_sentence = translator.translate(sentence, dest='he', src='ja')
    return trans_sentence.text