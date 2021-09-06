"""
関数を生成するURL {
    pafyをインポート
    pafyオブイジェクト生成
    
    メタデータを作成{
        タイトル情報
        著者名
        音楽情報
    }
    URLを取得
    取得したURLをeel.music_urlで呼び出す <- url,metadata
}

"""

import eel
@eel.expose
def test():
    eel.test()

@eel.expose
def gererate_url(url):
    import pafy
    music = pafy.new(url)
    best = music.getbestaudio()
    print(best)
    metaData = {
        "title": music.title,
        "author":music.author,
        "thumb":music.thumb
    }
    url = best.url
    print("metadata<-",metaData)
    print("url<-",url)
    eel.music_url(url,metaData);# <-!!!