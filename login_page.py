from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        
        # Localizadores de Login
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.TAG_NAME, "button")

    def obtener_error(self):
        """Captura el texto del mensaje de error rojo 'Invalid credentials'"""
        elemento_error = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-alert-content-text")))
        return elemento_error.text

    def ingresar_credenciales(self, usuario, clave):
        self.driver.find_element(*self.username_field).send_keys(usuario)
        self.driver.find_element(*self.password_field).send_keys(clave)
        self.driver.find_element(*self.login_button).click()

    def crear_empleado(self, nombre, apellido):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Add ']"))).click()
        self.wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(nombre)
        self.driver.find_element(By.NAME, "lastName").send_keys(apellido)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def buscar_empleado(self, nombre):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))).click()
        search = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")))
        search.send_keys(nombre)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def editar_empleado(self, nuevo_nombre):
        # 1. Clic en el icono de lápiz (Editar)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='oxd-icon bi-pencil-fill'])[1]"))).click()
        
        # 2. Limpiar y cambiar el nombre
        campo_nombre = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        campo_nombre.send_keys(Keys.CONTROL + "a")
        campo_nombre.send_keys(Keys.DELETE)
        campo_nombre.send_keys(nuevo_nombre)
        
        # --- LA SOLUCIÓN: Esperar a que el loader desaparezca ---
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader")))
        
        # 3. Clic en Guardar
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    def eliminar_empleado(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='oxd-icon bi-trash'])[1]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Yes, Delete ']"))).click()