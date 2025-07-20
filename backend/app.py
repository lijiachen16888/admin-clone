from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 简单的用户数据，实际可用数据库替代
users = {
    "admin": "123456"
}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({"success": True, "message": "登录成功"})
    else:
        return jsonify({"success": False, "message": "用户名或密码错误"}), 401

@app.route('/api/data', methods=['GET'])
def get_data():
    # 返回一些示例数据
    sample_data = [
        {"id": 1, "name": "产品A", "price": 100},
        {"id": 2, "name": "产品B", "price": 200},
    ]
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
