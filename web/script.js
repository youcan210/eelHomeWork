/*
URLからプレイを始める {

}

*/

playLstBtn = document.getElementById("t_playlist");
playLstBtn.addEventListener("click", () => {
    // ユーザーからURLを取得
    url = document.getElementById("t_URL").value
    console.log(url);
    eel.gererate_url(url)();
})
eel.expose(test)
function test() {
    print("This is send from Python hello!!")
}
eel.expose(music_url)
function music_url(url,metaData) {
    // metadata
    thumb = document.getElementById("thumb_img").src = metaData.thumb;
    document.getElementById("music_name").innerHTML = metaData.title;
    document.getElementById("audSrc").setAttribute("src",url);
    console.log(thumb);

}
window.onload = appStart;