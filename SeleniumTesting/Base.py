from selenium import webdriver


class Base():
    driver = None

    def __init__(self, website):
        self.driver = webdriver.Chrome()
        self.driver.get(website)

    def type(self, field, text):
        input_field = self.driver.find_element_by_css_selector(field)
        input_field.send_keys(text)

    def click(self, button, index=0):
        if len(self.driver.find_elements_by_css_selector(button)) >= (index + 1):
            target_button = self.driver.find_elements_by_css_selector(button)[index]
            target_button.click()

    def check_existence_of(self, element, index=0):
        if len(self.driver.find_elements_by_css_selector(element)) >= (index + 1):
            return True
        else:
            return False

    def check_content_of(self, element, xpath, content, index=0):
        if len(self.driver.find_elements_by_css_selector(element)) >= (index + 1):
            requested_element = self.driver.find_elements_by_css_selector(element)[index]
            requested_xpath = requested_element.find_element_by_xpath(xpath)
            if requested_xpath.get_attribute("innerHTML") == content:
                return True
            else:
                return False
        else:
            return False

    def check_text_of(self, element, content):
        requested_element = self.driver.find_element_by_css_selector(element)
        if requested_element.get_attribute("innerHTML") == content:
            return True
        else:
            return False

    def close_driver(self):
        self.driver.close()
        pass