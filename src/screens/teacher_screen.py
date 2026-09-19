from src.components.footer import footer_dashboard
import streamlit as st
from src.ui.base_layout import style_base_layout, style_background_dashboard
from src.components.header import header_dashboard

from src.database.db import create_teacher, check_teacher_exists, teacher_login

def teacher_screen():
    style_base_layout()
    style_background_dashboard()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=='login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'register':
        teacher_screen_register()

def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    st.header(f"Welcome {teacher_data['name']}!")

def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All Fields are required!"
    if check_teacher_exists(teacher_username):
        return False, "This username already exists!"
    if teacher_pass != teacher_pass_confirm:
        return False, "Password doesn't match!"

    try:
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Successfully Created! Login Now"
    except Exception as e:
        return False, f"Unexpected Error: {e}"


def login_teacher(teacher_username, teacher_pass):
    if not teacher_username or not teacher_pass:
        return False, "All Fields Required"
    
    try:
        teacher_login(teacher_username, teacher_pass)
        return True, "Successful Login"
    except Exception as e:
        return False, f"Unexpected Error: {e}"

def login_teacher(teacher_username,teacher_pass):
    if not teacher_username or not teacher_pass:
        return False

    teacher = teacher_login(teacher_username, teacher_pass)
    
    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    
    else:
        return False
    
    

def teacher_screen_login():
    c1, c2 = st.columns(2, gap="large", vertical_alignment="center")

    with c1:
        header_dashboard()
    
    with c2:
        if st.button("Back to Home",type='secondary', key='loginbackbtn', width='stretch'):
            st.session_state['login_type'] = None
            st.rerun()
    st.header('Login using Password')
    st.space()
    st.space()

    teacher_username = st.text_input("Enter Username", placeholder='ex. farhanwajid')
    teacher_pass = st.text_input("Enter Password", type='password', placeholder='Enter Password')

    btnc1, btnc2 = st.columns(2)
    st.space()
    with btnc1:
        if st.button("Login", icon=':material/passkey:', width='stretch'):
            if login_teacher(teacher_username, teacher_pass):
                st.toast("Welcome Back!", icon="👋")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid Username and Password Combo...")

    with btnc2:
        if st.button("Register Instead", type='primary' ,icon=':material/passkey:', width='stretch'):
            st.session_state.teacher_login_type = 'register'
            st.rerun()

    footer_dashboard()


def teacher_screen_register():
    c1, c2 = st.columns(2, gap="large", vertical_alignment="center")

    with c1:
        header_dashboard()
    
    with c2:
        if st.button("Back to Home",type='secondary', key='registerbackbtn', width='stretch'):
            st.session_state['login_type'] = None
            st.rerun()  

    st.header('Register using Password')
    st.space()
    st.space()

    teacher_username = st.text_input("Enter Username", placeholder='ex. farhanwajid@')
    teacher_name = st.text_input("Enter Name", placeholder='Farhan Wajid')
    teacher_pass = st.text_input("Enter Password", type='password', placeholder='Enter Password')
    teacher_pass_confirm = st.text_input("Confirm the Password", type='password', placeholder='Confirm the Password')


    btnc1, btnc2 = st.columns(2)
    st.space()
    with btnc1:
        if st.button("Register Now", type='primary',icon=':material/passkey:', width='stretch'):
            success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
            if success:
                st.success(message)
                import time 
                time.sleep(2)
                st.session_state.teacher_login_type = 'login'
                st.rerun()
            else:
                st.error(message)

    with btnc2:
        if st.button("Login Instead" ,type='secondary',icon=':material/passkey:', width='stretch'):
            st.session_state.teacher_login_type='login'
            st.rerun()
        

    footer_dashboard()