from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

users = []
posts = []
comments = []


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)
    return jsonify({'message': 'User not found.'}), 404


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        'id': len(users) + 1,
        'username': data['username'],
        'email': data['email'],
        'password': data['password']
    }
    users.append(new_user)
    return jsonify({'message': 'New user has been created.'})


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    for user in users:
        if user['id'] == user_id:
            data = request.get_json()
            user['username'] = data['username']
            user['email'] = data['email']
            user['password'] = data['password']
            return jsonify({'message': 'The user has been updated.'})
    return jsonify({'message': 'User not found.'}), 404


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({'message': 'The user has been deleted.'})
    return jsonify({'message': 'User not found.'}), 404


@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)


@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            return jsonify(post)
    return jsonify({'message': 'Post not found.'}), 404


@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = {
        'id': len(posts) + 1,
        'title': data['title'],
        'content': data['content'],
        'date_posted': datetime.utcnow().isoformat(),
        'user_id': data['user_id']
    }
    posts.append(new_post)
    return jsonify({'message': 'New post has been created.'})


@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            data = request.get_json()
            post['title'] = data['title']
            post['content'] = data['content']
            return jsonify({'message': 'The post has been updated.'})
    return jsonify({'message': 'Post not found.'}), 404


@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            posts.remove(post)
            return jsonify({'message': 'The post has been deleted.'})
    return jsonify({'message': 'Post not found.'}), 404


@app.route('/posts/<int:post_id>/comments', methods=['POST'])
def create_comment(post_id):
    data = request.get_json()
    new_comment = {
        'id': len(comments) + 1,
        'content': data['content'],
        'date_posted': datetime.utcnow().isoformat(),
        'user_id': data['user_id'],
        'post_id': post_id
    }
    comments.append(new_comment)
    return jsonify({'message': 'New comment has been created.'})


if __name__ == '__main__':
    app.run(debug=True)
