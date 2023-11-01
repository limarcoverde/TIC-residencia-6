import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test2:

    URL = 'https://www.saucedemo.com/'
    PRODUCT_NAME = 'Sauce Labs Backpack'
    PRODUCT_VALUE = '$29.99'
    PRODUCT_QTD = '1'
    PRODUCT_DESCRIPTION = 'carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.'

    @pytest.fixture
    def open_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()

    def test_add_product(self, open_browser):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()

        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html', "URL de Products não encontrada!"

        try:
            self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
            print('test')
        except NoSuchElementException:
            pytest.fail('Elemento para adicionar não encontrado!')
        
        try:
            remove_button = self.driver.find_element(By.ID, 'remove-sauce-labs-backpack')
        except NoSuchElementException:
            pytest.fail('Remove button não encontrado!')

        assert remove_button.is_displayed(), 'Remove button não encotrado!'
    
        try:
            icon_cart = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
        except NoSuchElementException:
            pytest.fail('Icon cart value não encontrado!')
        
        assert icon_cart.is_displayed(), 'Icon cart value não encotrado!'
        assert icon_cart.text == '1'

        try:
            self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        except NoSuchElementException:
            pytest.fail('Icon cart não encontrado!')

        assert self.driver.current_url == 'https://www.saucedemo.com/cart.html', "URL do cart não encontrada!"

        try:
            productName = self.driver.find_element(By.CLASS_NAME, 'inventory_item_name')
            productQTD = self.driver.find_element(By.CLASS_NAME, 'cart_quantity')
            productDescription = self.driver.find_element(By.CLASS_NAME, 'inventory_item_desc')
            productValue = self.driver.find_element(By.CLASS_NAME, 'inventory_item_price')
        except NoSuchElementException:
            pytest.fail('Produto não está no carrinho!')

        assert productName.text == self.PRODUCT_NAME
        assert productQTD.text == self.PRODUCT_QTD
        assert productDescription.text == self.PRODUCT_DESCRIPTION
        assert productValue.text == self.PRODUCT_VALUE
            
        





