# 二つのフォームから取得した値を合計する
import eel

eel.init("webtest")

@eel.expose
def js_add(setdata1,setdata2):
    return int(setdata1) + int(setdata2)


eel.start("index.html",mode="chrome",
        size=(500,500),
        host="localhost",
        port=8000,
        position=(0,0),
        )