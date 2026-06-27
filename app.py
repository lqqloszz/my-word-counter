import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    count = 0
    seconds = 0
    speed = 'normal'
    text_count = ""

    if request.method == 'POST':
        text_content = request.form.get('text_input', '')
        speed = request.form.get('speed', 'normal')

        #計算總字數 (包含標點符號，因為網紅讀稿時標點符號也是時間成本)
        count = len(text_content)

        if count > 0:
            #依據海外/台灣自媒體大數據統計的華語口播語速計算 (每秒可念字數)
            if speed == 'fast':
                words_per_second = 300 / 60 #5速嘴，300字/min = 5字/s
            elif speed == 'slow':
                words_per_second = 150 / 60 #緩速，150字/min = 2.5字/s
            else:
                words_per_second = 220 / 60 #正常，220字/min = 3.66字/s

            #計算總秒數，四捨五入到小數點第一位
            seconds = round(count / words_per_second, 1)

    return render_template('index.html', count = count, seconds = seconds, speed = speed, text_content = text_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
