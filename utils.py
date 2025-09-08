"""
このファイルは、画面表示以外の様々な関数定義のファイルです。
"""

import logging
from typing import List
from sudachipy import tokenizer, dictionary
import constants as ct

def build_error_message(message):
    """
    エラーメッセージと管理者問い合わせテンプレートの連結

    Args:
        message: 画面上に表示するエラーメッセージ

    Returns:
        エラーメッセージと管理者問い合わせテンプレートの連結テキスト
    """
    return "\n".join([message, ct.COMMON_ERROR_MESSAGE])
