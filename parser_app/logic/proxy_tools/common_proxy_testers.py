import os
from typing import Optional

from selenium import webdriver
import json

from parser_app.logic.handlers.handler_tools import load_page_with_TL


GOOGLE_CHROME_ERROR_LIST = json.load(
    open(os.path.join('.', 'parser_app', 'logic', 'proxy_tools', 'google_chrome_error_list.json'))
)


def simple_test_driver_with_url(driver: webdriver.Chrome, url: str) -> bool:
    try:
        page = load_page_with_TL(driver, url, 7.5)
    except:
        return False
    return test_html_page(page)


def test_html_page(page: Optional[str] = None) -> bool:
    if page is None:
        return False

    # чистой воды эвристика
    if len(page) < 500:
        return False

    if not isinstance(page, str):
        return False

    page_text = str(page).lower()

    for custom_bad_word in ["an error occurred", "no internet", "bad ip", "web page blocked"]:
        if custom_bad_word in page_text:
            return False

    for google_chrome_error in GOOGLE_CHROME_ERROR_LIST:
        if google_chrome_error.lower() in page_text:
            return False

    return True

