from flask import 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE']








def init_todo_db():
    pass


def find_task(id):
    pass

def insert_task(title, description):
    pass

def change_task(task):
    pass


def remove_task(task):
    pass


@app.route('/')
def home():
    return "Welcome to Rehab's To-Do API Service"

@app.route('/todos', methods=['GET'])
def get_tasks():
    rerturn 'this returns all tasks'    


@app.route('/todos/<int:task_id>', methods=['GET'])
def get_task(task_id):
    return f'this return specific info about {task_id} task' 


@app.route('/todos', methods=['POST'])
def add_task():
    return 'this URL add new task'


@app.route('/todos/<int:task_id>', methods=['PUT']) 
def update_task(task_id):
    return f' this URL updates specific {task_id} task' 



@app.route('/todos/<int:task_id>', methods=['DELETE']) 
def delete_task(task_id):
    return f' this URL deletes specific {task_id} task'  









if __name__=='__main':
    init_todo_db    