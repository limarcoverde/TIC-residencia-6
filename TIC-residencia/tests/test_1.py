import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test1:

    URL = 'https://www.saucedemo.com/'
    driver = webdriver.Chrome()

    @pytest.fixture
    def open_browser(self):
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()

    def test_logout(self, open_browser):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()

        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html', "URL de Products não encontrada!"

        try:
            self.driver.find_element(By.ID, 'react-burger-menu-btn').click()
            menu_element = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        except NoSuchElementException:
            pytest.fail('Elemento Menu não encontrado!')

        assert menu_element.is_displayed(), 'Menu não encotrado!'
        
        self.driver.find_element(By.ID, 'logout_sidebar_link').click()

        assert self.driver.current_url == self.URL, "Logout não funcionou!"