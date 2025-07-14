# Vercel에 배포할 app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# 실제 비밀번호는 코드 안에 저장하거나 환경 변수로 설정
CORRECT_PASSWORD = "1234"

@app.route('/')
def home():
    return "Roblox Window Monotor V2 Authenticate Server"

@app.route('/verify', methods=['POST'])
def verify_password():
    data = request.get_json()
    if not data or 'password' not in data:
        return jsonify({"success": False, "message": "Password not provided"}), 400

    user_password = data['password']
    if user_password == CORRECT_PASSWORD:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "Invalid password"})

if __name__ == '__main__':
    app.run(debug=True)