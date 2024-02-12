from flask import Blueprint
from ..controllers.teachers_crontrollers import teacher_login_page, teacher_signup_page, teacher_panel_page, create_task
from ..controllers.students_controllers import homepage, signup_page, login_page, students_tasks_panel 

blueprint = Blueprint('main', __name__)

@blueprint.route('/', methods=['GET'])
def return_index():
    return homepage()

@blueprint.route('/signup', methods=['GET', 'POST'])
def return_signup():
    return signup_page()

@blueprint.route('/login', methods=['GET', 'POST'])
def return_login():
    return login_page()

@blueprint.route('/assignments')
def return_tasks_panel():
    return students_tasks_panel()

@blueprint.route('/teacher-signup', methods=['GET', 'POST'])
def return_teacher_signup():
    return teacher_signup_page()

@blueprint.route('/teacher-login', methods=['GET', 'POST'])
def return_login_page():
    return teacher_login_page()

@blueprint.route('/teacher-panel', methods=['GET', 'POST'])
def return_teacher_panel():
    return teacher_panel_page()

@blueprint.route('/create-task', methods=['GET', 'POST'])
def return_create_task():
    return create_task()

if __name__ == '__main__':
    blueprint.run(debug=True)
