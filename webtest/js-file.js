// 2 js_Python作成
/**
 * HTMLのフォームから値を取得、
 * id=addでボタンクリックで値をPythonに送る {
 * 
 * id=addイベントクリックで起動 {
 * 
 * フォームの要素を取得
 * 要素から値を取得する
 * result = js_addを非同期で呼び出し <- arg(setdata1,setdata2)
 * 
 * テキストエリアに表示する <- result
 * }
 * フォーカスが外れたときに発生 {
 * 
 * }
 * }
 * **/
addBtn = document.getElementById("add")
console.log(addBtn);
addBtn.addEventListener("click", async () => {
    intOne = document.getElementById("int1");
    intTwo = document.getElementById("int2");
    res = document.getElementById("res")
    if (intOne,intTwo == "") {
        alert("these form empty!! input form");
    }
    js_add = await eel.js_add(intOne.value,intTwo.value)();
    res.textContent += js_add + "\n";
    intOne.value = "";
    intTwo.value = "";
    console.log(js_add);
})