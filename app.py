from flask import Flask, render_template, request, session, redirect
from datetime import timedelta
import mysql.connector

app = Flask(__name__)

#*** SESSION用初期設定
app.secret_key = 'IH12xPY24_No08'
app.permanent_session_lifetime = timedelta(minutes=3)
dataf = "backup.csv"

def con_db():
    con = mysql.connector.connect(
        host='localhost',
        user='py24user',
        passwd='py24pass',
        db='py24db'
    )
    return con

def lunch_sel(sql, params=()):
    con = con_db()
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql, params)
    result = cursor.fetchall()
    con.close()
    return result

#****************************************************
# SESSIONログイン状況
#****************************************************
def session_ck(tbl):
    if not tbl:
        return {"admn": "", "usname": "ゲスト"}
    
    admn = tbl["admn"]  #*** 管理者モード
    usname = tbl["usname"]  #*** ユーザー名
    if admn == "a":
        usname += "（管理者）"
    
    return {"admn": admn, "usname": usname}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cars')
def cars():
    return render_template('cars.html')

@app.route('/match')
def match():
    return render_template('match1.html')
#****************************************************
# ログイン画面表示 （'/login'）
#****************************************************
@app.route('/login', methods=["GET"])
def login():
    rec = {}
    etbl = {}
    return render_template('login.html', rec=rec, etbl=etbl)

#****************************************************
# ログイン処理 （'/loginck'）
#****************************************************
@app.route('/loginck', methods=["POST"])
def loginck():
    etbl = {}
    rec = request.form
    userid = request.form.get("userid", "").strip()
    userps = request.form.get("userps", "").strip()

    #*** 空白・未入力チェック ***
    ecnt = 0
    if not userid:
        etbl["userid"] = "ユーザーIDが入力されていません"
        ecnt += 1
    if not userps:
        etbl["userps"] = "パスワードが入力されていません"
        ecnt += 1

    #*** エラー判定 ***
    if ecnt != 0:
        return render_template('login.html', rec=rec, etbl=etbl)

    #*** ログイン認証（SQLインジェクション対策済み）***
    sql = "SELECT * FROM user WHERE userid = %s AND userps = %s;"
    tbl = lunch_sel(sql, (userid, userps))

    if len(tbl) == 0:
        etbl["userid"] = "ユーザーIDまたはパスワードが違います"
        return render_template('login.html', rec=rec, etbl=etbl)

    #*** session保存 ***
    session["admn"] = tbl[0]["admn"]
    session["usname"] = tbl[0]["usname"]
    return redirect('/')

#****************************************************
# ログアウト処理 （'/logout'）
#****************************************************
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
