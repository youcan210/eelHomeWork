import eel
import desktop
import search
import __main__

app_name="web"
end_point="index.html"
size=(700,600)

@ eel.expose
def kimetsu_search(word,csv_name):
    search.kimetsu_search(word,csv_name)
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)