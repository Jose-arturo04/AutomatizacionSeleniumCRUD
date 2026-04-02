import pytest
import os
from login_page import LoginPage 

# NOTA: No pongas @pytest.fixture aquí, eso ya está en conftest.py

def test_HU01_login_exitoso(driver):
    """Prueba de ingreso con credenciales válidas"""
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.ingresar_credenciales("Admin", "admin123")
    
    # Crear carpeta de reportes si no existe
    if not os.path.exists('reports'): 
        os.makedirs('reports')
        
    driver.save_screenshot("reports/HU01_Login_Exitoso.png")
    assert "dashboard" in driver.current_url.lower()

def test_HU01_login_incorrecto(driver):
    """Prueba de rechazo con credenciales inválidas"""
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.ingresar_credenciales("UsuarioFalso", "ClaveFalsa")
    
    if not os.path.exists('reports'): 
        os.makedirs('reports')
        
    driver.save_screenshot("reports/HU01_Login_Fallido.png")
    # Este assert usará el método 'obtener_error' que añadimos a login_page.py
    assert "Invalid credentials" in login.obtener_error()