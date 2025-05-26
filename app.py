from flask import Flask, render_template, request, redirect, session, url_for
import mariadb  # ✅ MariaDB（MySQL 互换性あり）
from datetime import datetime, timedelta 
from flask_mail import Mail, Message
import random
from app_dsp import appdsp

app = Flask(__name__)
app.secret_key = 'IH12xPY24_No08'  # ✅ セッションのセキュリティキー
app.permanent_session_lifetime = timedelta(minutes=15)  # ✅ セッションの有効時間を3分に設定

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'carpling.official@gmail.com'
app.config['MAIL_PASSWORD'] = 'dignuqrdshzrkiso'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

type={"body_type":""}
select_rec=[]
signup_rec={}
my_gip="118.27.30.198"

# ****************************************************
# ** データベース接続関数 (DBに接続する) **
# ****************************************************
def con_db():
    try:
        print(my_gip+"🛠️ データベース接続を試みています...")
        conn = mariadb.connect(
            # host="192.168.3.34",
            #接続出来なかった場合localhostに切り替える
            host="localhost",
            user="carpling_system_admin",
            password="carpling_admin",
            # user="root",
            # password="",
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
    select_rec.clear()
    type["body_type"]=request.form.get("type")
    if type["body_type"]=="Celibate":
        select_rec.append("100~250万円")
        select_rec.append("250~350万円")
        select_rec.append("350万円~")
    if type["body_type"]=="Family":
        select_rec.append("200~350万円")
        select_rec.append("350~550万円")
        select_rec.append("550万円~")
    if type["body_type"]=="Luxury":
        select_rec.append("300~450万円")
        select_rec.append("450~650万円")
        select_rec.append("650万円~")
    print(select_rec)
    return render_template('match_ages.html',e_tbl={},select_rec=select_rec)

@app.route('/match_result', methods=["POST"])
def match_result():
    e_tbl={}
    rec2=[]
    count=0
    desc_flag = "0"
    rec=request.form
    for key,value in rec:
        count=count+1
        print(key,value)
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
    select_sql = 0  #マッチング結果が溜まっていくバグが発生したので初期化
    if count==7:
        print("OK")
        print(type["body_type"])
        select_sql = 'SELECT * FROM cars WHERE '
        if type["body_type"]=="Celibate":
            select_sql+='category = "Celibate"'
            if rec2[0]=="A-1":
                select_sql+='AND max_price <= 2500000 '
            elif rec2[0]=="B-1":
                select_sql+='AND max_price <= 3500000 '
            else:
                desc_flag="1"
                desc_append="ORDER BY max_price DESC"

        elif type["body_type"]=="Family":
            select_sql+='category = "Family"'
            if rec2[0]=="A-1":
                select_sql+='AND max_price <= 3500000 '
            elif rec2[0]=="B-1":
                select_sql+='AND max_price <= 5500000 '
            else:
                desc_flag="1"
                desc_append="ORDER BY max_price DESC"

        elif type["body_type"]=="Luxury":
            select_sql+='category = "Luxury"'
            if rec2[0]=="A-1":
                select_sql+='AND max_price <= 4500000 '
            elif rec2[0]=="B-1":
                select_sql+='AND max_price <= 6500000 '
            else:
                desc_flag="1"
                desc_append="ORDER BY max_price DESC"

        if rec2[1]=="A-2":
            select_sql+='AND fuel_type in ("ハイブリッド" , "ガソリン / ハイブリッド")'
        elif rec2[1]=="B-2":
            select_sql+='AND fuel_type = "ガソリン(レギュラー)"'
        elif rec2[1]=="C-2":
            select_sql+='AND fuel_type in ("ガソリン(ハイオク) " , "ガソリン(レギュラー)")'

            if desc_flag =="1":
                desc_append+=', fuel_type DESC'
            else:
                desc_flag = "1"
                desc_append = "ORDER BY fuel_type DESC"                

        if rec2[2]=="A-3":
            capasity_select_sql='AND capasity >= "4"'
        elif rec2[2]=="C-3":
            capasity_select_sql='AND capasity >= "2"'
        
        if rec2[3]=="A-4":
            sport_select_sql='AND turbo = "yes"'
        elif rec2[3]=="A-4":
            sport_select_sql='AND turbo = "yes"'
        else:
            sport_select_sql='AND turbo = "N/A"'

        if desc_flag == "1":
            conn = con_db()
            cursor = conn.cursor()
            select_end_sql=';'
            sql=select_sql+desc_append+select_end_sql
            print(sql)
            cursor.execute(sql)
            car_result = cursor.fetchall()
            print(car_result)
        else:
            conn = con_db()
            cursor = conn.cursor()
            select_end_sql=';'
            sql=select_sql+select_end_sql
            print(sql)
            cursor.execute(sql)
            car_result = cursor.fetchall()
            print(car_result)
        hit_count=len(car_result)
        while len(car_result) < 10:
            car_result.append((0,0,0,0,0,0,0,0,0,0,0))
        if hit_count >= 11:
            pass
            # passではなく、11件以上からランダムに10件取り出しcar_resultに入れなおすプログラムを作る。
        
        # ヒット数が11件以上ならランダムに被りなく10件だけ取り出してcar_resultに入れなおすプログラムを追加
        return render_template('result.html',car_result=car_result, hit_count=hit_count)
        # ↑ヒット数hit_countをhit_countに入れて送る
    
    else:
        return render_template('match_ages.html',e_tbl=e_tbl,select_rec=select_rec)
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


@app.route("/confirmation", methods=["POST"])

def confirmation():
    # 送信された情報がPOSTで送られているかの確認
    if request.method == 'POST':
        etbl = {}
        # 送信された情報を取得
        username = request.form.get("username", "").strip()
        userps = request.form.get("userps", "").strip()
        useremail = request.form.get("useremail", "").strip()
        userphone = request.form.get("userphone", "").strip()
        gender = request.form.get("gender", "").strip()
        birthday = request.form.get("birthday", "").strip()
        signup_rec.update(username=username,userps=userps,useremail=useremail,userphone=userphone,gender=gender,birthday=birthday)

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
            signup_rec["age"]=age
        except ValueError:
            etbl["birthday"] = "誕生日の形式が正しくありません（YYYY-MM-DD）"
            return render_template('newlogin.html', rec=request.form, etbl=etbl)
        
        avatar_url = "https://th.bing.com/th/id/OIP.default_avatar.jpg"
        signup_rec["avatar_url"]=avatar_url
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        signup_rec["created_at"]=created_at



        conn = con_db()
        # try:
        if not conn:
            etbl["userid"] = "データベースに接続できません"
            return render_template('newlogin.html', rec=request.form, etbl=etbl)

        cursor = conn.cursor(dictionary=True)
        print("🔍 既存のユーザーIDを取得中...")
        cursor.execute("SELECT userid FROM users WHERE userid LIKE 'test%'")
        existing_users = cursor.fetchall()
        existing_numbers = set()
        for user in existing_users:
            try:
                num = int(user["userid"].replace("test", ""))
                if num >= 4:
                    existing_numbers.add(num)
            except ValueError:
                continue
        new_number = 4
        while new_number in existing_numbers:
            new_number += 1  # 递增直到找到未使用的编
        new_id = f"test{new_number:02d}"
        # ✅ **并发检查，确保 `userid` 仍然唯一**
        signup_rec["new_id"]=new_id
        cursor.execute("SELECT COUNT(*) as count FROM users WHERE userid = %s", (new_id,))
        result = cursor.fetchone()
        if result["count"] > 0:
            raise Exception(f"❌ ユーザーID {new_id} が既に存在します！")
        
        email = useremail
        code = generate_code()
        # sessionに確認コードを設定
        session["check"] = code
        print(session["check"])
        # メッセージの各種設定
        # 最初の一文：メールヘッダ
        # sender：送信元メールアドレス
        # recipients：送信先メールアドレス
        msg = Message('Carpling 登録認証コード',recipients=[email])
        # メール本文の編集
        msg.body = 'あなたの認証コード：{}　偽サイトへの入力誘導が発生しております。このメールに心当たりがない場合は削除してください。発行元：CarplingⒸ'.format(code)
        # メールを送信する一文
        mail.send(msg)
        # return 'Email sent!'
        return render_template("confirmation.html",code=code)
    
        # except Exception:
        #     print("エラーが発生しました。")
        #     return render_template("newlogin.html",etbl=etbl)


@app.route("/entry_fn" ,methods=["POST"])
def entry_fn():
    print("SIGNUP OK")
    # セッションが存在していない場合の処理
    if not session:
        return render_template("newlogin.html")
    # セッションが存在している場合の処理
    else:
        # try:

        # 取得したコードをスタックに格納
        source = request.form
        print(source)
        # からの変数を作成
        # source = ""
        # for key,value in stack.items():
        #     # 配列の確認コードを連結
        #     source += value
        # print(source)
        # coreにsessionから確認コードを取得
        core = session["check"]
        print(core)
        print(core == source["code1"])
        # 確認コードが一致していた場合に入る処理
        # try:
        if core == source["code1"]:
            etbl={}
            # ✅ 连接数据库
            conn = con_db()
            if not conn:
                etbl["userid"] = "データベースに接続できません"
                return render_template('newlogin.html', rec=request.form, etbl=etbl)
            try:
                cursor = conn.cursor(dictionary=True)
                # ✅ 插入新用户数据
                sql_insert = """
                    INSERT INTO users (userid, username, password, email, phone, avatar, age, gender, birthday, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                signup_1=signup_rec["new_id"]
                signup_2=signup_rec["username"]
                signup_3=signup_rec["userps"]
                signup_4=signup_rec["useremail"]
                signup_5=signup_rec["userphone"]
                signup_6=signup_rec["avatar_url"]
                signup_7=signup_rec["age"]
                signup_8=signup_rec["gender"]
                signup_9=signup_rec["birthday"]
                signup_10=signup_rec["created_at"]

                cursor.execute(sql_insert, (signup_1,signup_2,signup_3,signup_4,signup_5,signup_6,signup_7,signup_8,signup_9,signup_10))
                conn.commit()
                print(f"✅ 新規ユーザー登録成功！userid: {signup_rec['new_id']}")
                login_success="登録に成功しました。あなたのIDは[ {} ]です。ログインしてください。".format(signup_1)
                return render_template('login.html', login_success=login_success , rec=request.form, etbl=etbl)  # ✅ 登録後ログインページへリダイレクト
            except mariadb.Error as err:
                print(f"❌ SQLエラー: {err}")
                etbl["userid"] = "データベースエラーが発生しました"
                return render_template('newlogin.html', rec=request.form, etbl=etbl)
            finally:
                cursor.close()
                conn.close()
        else:
            error = "確認コードが間違っています。もう一度お試しください"
            return render_template("confirmation.html",error=error)
            
        # except Exception:
        #     print("エラーが発生しました。")
        #     return render_template("index.html")

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
        session["usertype"]=user["user_type"]
        
        print(f"✅ ログイン成功！Session: {session}")
        if session["usertype"]=="n":
            return redirect('/')  # ✅ ホームページにリダイレクト
        elif session["usertype"]=="a":
            return render_template('system.html', rec={"userid": userid, "userps": userps})

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
# ** 管理機能 ('/system') **
# ****************************************************

@app.route("/system" ,methods=["GET"])
def system():
    return render_template("system.html",session=session)

@app.route("/system_2" ,methods=["GET"])
def system_2():
    return render_template("system_2.html")

# ****************************************************
# ** ログアウト ('/logout') **
# ****************************************************
@app.route('/logout')
def logout():
    session.clear()  # ✅ セッションをクリア
    return redirect(url_for('index'))  # ✅ ホームページに戻る

def generate_code(length=6):
    # 数字のみの確認コードを生成
    digits = '0123456789'
    return ''.join(random.choice(digits) for _ in range(length))

@app.errorhandler(404)
def error404(error):
    error="page not found"
    type="404"
    text="ページが見つかりません"
    return render_template("error.html",error=error,type=type,text=text),404

@app.errorhandler(413)
def error413(error):
    error="error"
    type="413"
    text="ファイル容量は2MB以下にしてください"
    return render_template("error.html",error=error,type=type,text=text),413


@app.errorhandler(500)
def error500(error):
    error="server error"
    type="500"
    text="以下の連絡先にお問い合わせください"
    return render_template("errorUser.html",error=error,type=type,text=text),500

if __name__ == '__main__':
    app.run(debug=True)

# ****************************************************
# ** マッチ結果 ('/loginck') **
# ****************************************************
@app.route('/match_result', methods=["POST"])
def match_result():
    return render_template('result.html')
# ****************************************************

