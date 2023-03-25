import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.elements_page import TextBoxPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()
# @pytest.fixture(scope='function')
# def autorize():
#     text_box_page = TextBoxPage(driver, 'https://petfriends.skillfactory.ru/login')
#     text_box_page.open()
#     # text_box_page.SUBMIT_IF_HAVE.click()
#     text_box_page.fill_all_fields()
#     text_box_page.go_to_my_pets()



# def test_show_my_pets():
#    # Вводим email
#    pytest.driver.find_element_by_id('email').send_keys('LarryFram.r.10.1.9.93@gmail.com')
#    # Вводим пароль
#    pytest.driver.find_element_by_id('pass').send_keys('12345')
#    # Нажимаем на кнопку входа в аккаунт
#    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
#    # Проверяем, что мы оказались на главной странице пользователя
#    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"