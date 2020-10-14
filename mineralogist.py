import requests
import webbrowser

def search_minerals(search):
    webbrowser.open('http://www.museum.kyushu-u.ac.jp/specimen/kouhyouhon/engref.html')
    response = '九州大学の鉱物リストにアクセスしました。詳細はこちらから検索をお願いします。'
    return response

def buy_stones(shop):
    if shop == 'アマゾン':
        webbrowser.open('https://amazon.co.jp')
        response = 'アマゾンにアクセスしました。引き続きお買い物をお楽しみください。\n\n' \
                   'ショッピングを継続する場合は店舗名を、ショッピングを終了する場合はリセットを入力してください。\n\n' \
                   '対応可能サイト：アマゾン, 楽天, 東昇天然石, ストーンキャッスル'
        return response
    elif shop == '楽天':
        webbrowser.open('https://rakuten.co.jp')
        response = '楽天にアクセスしました。引き続きお買い物をお楽しみください。\n\n' \
                   'ショッピングを継続する場合は店舗名を、ショッピングを終了する場合はリセットを入力してください。\n\n' \
                   '対応可能サイト：アマゾン, 楽天, 東昇天然石, ストーンキャッスル'
        return response
    elif shop == '東昇天然石':
        webbrowser.open('https://shopping.geocities.jp/tosho-stones/')
        response = '東昇天然石にアクセスしました。引き続きお買い物をお楽しみください。\n\n' \
                   'ショッピングを継続する場合は店舗名を、ショッピングを終了する場合はリセットを入力してください。\n\n' \
                   '対応可能サイト：アマゾン, 楽天, 東昇天然石, ストーンキャッスル'
        return response
    elif shop == 'ストーンキャッスル':
        webbrowser.open('http://www.stone-castle.com/')
        response = 'ストーンキャッスルにアクセスしました。引き続きお買い物をお楽しみください。\n\n' \
                   'ショッピングを継続する場合は店舗名を、ショッピングを終了する場合はリセットを入力してください。\n\n' \
                   '対応可能サイト：アマゾン, 楽天, 東昇天然石, ストーンキャッスル'
        return response
    else:
        response = 'その店舗は登録されていません。申し訳ありません。\n\n' \
                   'ショッピングを継続する場合は店舗名を、ショッピングを終了する場合はリセットを入力してください。\n\n' \
                   '対応可能サイト：アマゾン, 楽天, 東昇天然石, ストーンキャッスル'
        return response

def search_events(place):
    if place == '国内':
        webbrowser.open('https://www.tucson-gemshow.com/%E3%83%9F%E3%83%8D%E3%83%A9%E3%83%AB%E3%82%B7%E3%83%A7%E3%83%BC-2020-%E3%82%B9%E3%82%B1%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB-%E5%9B%BD%E5%86%85%E7%89%88/')
        response = '今月開催中の国内のミネラルショーのイベント情報を表示しました。詳細は展開されたブラウザからご確認ください。\n' \
                   '海外の情報を知りたい場合は海外と入力し話しかけてください。検索を終了する場合リセットと入力し話しかけてください。'
        return response
    elif place == '海外':
        webbrowser.open('https://www.tucson-gemshow.com/%E3%83%9F%E3%83%8D%E3%83%A9%E3%83%AB%E3%82%B7%E3%83%A7%E3%83%BC-2020-%E3%82%B9%E3%82%B1%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB-%E6%B5%B7%E5%A4%96%E7%89%88/')
        response = '今月開催中の海外のミネラルショーのイベント情報を表示しました。詳細は展開されたブラウザからご確認ください。\n' \
                   '国内の情報を知りたい場合は国内と入力し話しかけてください。検索を終了する場合リセットと入力し話しかけてください。'
        return response
    else:
        response = '国内または海外から選択してください。検索を終了する場合はリセットと入力し話しかけてください。'
        return response