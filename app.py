from flask import Flask, render_template, request, redirect, session, url_for
import mariadb  # ✅ MariaDB（MySQL 互换性あり）
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'IH12xPY24_No08'  # ✅ セッションのセキュリティキー
app.permanent_session_lifetime = timedelta(minutes=15)  # ✅ セッションの有効時間を3分に設定

type={"body_type":""}

# ****************************************************
# ** データベース接続関数 (DBに接続する) **
# ****************************************************
def con_db():
    try:
        print("🛠️ データベース接続を試みています...")
        conn = mariadb.connect(
            host="localhost",
            user="py24user",
            password="py24pass",
            database="carpling_db",

            port=3306  # ✅ MariaDBのデフォルトポート
        )
        print("✅ データベース接続成功！")
        return conn
    except mariadb.Error as err:
        print(f"❌ データベース接続失敗: {err}")
        return None  # 接続に失敗した場合は None を返す

# ****************************************************
# ** ホームページ ('/') **
# ****************************************************
@app.route('/')
def index():
    return render_template('index.html')  # ✅ `index.html` を表示（ログイン情報が表示される）

@app.route('/mypage')
def mypage():
    if not session:
        return render_template('index.html')
    else:
        return render_template('mypage.html')

@app.route('/match')
def match():
    return render_template('matchtop.html')

@app.route('/match_ages', methods=["POST"])
def match_ages():
    # type.clear()
    type["body_type"]=request.form.get("type")
    return render_template('match_ages.html',e_tbl={})

@app.route('/match_result', methods=["POST"])
def match_result():
    rec2=[]
    e_tbl={}
    count=0
    rec=request.form
    for key,value in rec:
        print(key,value)
        count=count+1

    gender = request.form.get("10")
    age = request.form.get("11")
    s1 = request.form.get("12")
    rec2.append(s1)
    s2 = request.form.get("13")
    rec2.append(s2)
    s3 = request.form.get("14")
    rec2.append(s3)
    s4 = request.form.get("15")
    rec2.append(s4)
    s5 = request.form.get("16")
    rec2.append(s5)

    print(rec2)
    for i in range (0,5):
        if not rec2[i]:
            print("NOT")
            tbl_key=str(i)
            e_tbl[tbl_key]="選択されていません"
    print(e_tbl)
        


    print(gender)

    if count==7:
        print("OK")
        print(type["body_type"])

        if type["body_type"]=="Celibate":
            body_select_sql="category = Celibate"
        elif type["body_type"]=="Family":
            body_select_sql="category = Family"
        elif type["body_type"]=="Luxury":
            body_select_sql="category = Luxury"

        if rec2[0]=="A-1":
            price_select_sql='max_price <= 2500000 '
        elif rec2[0]=="B-1":
            price_select_sql='max_price <= 4500000 '
        else:
            price_select_sql='max_price >= 4500000 '

        if rec2[1]=="A-2":
            fuel_select_sql='fuel_type == "ハイブリッド"'

        if rec2[2]=="A-3":
            capasity_select_sql='capasity >= "4"'
        elif rec2[2]=="C-3":
            capasity_select_sql='capasity >= "2"'
        
        if rec2[3]=="A-4":
            sport_select_sql='turbo == "yes"'
        elif rec2[3]=="A-4":
            sport_select_sql='turbo == "yes"'
        else:
            sport_select_sql='turbo == "N/A"'    

        conn = con_db()
        cursor = conn.cursor(dictionary=True)
        select_sql = 'SELECT * FROM cars WHERE "'
        select_dock_sql=" AND "
        select_dock2_sql=" OR "
        select_end_sql='"'
        sql=select_sql+body_select_sql+select_dock_sql+price_select_sql+select_dock_sql+fuel_select_sql+select_dock_sql+capasity_select_sql+select_end_sql
        print(sql)
        cursor.execute(sql)
        car_result = cursor.fetchall()
        print(car_result)

        return render_template('result.html')
    
    else:
        return render_template('match_ages.html',e_tbl=e_tbl)
#****************************************************
# ログイン画面表示 （'/login'）
#****************************************************



# ****************************************************
# ** ログインページ ('/login') **
# ****************************************************
@app.route('/login', methods=["GET"])
def login():
    session.clear()  # ✅ 過去のログイン情報をクリア
    return render_template('login.html', rec={}, etbl={})


# ****************************************************
# ** ログイン認証 ('/loginck') **
# ****************************************************
@app.route('/loginck', methods=["POST"])
def loginck():
    etbl = {}  # エラーメッセージを格納する辞書
    userid = request.form.get("userid", "").strip()  # ユーザーIDを取得・空白削除
    userps = request.form.get("userps", "").strip()  # パスワードを取得・空白削除

    print(f"📌 ユーザー入力: userid={userid}, userps={userps}")

    # ❌ ユーザーIDまたはパスワードが空の場合、エラーを表示
    if not userid:
        etbl["userid"] = "ユーザーIDが入力されていません"
    if not userps:
        etbl["userps"] = "パスワードが入力されていません"

    # ✅ 入力にエラーがある場合は、再度ログインページを表示
    if etbl:
        return render_template('login.html', rec={"userid": userid, "userps": userps}, etbl=etbl)

    # ✅ データベース接続
    conn = con_db()
    if not conn:
        etbl["userid"] = "データベースに接続できません"
        return render_template('login.html', rec={"userid": userid, "userps": userps}, etbl=etbl)

    try:
        cursor = conn.cursor(dictionary=True)
        print("🔍 SQLクエリを実行中...")

        # ✅ ユーザー情報を検索
        sql = "SELECT * FROM users WHERE userid = %s"
        cursor.execute(sql, (userid,))
        user = cursor.fetchone()
        print(f"📌 検索結果: {user}")

        # ❌ ユーザーIDが見つからない場合、エラーを表示
        if not user:
            etbl["userid"] = "ユーザーIDまたはパスワードが違います"
            return render_template('login.html', rec={"userid": userid, "userps": userps}, etbl=etbl)

        # ❌ パスワードが一致しない場合、エラーを表示
        if user["password"] != userps:
            etbl["userps"] = "パスワードが間違っています"
            return render_template('login.html', rec={"userid": userid, "userps": userps}, etbl=etbl)

        # ✅ 認証成功：セッションにユーザー情報を保存
        session["usname"] = user["username"]  # ユーザー名
        session["userid"] = user["userid"]  # ユーザーID
        session["userimg"]= user["avatar"]
        session["useremail"]=user["email"]
        session["userphone"]=user["phone"]
        session["userage"]=user["age"]
        session["usergender"]=user["gender"]
        session["userbirthday"]=user["birthday"].strftime("%Y年%m月%d日").lstrip("0").replace(" 0", " ")
        
        print(f"✅ ログイン成功！Session: {session}")

        return redirect('/')  # ✅ ホームページにリダイレクト

    except mariadb.Error as err:
        print(f"❌ SQLクエリエラー: {err}")
        etbl["userid"] = "データベースエラーが発生しました"
        return render_template('login.html', rec={"userid": userid, "userps": userps}, etbl=etbl)

    finally:
        cursor.close()
        conn.close()
@app.route('/search')
def search():
    car_type = request.args.get("type", "")  # ✅ 获取 URL 参数
    conn = con_db()
    
    if not conn:
        return render_template('error.html', message="データベースに接続できません")

    try:
        cursor = conn.cursor(dictionary=True)
        print(f"🔍 SQL実行: 車種 '{car_type}' を検索中...")
        
        # ✅ 查询数据库，获取相应车型的数据
        sql = "SELECT * FROM cars WHERE body_type = %s"
        cursor.execute(sql, (car_type,))
        cars = cursor.fetchall()

        return render_template("search_results.html", cars=cars, car_type=car_type)

    except mariadb.Error as err:
        print(f"❌ SQLクエリエラー: {err}")
        return render_template('error.html', message="データ取得エラーが発生しました")

    finally:
        cursor.close()
        conn.close()

# ****************************************************
# ** ログアウト ('/logout') **
# ****************************************************
@app.route('/logout')
def logout():
    session.clear()  # ✅ セッションをクリア
    return redirect(url_for('index'))  # ✅ ホームページに戻る

if __name__ == '__main__':
    app.run(debug=True)

