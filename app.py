from flask import Flask, render_template, request

#初始化 Flask 網頁工廠
app = Flask(__name__)

#語法解說:@app.route 告訴電腦，每當使用者來到網站首頁 ("/") 時，要執行下面的 home() 功能
#methods = ["GET", "POST"] 代表網頁允許 「開啟查看(GET)」與「按下按鈕傳送資料(POST)」
@app.route("/", methods = ["GET", "POST"])
def home():
    current_count = 0
    user_text = ""

    #語法解說:如果使用者按下了網頁上的「開始計算」按鈕(觸發 POST)
    if request.method == "POST":
        #抓取網頁上文字方塊(名稱叫 text_input)裡面的內容
        user_text = request.form.get("text_input", "")
        #用 python 內建的 len() 幫他計算文字總長度
        current_count = len(user_text)

    #把計算完的結果(count 和 text)打包，丟給前台的 HTML 畫面顯示出來
    return render_template("index.html", count = current_count, text = user_text)

#啟動網頁伺服器
if __name__ == "__main__":
    app.run(debug=True)