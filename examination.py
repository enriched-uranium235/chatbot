from pykakasi import kakasi

kakasi = kakasi()

def jp_to_romen(text):
    kakasi.setMode('H', 'a')
    kakasi.setMode('K', 'a')
    kakasi.setMode('J', 'a')
    conv = kakasi.getConverter()
    answer = conv.do(text)
    answer2 = answer.capitalize()
    return answer2