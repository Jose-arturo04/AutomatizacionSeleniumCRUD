import pytest
import time
from login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_HU02_crear_empleado_exitoso(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.ingresar_credenciales("Admin", "admin123")
    
    nombre_jose = f"Arturo{str(int(time.time()))[-4:]}"
    login.crear_empleado(nombre_jose, "Selenium")
    
    # Aumentamos la paciencia a 50 segundos y validamos la URL
    WebDriverWait(driver, 50).until(EC.url_contains("viewPersonalDetails"))
    assert "viewPersonalDetails" in driver.current_url