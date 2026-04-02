import pytest
import time
import os
from login_page import LoginPage

# Pytest tomará automáticamente el 'driver' de conftest.py

def test_HU02_crear_empleado_exitoso(driver):
    """Escenario: Crear un nuevo empleado en el módulo PIM"""
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    
    # 1. Login previo indispensable
    login.ingresar_credenciales("Admin", "admin123")
    
    # 2. Acción CRUD: Create (Usando el método robusto con esperas)
    login.crear_empleado("Jose", "Selenium")
    
    # 3. Pausa estratégica para el video y para que el server procese
    time.sleep(6) 
    
    # 4. Captura de pantalla de evidencia
    if not os.path.exists('reports'): 
        os.makedirs('reports')
    driver.save_screenshot("reports/HU02_Create_Exitoso.png")
    
    # 5. Validación final por URL
    assert "viewPersonalDetails" in driver.current_url