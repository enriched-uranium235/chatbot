import webbrowser

def browser_open(address):
    if address == 'アマゾン':
        url = "amazon.co.jp"
        webbrowser.open(url)
        response = 'アマゾン公式サイトに移動します。'
        return response
    elif address == '楽天':
        url = "rakuten.co.jp"
        webbrowser.open(url)
        response = '楽天公式サイトに移動します。'
        return response
    elif address == '法令データ提供システム':
        url = "https://elaws.e-gov.go.jp"
        webbrowser.open(url)
        response = '法務省e-ガバメントへ移動します。'
        return response
    elif address == '国税庁':
        url = "https://www.nta.go.jp/"
        webbrowser.open(url)
        response = '国税庁公式サイトへ移動します。'
        return response
    elif address == '総務省':
        url = "https://www.soumu.go.jp/"
        webbrowser.open(url)
        response = '総務省公式サイトへ移動します。'
        return response
    elif address == '厚労省':
        url = "https://www.mhlw.go.jp/index.html"
        webbrowser.open(url)
        response = '厚労省トップページに移動します。'
        return response
    elif address == '法務省':
        url = "http://www.moj.go.jp/"
        webbrowser.open(url)
        response = '法務省トップページに移動します。'
        return response
    else:
        response = 'そのキーワードは登録されていません。'
        return response
