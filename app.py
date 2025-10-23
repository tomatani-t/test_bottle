import bottle

html = '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>Bottle</title>
</head>
<body>
<br><h2>入力情報</h2>
<h2>選択されたチェックボックスを取得する</h2>
<form action="/input" method="post">
<p>Input Date(1月-3月):<br><input type="date" name="indate" value="2025-01-04" min="2025-01-04" max="2025-03-28" ></p>
<p>Input Number(1-10):<br><input type="number" name="innumber" min="1" max="10"></p>
<p>Input Data(1-8桁　枠10):<br><input type="text" name="indata" required minlength="1" maxlength="8" size="10"></p>
<p>Input Password(最小4桁):<br><input type="password" name="inpassword" minlength="4" required ></p>
<p><input type="submit" value="Input Dtata"></p>
</form>
<br><br><h2>状況</h2>
{b}
</body>
</html>
'''

@bottle.route('/')
def index():
    return html.format(b = '')

@bottle.route('/input', method='post')
def sel_chk():
    date = bottle.request.forms.getunicode('indate')
    number = bottle.request.forms.getunicode('innumber')
    data = bottle.request.forms.getunicode('indata')
    password = bottle.request.forms.getunicode('inpassword')
    return html.format(b=f'結果：Date={date}_number={number}_data={data}_password={password}')

# HTTPサーバの起動
bottle.run(host='localhost', port=8000)

