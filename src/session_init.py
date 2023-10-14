import streamlit as st
import yaml
import os

def init():
    config_yaml_path = 'config.yaml'
    #check if config.yaml exists
    if os.path.isfile(config_yaml_path):
        with open(config_yaml_path, 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            st.session_state.name = config['name']
            st.session_state.user_name = config['user_name']
            st.session_state.user_password = config['user_password']
            st.session_state.user_email = config['user_email']
            st.session_state.discord_webhook = config['discord_webhook']
    else:
        #set default values
        st.session_state.name = ""
        st.session_state.user_name = ""
        st.session_state.user_password = ""
        st.session_state.user_email = ""
        st.session_state.discord_webhook = ""
        #create config.yaml
        with open(config_yaml_path, 'w') as f:
            yaml.dump({
                'name': st.session_state.name,
                'user_name': st.session_state.user_name,
                'user_password': st.session_state.user_password,
                'user_email': st.session_state.user_email,
                'discord_webhook': st.session_state.discord_webhook
            }, f)
        

def save_config():
    config_yaml_path = 'config.yaml'
    now_values = {k: v for k, v in st.session_state.items()}
    with open(config_yaml_path, 'w') as f:
        yaml.dump(now_values, f)