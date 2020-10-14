from datetime import datetime
import tkinter as tk
import tkinter.messagebox
import numpy as np
import speech_recognition as sr
from ariya import *
from is_weather import *
from wiki_search import wikipediaSearch
from finance import get_finance
from browser_open import browser_open
from mineralogist import *
from transrate import *
from transratework import *
from PIL import Image, ImageTk

""" グローバル変数の定義
"""
entry = None            # 入力エリアのオブジェクトを保持
response_area = None    # 応答エリアのオブジェクトを保持
response_area2 = None   # 応答エリア2のオブジェクトを保持
lb = None               # ログ表示用リストボックスを保持
action = None           # 'オプション'メニューの状態を保持
ariya = Ptna('ariya')     # Ariyaオブジェクトを保持
on_canvas = None        # Canvasオブジェクトを保持
ptyna_images = []       # イメージを保持
log = []                # インプット文字列を保持
question = 0
r = sr.Recognizer()
mic = sr.Microphone()

def putlog(str):
    """ 対話ログをリストボックスに追加する関数
        @str  入力文字列または応答メッセージ
    """
    lb.insert(tk.END, str)
    # インプットと応答をリストlogに追加
    log.append(str + '\n')

def prompt():
    """ アリアのプロンプトを作る関数
    """
    p = ariya.name
    if (action.get())==0:
        p += '：' + ariya.responder.name
    return p + '> '


def chagImg(img):
    """ 画像をセットする関数
    """
    canvas.itemconfig(
        on_canvas,
        image = ptyna_images[img]      # 表示するイメージを変更
    )

def change_looks():
    em =ariya.emotion.mood
    if -5 <= em <= 5:
        chagImg(0)
    elif -10 <= em < -5:
        chagImg(1)
    elif -15 <= em < -10:
        chagImg(2)
    elif 5 <= em <= 15:
        chagImg(3)


def talk():
    """ 対話を行う関数
        ・Ptnaクラスのdialogue()を実行して応答メッセージを取得
        ・入力文字列および応答メッセージをログに出力
    """
    global question
    global picture
    global img

    value = entry.get()    
    # 入力エリアが未入力の場合
    if not value:
        flag = np.random.randint(0,3)
        if flag == 1:
            response_area.configure(text='はい?')
        elif flag == 2:
            response_area.configure(text='音声入力のボタンを押して話しかけると聞き取った内容をログボックスに表示します。')
        else:
            response_area.configure(text='「機能説明」と入力し「話す」を押すと現在実装済みの機能が表示されます。')
    elif value == '機能説明':
        response_area.configure(text='現在実装されている機能は下記のとおりです。\n'
                                     'チャット会話, 天気予報1(入力ワード:今日の天気)\n'
                                     '天気予報2(入力ワード:明日の天気), wikipedia検索(入力ワード:ウィキ)\n'
                                     '為替レート検索(入力ワード:為替レート), ブラウザ展開(入力ワード:ブラウザ展開)\n'
                                     '石関連(入力ワード:石野郎), 文章翻訳(入力ワード：翻訳)\n'
                                     'フリーランス業務用翻訳(入力ワード:フリーランス翻訳), \n'
                                     '画像表示(入力ワード:画像切り替え)')
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '今日の天気':
        if question == 0:
            response_area.configure(text='どこの天気ですか？下記形式に沿って入力して話しかけてください。\n'
                                         '例：Tokyo')
            question = 1
            # 入力エリアをクリア
            entry.delete(0, tk.END)
    elif question ==1:
        response = is_weather(value)
        response_area.configure(text=value + 'の天気は、\n'
                             + response + 'です。')
        question = 0
        # 入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == 'ウィキ':
        if question == 0:
            response_area.configure(text='何を調べますか？')
            question = 2
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 2:
        response = wikipediaSearch(value)
        response_area.configure(text=response + '\n\n検索終了と入力するとウィキ検索機能を終了します。')
        if value == '検索終了':
            response_area.configure(text='ウィキ検索機能を終了しチャット会話に戻ります。')
            question = 0
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '為替レート':
        if question == 0:
            response_area.configure(text='どの銘柄ですか？対応可能なのは、\n'
                                         'アメリカドル/日本円\n'
                                         'ユーロ/日本円\n'
                                         'オーストラリアドル/日本円\n'
                                         'ニュージーランドドル/日本円\n'
                                         'ポンド/日本円　です。\n'
                                         '調べたい通貨を入力して話しかけてください。(アメリカドル等)'
                                    )
            question = 3
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 3:
        response = get_finance(value)
        response_area.configure(text=response)
        if value == '終了':
            response_area.configure(text='レート検索を終了します。')
            question = 0
        #入力エリアをクリア
        entry.delete(0, tk.END)
    # 入力されていたら対話オブジェクトを実行
    elif value == 'ブラウザ展開':
        if question == 0:
            response_area.configure(text='検索ワードを入力してください。\n'
                                         '実装済みワード：アマゾン , 楽天 , 法令データ提供システム, 国税庁, 総務省, 厚労省, 法務省')
            question = 4
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 4:
        response = browser_open(value)
        response_area.configure(text=response)
        question = 0
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '石野郎':
        if question == 0:
            response_area.configure(text='何を行いますか？下記内容のいずれかを入力し話すを押してください。\n'
                                         '石の名前を調べる, 石を買う, ミネラルショーのイベント情報')
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif value == '石の名前を調べる':
        if question == 0:
            response = search_minerals(value)
            response_area.configure(text=response)
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif value == '石を買う':
        if question == 0:
            response_area.configure(text='ネットでの石のお買い求めは\n'
                                         'アマゾン, 楽天, 東昇天然石, ストーンキャッスル\n'
                                         'にアクセスできます。アクセスしたいサイト名を入力し話しかけてください。')
            question = 5
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 5:
        response = buy_stones(value)
        response_area.configure(text=response)
        if value == 'リセット':
            response_area.configure(text='店舗検索を終了します。')
            question = 0
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == 'ミネラルショーのイベント情報':
        if question == 0:
            response_area.configure(text='国内と海外のどちらを調べますか？')
            question = 6
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 6:
        response = search_events(value)
        response_area.configure(text=response)
        if value == 'リセット':
            response_area.configure(text='イベント検索を終了します。')
            question = 0
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '翻訳':
        if question == 0:
            response_area.configure(text='現在下記の言語の翻訳に対応しています。下記形式に沿って翻訳したい言語を入力し話しかけてください。\n'
                                         '例：日本語→英語\n'
                                         '対応言語：日本語→英語, 日本語→ラテン語, 日本語→フランス語\n'
                                         '日本語→ドイツ語, 日本語→イタリア語, 日本語→ロシア語\n'
                                         '日本語→韓国語, 日本語→ヘブライ語, 英語→日本語')
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif value == '日本語→英語':
        if question == 0:
            response_area.configure(text='翻訳したい文章を入力して話しかけてください。')
            question = 7
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 7:
        response = translate_ja_en(value)
        response_area.configure(text=response + '\n\n翻訳を終了する場合リセットと入力し話しかけてください。')
        if value == 'リセット':
            response_area.configure(text='翻訳を終了しチャット会話に戻ります。')
            question = 0
        else:
            # ログを残す
            # 入力文字列引数にしてputlog()を呼ぶ
            putlog('> ' + value)
            # 応答メッセージを引数にしてputlog()を呼ぶ
            putlog('ariya> ' + response)
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '日本語→ラテン語':
        if question == 0:
            response_area.configure(text='翻訳したい文章を入力して話しかけてください。')
            question = 8
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 8:
        response = translate_ja_la(value)
        response_area.configure(text=response + '\n\n翻訳を終了する場合リセットと入力し話しかけてください。')
        if value == 'リセット':
            response_area.configure(text='翻訳を終了しチャット会話に戻ります。')
            question = 0
        else:
            # ログを残す
            # 入力文字列引数にしてputlog()を呼ぶ
            putlog('> ' + value)
            # 応答メッセージを引数にしてputlog()を呼ぶ
            putlog('ariya> ' + response)
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '日本語→フランス語':
        if question == 0:
            response_area.configure(text='翻訳したい文章を入力して話しかけてください。')
            question = 9
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 9:
        response = translate_ja_fr(value)
        response_area.configure(text=response + '\n\n翻訳を終了する場合リセットと入力し話しかけてください。')
        if value == 'リセット':
            response_area.configure(text='翻訳を終了しチャット会話に戻ります。')
            question = 0
        else:
            # ログを残す
            # 入力文字列引数にしてputlog()を呼ぶ
            putlog('> ' + value)
            # 応答メッセージを引数にしてputlog()を呼ぶ
            putlog('ariya> ' + response)
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '日本語→ドイツ語':
        if question == 0:
            response_area.configure(text='翻訳したい文章を入力して話しかけてください。')
            question = 10
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 10:
        response = translate_ja_de(value)
        response_area.configure(text=response + '\n\n翻訳を終了する場合リセットと入力し話しかけてください。')
        if value == 'リセット':
            response_area.configure(text='翻訳を終了しチャット会話に戻ります。')
            question = 0
        else:
            # ログを残す
            # 入力文字列引数にしてputlog()を呼ぶ
            putlog('> ' + value)
            # 応答メッセージを引数にしてputlog()を呼ぶ
            putlog('aliya> ' + response)
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '日本語→イタリア語':
        if question == 0:
            response_area.configure(text='翻訳したい文章を入力して話しかけてください。')
            question = 11
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 11:
        response = translate_ja_it(value)
        response_area.configure(text=response + '\n\n翻訳を終了する場合リセットと入力し話しかけてください。')
        if value == 'リセット':
            response_area.configure(text='翻訳を終了しチャット会話に戻ります。')
            question = 0
        else:
            # ログを残す
            # 入力文字列引数にしてputlog()を呼ぶ
            putlog('> ' + value)
            # 応答メッセージを引数にしてputlog()を呼ぶ
            putlog('ariya> ' + response)
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '日本語→ロシア語':
        if question == 0:
            response_area.configure(text='翻訳したい文章を入力して話しかけてください。')
            question = 12
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 12:
        response = translate_ja_ru(value)
        response_area.configure(text=response + '\n\n翻訳を終了する場合リセットと入力し話しかけてください。')
        if value == 'リセット':
            response_area.configure(text='翻訳を終了しチャット会話に戻ります。')
            question = 0
        else:
            # ログを残す
            # 入力文字列引数にしてputlog()を呼ぶ
            putlog('> ' + value)
            # 応答メッセージを引数にしてputlog()を呼ぶ
            putlog('ariya> ' + response)
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '日本語→韓国語':
        if question == 0:
            response_area.configure(text='翻訳したい文章を入力して話しかけてください。')
            question = 13
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 13:
        response = translate_ja_ko(value)
        response_area.configure(text=response + '\n\n翻訳を終了する場合リセットと入力し話しかけてください。')
        if value == 'リセット':
            response_area.configure(text='翻訳を終了しチャット会話に戻ります。')
            question = 0
        else:
            # ログを残す
            # 入力文字列引数にしてputlog()を呼ぶ
            putlog('> ' + value)
            # 応答メッセージを引数にしてputlog()を呼ぶ
            putlog('ariya> ' + response)
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '日本語→ヘブライ語':
        if question == 0:
            response_area.configure(text='翻訳したい文章を入力して話しかけてください。')
            question = 14
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 14:
        response = translate_ja_he(value)
        response_area.configure(text=response + '\n\n翻訳を終了する場合リセットと入力し話しかけてください。')
        if value == 'リセット':
            response_area.configure(text='翻訳を終了しチャット会話に戻ります。')
            question = 0
        else:
            # ログを残す
            # 入力文字列引数にしてputlog()を呼ぶ
            putlog('> ' + value)
            # 応答メッセージを引数にしてputlog()を呼ぶ
            putlog('ariya> ' + response)
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '英語→日本語':
        if question == 0:
            response_area.configure(text='翻訳したい文章を入力して話しかけてください。')
            question = 15
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 15:
        response = translate_en_ja(value)
        response_area.configure(text=response + '\n\n翻訳を終了する場合リセットと入力し話しかけてください。')
        if value == 'リセット':
            response_area.configure(text='翻訳を終了しチャット会話に戻ります。')
            question = 0
        else:
            # ログを残す
            # 入力文字列引数にしてputlog()を呼ぶ
            putlog('> ' + value)
            # 応答メッセージを引数にしてputlog()を呼ぶ
            putlog('ariya> ' + response)
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '明日の天気':
        if question == 0:
            response_area.configure(text='どこの天気ですか？下記形式に沿って入力し話しかけてください。\n例:Tokyo')
            question = 16
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 16:
        response = next_weather(value)
        response_area.configure(text=value + 'の天気は\n' + response + '　です。')
        question = 0
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == 'フリーランス翻訳':
        response_area.configure(text='現在対応可能なのは英語→日本語と日本語→英語です。\n'
                                     '英語→日本語の翻訳作業は和訳, 日本語→英語の翻訳作業は英訳と入力し話しかけてください。')
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '和訳':
        response_area.configure(text='和訳を開始します。翻訳する文章を入力し話しかけてください。')
        question = 17
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif question == 17:
        response = translate_en_ja(value)
        response_area.configure(text=response + '\n\n翻訳を終了する場合finishと入力し話しかけてください。')
        if value == 'finish':
            response_area.configure(text='翻訳を終了しチャット会話に戻ります。\n'
                                         '翻訳した内容はtransフォルダ内のtrans_en-jp.txtから確認し、\n'
                                         'Word, Excel等にコピペしてください。')
            question = 0
        else:
            save_en_jp(response)
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '英訳':
        response_area.configure(text='英訳を開始します。翻訳する文章を入力し話しかけてください。')
        question = 18
        #入力エリアをクリア
        entry.delete(0, tk.END)
    elif question == 18:
        response = translate_ja_en(value)
        response_area.configure(text=response + '\n\n翻訳を終了する場合終了と入力し話しかけてください。')
        if value == '終了':
            response_area.configure(text='翻訳を終了しチャット会話に戻ります。\n'
                                         '翻訳した内容はtransフォルダ内のtrans_jp-en.txtから確認し、\n'
                                         'Word, Excel等にコピペしてください。')
            question = 0
        else:
            save_jp_en(response)
        # 入力エリアをクリア
        entry.delete(0, tk.END)
    elif value == '画像切り替え':
        if question == 0:
            response_area.configure(text='私の右側に指定された画像を表示します。表示する画像ファイルを入力し話しかけてください。')
            question = 19
            #入力エリアをクリア
            entry.delete(0, tk.END)
    elif question == 19:
        if value == '終了。':
            response_area.configure(text='画像の切り替えを終了します。')
            question = 0
            #入力エリアをクリア
            entry.delete(0, tk.END)
        else:
            image_files = 'picture/' + value + '.jpg'
            try:
                response_area.configure(text='指定された画像を私の右側に表示しました。全画面表示にしてご確認ください。\n\n'
                                             '終了する場合は終了。と入力し話しかけてください。')
                img = Image.open(image_files)
                img = ImageTk.PhotoImage(img)
                response_area2.create_image(
                    0,
                    0,
                    image = img,
                    anchor = tk.NW
                )
            except:
                response_area.configure(text='指定された画像が見つかりませんでした。pictureフォルダ内にjpg形式の画像を追加してください。\n\n'
                                             '終了する場合は終了。と入力し話しかけてください。')
        #入力エリアをクリア
        entry.delete(0, tk.END)
    else:
        # 入力文字列を引数にしてdialogue()の結果を取得
        response = ariya.dialogue(value)
        # 応答メッセージを表示
        response_area.configure(text=response)
        # 入力文字列引数にしてputlog()を呼ぶ
        putlog('> ' + value)
        # 応答メッセージを引数にしてputlog()を呼ぶ
        putlog(prompt() + response)
        # 入力エリアをクリア
        entry.delete(0, tk.END)

    change_looks() #画像チェンジ

def catchSound():
    response_area.configure(text='話しかけてください。')

    with mic as source:
        r.adjust_for_ambient_noise(source)  # 雑音対策
        audio = r.listen(source)

    response_area.configure(text='聞き取った音声を処理しています...')

    try:
        response_area.configure(text='聞き取った内容をログボックスに表示しました。内容をコピーしてご活用ください。\n'
                                     'recordsフォルダのrecords.txtにも記録されますのでそちらもご利用ください。')
        # ログを残す
        # 入力文字列引数にしてputlog()を呼ぶ
        putlog(r.recognize_google(audio, language='ja-JP'))
        save_record(r.recognize_google(audio, language='ja-JP'))

    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        response_area.configure(text='音声を認識できませんでした。')
    except sr.RequestError as e:
        response_area.configure(text="グーグルスピーチではその音声を処理できません。; {0}".format(e))

def writeLog():
    """ ログファイルに辞書を更新した日時を記録
    """
    # ログを作成
    now = 'Ptna System Dialogue Log: ' + datetime.now().strftime(
                                   '%Y-%m-%d %H:%m::%S' + '\n')
    log.insert(0, now)
    # ログファイルへの書き込み
    with open('log.txt', 'a', encoding = 'utf_8') as f:
        f.writelines(log)

#=================================================
# 画面を描画する関数
#=================================================

def run():
    # グローバル変数を使用するための記述
    global entry, response_area, lb, action, canvas, on_canvas, ptyna_images, response_area2, image_files, on_area2, img

    # メインウィンドウを作成
    root = tk.Tk()
    # ウィンドウのサイズを設定
    root.geometry('880x560')
    # ウィンドウのタイトルを設定
    root.title('Intelligent Agent : ')
    # フォントの用意
    font=('Helevetica', 11)
    font_log=('Helevetica', 11)

    def callback():
        """ 終了時の処理
        """
        # メッセージボックスの[OK]ボタンクリック時の処理
        if tkinter.messagebox.askyesno(
            'Quit?', '辞書を更新してもいい?'):
            ariya.save() # 記憶メソッド実行
            writeLog()  # ログの保存
            root.destroy()
	# [キャンセル]ボタンクリック
        else:
            root.destroy()

    root.protocol('WM_DELETE_WINDOW', callback)

    # メニューバーの作成
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    #「ファイル」メニュー
    filemenu = tk.Menu(menubar)
    menubar.add_cascade(label='ファイル', menu=filemenu)
    filemenu.add_command(label='閉じる', command=callback)
    # 「オプション」メニュー
    action = tk.IntVar()
    optionmenu = tk.Menu(menubar)
    menubar.add_cascade(label='オプション', menu=optionmenu)
    optionmenu.add_radiobutton(
        label='Responderを表示',          # アイテム名
        variable = action,                # 選択時の値を格納するオブジェクト
        value = 0                         # actionの値を0にする
    )
    optionmenu.add_radiobutton(
        label='Responderを表示しない',    # アイテム名
        variable = action,                # 選択時の値を格納するオブジェクト
        value = 1                         # actionの値を0にする
    )

    
    # キャンバスの作成
    canvas = tk.Canvas(
                root,               # 親要素をメインウィンドウに設定
                width = 500,        # 幅を設定
                height = 500,       # 高さを設定
                relief=tk.RIDGE,    # 枠線を表示
                bd=2                # 枠線の幅を設定
             )
    canvas.place(x=370, y=0)                # メインウィンドウ上に配置
    
    # イメージを用意
    ptyna_images.append(tk.PhotoImage(file = "ariya_normal.gif"))
    ptyna_images.append(tk.PhotoImage(file = "ariya_talk.gif"))
    ptyna_images.append(tk.PhotoImage(file = "ariya_sad.gif"))
    ptyna_images.append(tk.PhotoImage(file = "ariya_laugh.gif"))

    # キャンバス上にイメージを配置
    on_canvas = canvas.create_image(
        0,                                  # x座標
        0,                                  # y座標
        image = ptyna_images[0],            # 配置するイメージを指定
        anchor = tk.NW,                     # 配置の起点となる位置を左上隅に指定
    )


    # 応答エリアを作成
    response_area = tk.Label(
                        root,               # 親要素をメインウィンドウに設定
                        width=63,           # 幅を設定
                        height=9,          # 高さを設定
                        bg='yellowgreen',        # 背景色を設定
                        font=font,          # フォントを設定
                        relief=tk.RIDGE,    # 枠線の種類を設定
                        bd=2,               # 枠線の幅を設定
                        justify=tk.LEFT,
                        wraplength=500
                    )
    response_area.place(x=370, y=370)       # メインウィンドウ上に配置

    #2つめの応答エリアを作成
    response_area2 = tk.Canvas(
        root,  # 親要素をメインウィンドウに設定
        width=500,  # 幅を設定
        height=500,  # 高さを設定
        bg='white', #背景色を設定
        relief=tk.RIDGE,  # 枠線の種類を設定
        bd=2,  # 枠線の幅を設定
    )
    response_area2.place(x=880, y=0)  # メインウィンドウ上に配置

    image_files = "picture/Python-Logo-PNG.png"

    img = Image.open(image_files)
    tkimg = ImageTk.PhotoImage(img)

    on_area2 = response_area2.create_image(
        0,
        0,
        image = tkimg,
        anchor = tk.NW
    )

    # フレームの作成
    frame = tk.Frame(
                root,               # 親要素はメインウィンドウ
                relief=tk.RIDGE,    # ボーダーの種類
                borderwidth = 4     # ボーダー幅を設定
            )
    # 入力ボックスの作成
    entry = tk.Entry(
                frame,              # 親要素はフレーム
                width=70,           # 幅を設定
                font=font           # フォントを設定
            )
    entry.pack(side = tk.LEFT)      # フレームに左詰めで配置する
    entry.focus_set()               # 入力ボックスにフォーカスを当てる

    # ボタン1の作成
    button = tk.Button(
                frame,              # 親要素はフレーム
                width=15,           # 幅を設定
                text='話す',        # ボタンに表示するテキスト
                command=talk        # クリック時にtalk()関数を呼ぶ
             )
    button.pack(side = tk.LEFT)     # フレームに左詰めで配置する
    frame.place(x=30, y=520)        # フレームを画面上に配置

    # ボタン2の作成
    button = tk.Button(
                frame,              # 親要素はフレーム
                width=15,           # 幅を設定
                text='音声入力',        # ボタンに表示するテキスト
                command=catchSound        # クリック時にcatchSound()関数を呼ぶ
             )
    button.pack(side = tk.LEFT)     # フレームに左詰めで配置する
    frame.place(x=30, y=530)        # フレームを画面上に配置

    # リストボックスを作成
    lb = tk.Listbox(
            root,                   # 親要素はフレーム
            width=42,               # 幅を設定
            height=30,              # 高さを設定
            font=font_log           # フォントを設定
         )
    # 縦のスクロールバーを生成
    sb1 = tk.Scrollbar(
            root,                   # 親要素はフレーム
            orient = tk.VERTICAL,   # 縦方向のスクロールバーにする
            command = lb.yview      # スクロール時にListboxのyview()メソッドを呼ぶ
      )
    # 横のスクロールバーを生成
    sb2 = tk.Scrollbar(
            root,                   # 親要素はフレーム
            orient = tk.HORIZONTAL, # 横方向のスクロールバーにする
            command = lb.xview      # スクロール時にListboxのxview()メソッドを呼ぶ
          )
    # リストボックスとスクロールバー1を連動させる
    lb.configure(yscrollcommand = sb1.set)
    lb.configure(xscrollcommand = sb2.set)
    # grid()でリストボックス、スクロールバーを画面上に配置
    lb.grid(row = 0, column = 0)
    sb1.grid(row = 0, column = 1, sticky = tk.NS)
    sb2.grid(row = 1, column = 0, sticky = tk.EW)

    # メインループ
    root.mainloop()


#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':
    run()
