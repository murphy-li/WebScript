from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def login_199(operation):
    login(operation, "http://10.20.23.199:8088/uf3-web/", "admin", "admin@123")


def login(operation, url, user_name, password):
    """

    :param operation:
    :param url:
    :param user_name:
    :param password:
    :return:
    """
    operation.sync_open(url)
    operation.send_keys("[name=username]", user_name, 0)
    operation.send_keys("[name=password]", password, 0)
    while operation.wait_url_end_withs("/#/mainIndex") is False:
        operation.click("登录")
        operation.sleep(10)
    # operation.click("确定")
    # operation.accept_prompt()
