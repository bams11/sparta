from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('homework2.html')

## API 역할을 하는 부분
@app.route('/order_receive', methods=['POST'])
def ordering():
		# 클라이언트로부터 데이터를 받는 부분
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

    # mongoDB에 넣는 부분
    order = {

        'name': name_receive,

        'count': count_receive,

        'address': address_receive,

        'number': number_receive,

    }
		


    db.mouse_order.insert_one(article)

    return jsonify({'result': 'success'})

@app.route('/order', methods=['GET'])
def listing():
    # 모든 document 찾기 & _id 값은 출력에서 제외하기
    result = list(db.mouse_order.find({},{'_id':0}))
    # order라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'order':order})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)