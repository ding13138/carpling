from flask import Flask, render_template, request, redirect, session, url_for
import mariadb  # ✅ MariaDB（MySQL 互换性あり）
from datetime import datetime, timedelta 

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
            #user="root",
            #password="",
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
    e_tbl={}
    rec2=[]
    count=0
    rec=request.form

    
    return render_template('match_result.html')
#****************************************************
# ログイン画面表示 （'/login'）
#****************************************************



# ****************************************************
# ** ログインページ ('/login') **
# ****************************************************
@app.route('/login', methods=["GET"])
def login():
    session.clear()  
    return render_template('login.html', rec={}, etbl={})





# ****************************************************
# ** 新規登録ページ ('/newlogin') **
# ****************************************************
@app.route('/newlogin', methods=["GET"])
def newlogin():
    return render_template('newlogin.html', rec={}, etbl={})

@app.route('/newloginck', methods=["POST"])
def newloginck():
    etbl = {}
    username = request.form.get("username", "").strip()
    userps = request.form.get("userps", "").strip()
    useremail = request.form.get("useremail", "").strip()
    userphone = request.form.get("userphone", "").strip()
    gender = request.form.get("gender", "").strip()
    birthday = request.form.get("birthday", "").strip()

    print(f"📌 入力内容: {username}, {useremail}, {userphone}, {gender}, {birthday}")

    # 入力チェック
    if not username:
        etbl["username"] = "ユーザー名が入力されていません"
    if not userps:
        etbl["userps"] = "パスワードが入力されていません"
    if not useremail:
        etbl["useremail"] = "メールアドレスが入力されていません"
    if not userphone:
        etbl["userphone"] = "電話番号が入力されていません"
    if not gender:
        etbl["gender"] = "性別が選択されていません"
    if not birthday:
        etbl["birthday"] = "誕生日が入力されていません"

    if etbl:
        return render_template('newlogin.html', rec=request.form, etbl=etbl)

    # ✅ 计算年龄
    try:
        birth_date = datetime.strptime(birthday, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    except ValueError:
        etbl["birthday"] = "誕生日の形式が正しくありません（YYYY-MM-DD）"
        return render_template('newlogin.html', rec=request.form, etbl=etbl)

    # ✅ 头像 & 注册时间
    avatar_url = "https://th.bing.com/th/id/OIP.default_avatar.jpg"
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ✅ 连接数据库
    conn = con_db()
    if not conn:
        etbl["userid"] = "データベースに接続できません"
        return render_template('newlogin.html', rec=request.form, etbl=etbl)

    try:
        cursor = conn.cursor(dictionary=True)
        print("🔍 既存のユーザーIDを取得中...")

        # ✅ 获取数据库中所有 `textXX` 格式的 `userid`
        cursor.execute("SELECT userid FROM users WHERE userid LIKE 'test%'")
        existing_users = cursor.fetchall()

        # ✅ 提取所有已使用编号，并过滤掉 text01, text02, text03
        existing_numbers = set()
        for user in existing_users:
            try:
                num = int(user["userid"].replace("test", ""))
                if num >= 4:  # 从 text04 开始
                    existing_numbers.add(num)
            except ValueError:
                continue  # 格式错误，跳过

        # ✅ 找到最小的可用 `XX`（从 4 开始递增）
        new_number = 4
        while new_number in existing_numbers:
            new_number += 1  # 递增直到找到未使用的编号

        new_id = f"test{new_number:02d}"

        print(f"✅ 新しいユーザーID: {new_id}")

        # ✅ **并发检查，确保 `userid` 仍然唯一**
        cursor.execute("SELECT COUNT(*) as count FROM users WHERE userid = %s", (new_id,))
        result = cursor.fetchone()
        if result["count"] > 0:
            raise Exception(f"❌ ユーザーID {new_id} が既に存在します！")

        # ✅ 插入新用户数据
        sql_insert = """
            INSERT INTO users (userid, username, password, email, phone, avatar, age, gender, birthday, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql_insert, (new_id, username, userps, useremail, userphone, avatar_url, age, gender, birthday, created_at))
        conn.commit()
        print(f"✅ 新規ユーザー登録成功！userid: {new_id}")

        return redirect(url_for('login'))  # ✅ 登録後ログインページへリダイレクト

    except mariadb.Error as err:
        print(f"❌ SQLエラー: {err}")
        etbl["userid"] = "データベースエラーが発生しました"
        return render_template('newlogin.html', rec=request.form, etbl=etbl)

    except Exception as e:
        print(str(e))
        etbl["userid"] = "ユーザーIDの生成中にエラーが発生しました"
        return render_template('newlogin.html', rec=request.form, etbl=etbl)

    finally:
        cursor.close()
        conn.close()




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

# ****************************************************
# ** マッチ結果 ('/loginck') **
# ****************************************************
@app.route('/match_result', methods=["POST"])
def match_result():
    return render_template('result.html')
# ****************************************************