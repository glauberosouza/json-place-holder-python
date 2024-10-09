from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URL da API JSONPlaceHolder
BASE_URL = "https://jsonplaceholder.typicode.com"

@app.route('/post/<int:id>', methods=['GET'])
def get_post(id):
    response = requests.get(f'{BASE_URL}/posts/{id}')
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Post not found'}), response.status_code

@app.route('/posts')
def get_posts():
    response = requests.get(f'{BASE_URL}/posts')
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Post not found'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)