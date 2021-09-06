"""
eel インポート
eel 画面表示

YouTubeの情報取得 <- API
アプリケーションを終了する {
    
    コマンドラインから情報を入力する
}

"""
import eel
import main

eel.init("web")

# eelが二つの引数を返しているので、関数を取り持つための引数がいる
# @eel.expose
# def handle_exit(ar1,ar2):
#     import sys
#     sys.exit(0)# 終了

if __name__ == "__main__":
    size= (1000,600)
    app_opt = {
        "mode":"chrome",
        # "close_callback":handle_exit
    }
    eel.start("index.html",options=app_opt,size=size,suppress_error=True)