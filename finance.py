from bs4 import BeautifulSoup
import urllib.request as req

def get_finance(brand):
    if brand == 'アメリカドル':
        # HTML取得
        url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy"
        res = req.urlopen(url)

        # HTML解析
        soup = BeautifulSoup(res, "html.parser")

        # 任意のデータを抽出
        price = soup.select_one(".stoksPrice").string
        response = '1米ドル' + price + '円です。\n\nレート検索を終了する場合は終了を、他の銘柄を調べる場合は他の銘柄を入力して話しかけてください。\n\n' \
                                    '対応可能銘柄：アメリカドル, ユーロ, オーストラリアドル, ニュージーランドドル, ポンド'
        return response

    elif brand == 'ユーロ':
        # HTML取得
        url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=eurjpy"
        res = req.urlopen(url)

        # HTML解析
        soup = BeautifulSoup(res, "html.parser")

        # 任意のデータを抽出
        price = soup.select_one(".stoksPrice").string
        response = '1ユーロ' + price + '円です。\n\nレート検索を終了する場合は終了を、他の銘柄を調べる場合は他の銘柄を入力して話しかけてください。\n\n' \
                                    '対応可能銘柄：アメリカドル, ユーロ, オーストラリアドル, ニュージーランドドル, ポンド'
        return response

    elif brand == 'オーストラリアドル':
        # HTML登録
        url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=audjpy"
        res = req.urlopen(url)

        # HTML解析
        soup = BeautifulSoup(res, "html.parser")

        # 任意のデータを抽出
        price = soup.select_one(".stoksPrice").string
        response = '1オーストラリアドル' + price + '円です。\n\nレート検索を終了する場合は終了を、他の銘柄を調べる場合は他の銘柄を入力して話しかけてください。\n\n' \
                                    '対応可能銘柄：アメリカドル, ユーロ, オーストラリアドル, ニュージーランドドル, ポンド'
        return response

    elif brand == 'ニュージーランドドル':
        # HTML登録
        url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=nzdjpy"
        res = req.urlopen(url)

        # HTML解析
        soup = BeautifulSoup(res, "html.parser")

        # 任意のデータを抽出
        price = soup.select_one(".stoksPrice").string
        response = '1ニュージーランドドル' + price + '円です。\n\nレート検索を終了する場合は終了を、他の銘柄を調べる場合は他の銘柄を入力して話しかけてください。\n\n' \
                                    '対応可能銘柄：アメリカドル, ユーロ, オーストラリアドル, ニュージーランドドル, ポンド'
        return response

    elif brand == 'ポンド':
        # HTML登録
        url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=gbpjpy"
        res = req.urlopen(url)

        # HTML解析
        soup = BeautifulSoup(res, "html.parser")

        # 任意のデータを抽出
        price = soup.select_one(".stoksPrice").string
        response = '1英ポンド' + price + '円です。\n\nレート検索を終了する場合は終了を、他の銘柄を調べる場合は他の銘柄を入力して話しかけてください。\n\n' \
                                    '対応可能銘柄：アメリカドル, ユーロ, オーストラリアドル, ニュージーランドドル, ポンド'
        return response
