from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

todos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    todo = request.json
    if 'date' not in todo:
        todo['date'] = datetime.now().strftime('%Y-%m-%d')
    todos.append(todo)
    return jsonify(todo)

@app.route('/api/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    if 0 <= index < len(todos):
        deleted_todo = todos.pop(index)
        return jsonify(deleted_todo)
    return jsonify({'error': 'Todo not found'}), 404

@app.route('/api/todos/<int:index>', methods=['PUT'])
def update_todo(index):
    if 0 <= index < len(todos):
        todo = request.json
        todos[index] = todo
        return jsonify(todo)
    return jsonify({'error': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=53191)