from src.components.footer import footer_dashboard
import streamlit as st
from src.ui.base_layout import style_base_layout, style_background_dashboard
from src.components.header import header_dashboard

def teacher_screen():
    style_base_layout()
    style_background_dashboard()

    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=='login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'register':
        teacher_screen_register()


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

    techer_username = st.text_input("Enter Username", placeholder='ex. farhanwajid')
    teacher_pass = st.text_input("Enter Password", type='password', placeholder='Enter Password')

    btnc1, btnc2 = st.columns(2)
    st.space()
    with btnc1:
        st.button("Login", icon=':material/passkey:', width='stretch')
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

    techer_username = st.text_input("Enter Username", placeholder='ex. farhanwajid@')
    techer_name = st.text_input("Enter Name", placeholder='Farhan Wajid')
    teacher_pass = st.text_input("Enter Password", type='password', placeholder='Enter Password')
    teacher_pass_confirm = st.text_input("Confirm the Password", type='password', placeholder='Confirm the Password')


    btnc1, btnc2 = st.columns(2)
    st.space()
    with btnc1:
        st.button("Register Now", type='primary',icon=':material/passkey:', width='stretch')
    with btnc2:
        if st.button("Login Instead" ,type='secondary',icon=':material/passkey:', width='stretch'):
            st.session_state.teacher_login_type='login'
            st.rerun()
        

    footer_dashboard()