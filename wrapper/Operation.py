import selenium
import time
import logging
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)

class Operation:

    driver = None

    def __init__(self, remote_web_driver):
        self.driver = remote_web_driver

    def sync_open(self, url):
        self.driver.get(url)

    def click(self, selector, index=0):
        self.find_elements(selector)[index].click()

    def send_keys(self, selector, string, index=0):
        self.find_elements(selector)[index].send_keys(string)

    # def find_element(self, selector):
    #     try:
    #         return self.driver.find_element_by_id(selector)
    #     except selenium.common.exceptions.NoSuchElementException as e:
    #         logging.debug("找不到id为：" + selector + "的元素")
    #     try:
    #         return self.driver.find_element_by_name(selector)
    #     except selenium.common.exceptions.NoSuchElementException as e:
    #         logging.debug("找不到名字为：" + selector + "的元素")
    #     try:
    #         return self.driver.find_element_by_class_name(selector)
    #     except selenium.common.exceptions.NoSuchElementException as e:
    #         logging.debug("找不到类名为：" + selector + "的元素")
    #     try:
    #         return self.driver.find_element_by_tag_name(selector)
    #     except selenium.common.exceptions.NoSuchElementException as e:
    #         logging.debug("找不到标签为：" + selector + "的元素")
    #     try:
    #         return self.driver.find_element_by_link_text(selector)
    #     except selenium.common.exceptions.NoSuchElementException as e:
    #         logging.debug("找不到链接文字为：" + selector + "的元素")
    #     try:
    #         return self.driver.find_element_by_partial_link_text(selector)
    #     except selenium.common.exceptions.NoSuchElementException as e:
    #         logging.debug("找不到链接部分文字为：" + selector + "的元素")
    #     try:
    #         return self.driver.find_element_by_css_selector(selector)
    #     except selenium.common.exceptions.NoSuchElementException as e:
    #         logging.debug("找不到css选择器为：" + selector + "的元素")
    #     raise selenium.common.exceptions.NoSuchElementException

    def find_elements(self, selector):
        res = self.driver.find_elements_by_css_selector(selector)
        if len(res) > 0:
            return res
        logging.debug("找不到css选择器为：" + selector + "的元素")

        # res = self.driver.find_elements_by_xpath("//*[text()='" + selector + "']")
        # if len(res) > 0:
        #     return res
        # logging.debug("找不到文字包含：" + selector + "的元素")

        res = self.driver.find_elements_by_xpath("//*[contains(text(),'" + selector + "')]")
        if len(res) > 0:
            return res
        logging.debug("找不到部分文字包含：" + selector + "的元素")

        res = self.driver.find_elements_by_link_text(selector)
        if len(res) > 0:
            return res
        logging.debug("找不到链接文字为：" + selector + "的元素")
        res =  self.driver.find_elements_by_partial_link_text(selector)
        if len(res) > 0:
            return res
        logging.debug("找不到链接部分文字为：" + selector + "的元素")
        res = self.driver.find_elements_by_id(selector)
        if len(res) > 0:
            return res
        logging.debug("找不到id为：" + selector + "的元素")
        res = self.driver.find_elements_by_name(selector)
        if len(res) > 0:
            return res
        logging.debug("找不到名字为：" + selector + "的元素")
        try:
            res = self.driver.find_elements_by_class_name(selector)
            if len(res) > 0:
                return res
        except selenium.common.exceptions.InvalidSelectorException as e:
            logging.debug("找不到类名为：" + selector + "的元素", e)
        res = self.driver.find_elements_by_tag_name(selector)
        if len(res) > 0:
            return res
        logging.debug("找不到标签为：" + selector + "的元素")
        raise selenium.common.exceptions.NoSuchElementException()

    def wait_url_end_withs(self, url_end):
        url = self.driver.current_url
        return True if url.endswith(url_end) else False

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

    def accept_prompt(self):
        dig_prompt = self.driver.switch_to.alert
        # 在弹框内输入信息
        # dig_prompt.send_keys("Loading")
        dig_prompt.appept()