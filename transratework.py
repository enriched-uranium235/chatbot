#翻訳した内容を指定されたメモ帳に書き込むメソッドを作成(英語→日本語)
def save_en_jp(sentense):
    # ファイルへの書き込み
    with open('trans/trans_en-jp.txt', 'a', encoding='utf_8') as f:
        f.writelines(sentense + '\n\n')

#翻訳した内容を指定されたメモ帳に書き込むメソッドを作成(日本語→英語)
def save_jp_en(sentense):
    # ファイルへの書き込み
    with open('trans/trans_jp-en.txt', 'a', encoding='utf_8')as f:
        f.writelines(sentense + '\n\n')

#音声入力の内容を記録する
def save_record(sentense):
    # ファイルへの書き込み
    with open('records/records.txt', 'a', encoding='utf_8')as f:
        f.writelines(sentense + '\n\n')

