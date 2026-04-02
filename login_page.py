import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 25)

    def ingresar_credenciales(self, usuario, clave):
        self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(usuario)
        self.driver.find_element(By.NAME, "password").send_keys(clave)
        self.driver.find_element(By.TAG_NAME, "button").click()

    def obtener_error(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-alert-content-text"))).text

    def crear_empleado(self, nombre, apellido):
        # Navegar a PIM
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Add ']"))).click()
        
        # Llenar datos
        self.wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(nombre)
        self.driver.find_element(By.NAME, "lastName").send_keys(apellido)
        
        # ID Único para evitar errores de validación del sistema
        emp_id_field = self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        emp_id_field.send_keys(Keys.CONTROL + "a")
        emp_id_field.send_keys(Keys.DELETE)
        emp_id_field.send_keys(str(int(time.time()))[-5:])
        
        # Esperar a que el loader desaparezca (si existe)
        try:
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader")))
        except:
            pass

        # Guardado forzado
        btn_save = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        self.driver.execute_script("arguments[0].click();", btn_save)
        
        # Esperar a que la página cambie (importante para que no falle el test siguiente)
        time.sleep(5)

    def buscar_empleado(self, nombre):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))).click()
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Employee List"))).click()
        
        # Esperar al campo de búsqueda
        search = self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Employee Name']/ancestor::div[1]/following-sibling::div//input")))
        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(Keys.DELETE)
        search.send_keys(nombre)
        
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5) # Tiempo para que la tabla se refresque

    def editar_empleado(self, nuevo_nombre):
        lapiz = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='oxd-icon bi-pencil-fill'])[1]")))
        self.driver.execute_script("arguments[0].click();", lapiz)
        time.sleep(3)
        campo = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        campo.send_keys(Keys.CONTROL + "a")
        campo.send_keys(Keys.DELETE)
        campo.send_keys(nuevo_nombre)
        
        btn_save = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", btn_save)
        time.sleep(5)

    def eliminar_empleado(self):
        basura = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[i[@class='oxd-icon bi-trash']]")))
        self.driver.execute_script("arguments[0].click();", basura)
        confirmar = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Yes, Delete ']")))
        self.driver.execute_script("arguments[0].click();", confirmar)
        time.sleep(5)