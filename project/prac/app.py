from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['bams']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('bams')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

#GET 
#데이터를 조회할 때, 구글에서 인터스텔라를 조회한다. (HTML)
#공공 데이터 오픈 API에서 데이터를 가져온다 (JSON)
#통상적으로 서버 데이터를 가져오기만 하면 GET
#POST
#데이터를 추가하고, 변경하고, 삭제하고,
#회원 가입함 -> 데이터를 추가함
#데이터를 body key:value를 추가함