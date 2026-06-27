import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # 🌟 核心關鍵：先在最外層建立變數的「預設初始值」
    # 這樣一來，網頁第一次載入 (GET) 時，這些變數就存在了，不會報錯！
    count = 0
    seconds = 0
    speed = 'normal'
    text_content = ""
    
    if request.method == 'POST':
        # 當使用者點擊按鈕送出表單時，才去蓋掉上面的預設值
        text_content = request.form.get('text_input', '')
        speed = request.form.get('speed', 'normal')
        count = len(text_content)
        
        if count > 0:
            if speed == 'fast':
                words_per_second = 300 / 60  # 快嘴：每秒 5 字
            elif speed == 'slow':
                words_per_second = 150 / 60  # 慢速：每秒 2.5 字
            else:
                words_per_second = 220 / 60  # 正常：每秒 3.66 字
                
            seconds = round(count / words_per_second, 1)
            
    # 不管是 GET 還是 POST，這裡的變數都 100% 存在，絕對不會觸發 UnboundLocalError
    return render_template('index.html', count=count, seconds=seconds, speed=speed, text_content=text_content)

if __name__ == '__main__':
    # 讓 Render 可以動態綁定 Port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
