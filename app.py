from flask import Flask, render_template, request, jsonify
from app_service import AppService

app = Flask(__name__)
appService = AppService()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/tasks')
def get_tasks():
    tasks = appService.get_tasks()
    return jsonify(tasks)

@app.route('/api/task', methods=['POST'])
def create_task():
    task = request.json.get('task')
    if task:
        new_task = appService.create_task(task)
        return jsonify(new_task), 201
    else:
        return jsonify({'error': 'Invalid request'}), 400

@app.route('/api/task', methods=['PUT'])
def update_task():
    task = request.json.get('task')
    if task:
        updated_task = appService.update_task(task)
        return jsonify(updated_task), 200
    else:
        return jsonify({'error': 'Invalid request'}), 400

@app.route('/api/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    result = appService.delete_task(id)
    if result:
        return jsonify({'message': 'Task deleted successfully'}), 200
    else:
        return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run()
