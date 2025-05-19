#*******************************************************
# PY24 課題5【画像ファイル操作】
# CLASS : IH-12A-405(07) NAME : Kaito Okada
#-------------------------------------------------------
# 2024-11-20
#*******************************************************
from flask import Flask
from flask import render_template
from flask import request , Blueprint , send_file ,session

from class_lib import Py24db
#****************************************************
# モジュール定義
#****************************************************
appdsp = Blueprint('appdsp', __name__, url_prefix='/dsp')
#****************************************************
# 商品⼀覧表⽰処理 （'/dsp'）
#****************************************************
@appdsp.route('/' , methods=["GET"])
def index():
#*** 商品⼀覧SQL⽣成 ***
    sql = 'SELECT * FROM lunch ORDER BY scode;'
#*** Py24dbクラス活⽤ ***
    py24db = Py24db() # インスタンス化 
    rec = py24db.selectSql(sql) # メソッド呼出
    return render_template('index.html', rec=rec)
#****************************************************
# 商品詳細情報画⾯表⽰処理 （'/dsp/detail'）
#****************************************************
@appdsp.route('/detail/<scode>' , methods=["GET"])
def detail(scode):
    print("OK")
    sql = "SELECT * FROM lunch WHERE scode = '" + scode + "';"
#*** Py24dbクラス活⽤ ***
    py24db = Py24db() # インスタンス化
    rec = py24db.selectSql(sql) # メソッド呼出
    print(rec)
#*** SESSION格納
    session["filename"] = rec[0][5]
    return render_template('detail.html', rec=rec)