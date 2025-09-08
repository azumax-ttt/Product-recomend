"""
このファイルは、Webアプリのメイン処理が記述されたファイルです。
"""

from dotenv import load_dotenv
import logging
import streamlit as st
import utils
from initialize import initialize
import components as cn
import constants as ct

st.set_page_config(
    page_title=ct.APP_NAME
)

load_dotenv()

logger = logging.getLogger(ct.LOGGER_NAME)

try:
    initialize()
except Exception as e:
    logger.error(f"{ct.INITIALIZE_ERROR_MESSAGE}\n{e}")
    st.error(utils.build_error_message(ct.INITIALIZE_ERROR_MESSAGE))
    st.stop()

if not "initialized" in st.session_state:
    st.session_state.initialized = True
    logger.info(ct.APP_BOOT_MESSAGE)

cn.display_app_title()

cn.display_initial_ai_message()

try:
    cn.display_conversation_log()
except Exception as e:
    logger.error(f"{ct.CONVERSATION_LOG_ERROR_MESSAGE}\n{e}")
    st.error(utils.build_error_message(ct.CONVERSATION_LOG_ERROR_MESSAGE))
    st.stop()

chat_message = st.chat_input(ct.CHAT_INPUT_HELPER_TEXT)

if chat_message:
    logger.info({"message": chat_message})

    with st.chat_message("user", avatar=ct.USER_ICON_FILE_PATH):
        st.markdown(chat_message)

    res_box = st.empty()
    with st.spinner(ct.SPINNER_TEXT):
        try:
            result = st.session_state.retriever.invoke(chat_message)
        except Exception as e:
            logger.error(f"{ct.RECOMMEND_ERROR_MESSAGE}\n{e}")
            st.error(utils.build_error_message(ct.RECOMMEND_ERROR_MESSAGE))
            st.stop()
    
    with st.chat_message("assistant", avatar=ct.AI_ICON_FILE_PATH):
        try:
            cn.display_product(result)
            
            logger.info({"message": result})
        except Exception as e:
            logger.error(f"{ct.LLM_RESPONSE_DISP_ERROR_MESSAGE}\n{e}")
            st.error(utils.build_error_message(ct.LLM_RESPONSE_DISP_ERROR_MESSAGE))
            st.stop()

    st.session_state.messages.append({"role": "user", "content": chat_message})
    st.session_state.messages.append({"role": "assistant", "content": result})