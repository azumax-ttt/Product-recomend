"""
このファイルは、Webアプリのメイン処理が記述されたファイルです。
"""

from dotenv import load_dotenv
import logging
import streamlit as st
from initialize import initialize
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
