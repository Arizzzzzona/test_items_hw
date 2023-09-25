import pytest
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


cases = [
    ("es", "Añadir al carrito",),
    ("fr", "Ajouter au panier",),
    ("ru", "Добавить в корзину",),
    ("en", "Add to basket",),
]

ids = [x[0] for x in cases]

@pytest.mark.parametrize("language, want", cases,ids=ids)
def test_basket_btn(browser,user_language,language,want):
    if language != user_language:
        pytest.skip(f"skip {language} language")
    
    browser.get(link)
    browser.implicitly_wait(10)
    
    btn = browser.find_element(By.XPATH,"//*[@class='btn btn-lg btn-primary btn-add-to-basket']")
    got = btn.text
    assert want == got, f"want '{want}, got '{got}'"
    time.sleep(5)
