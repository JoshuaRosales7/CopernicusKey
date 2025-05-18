from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

CLIENT_ID = 'sh-25104f90-3d60-43a2-b7b9-dd137c9a7f86'
CLIENT_SECRET = 'OKv5aHVx2xOJgITcviwQdjHbeAVzpl4g'
TOKEN_URL = 'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token'

@app.route('/token', methods=['POST'])
def get_token():
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
    try:
        res = requests.post(TOKEN_URL, data=data, headers=headers)
        res.raise_for_status()
        return jsonify(res.json()), 200
    except Exception as e:
        return jsonify({'error': 'token_error', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
