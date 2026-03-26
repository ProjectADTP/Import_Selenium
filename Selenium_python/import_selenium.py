# Импорт необходимых модулей Selenium для работы с Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# Импорт webdriver-manager для автоматической установки драйвера Chrome последней версии
from webdriver_manager.chrome import ChromeDriverManager

# Создание переменной для работы с параметрами браузера Chrome
options = webdriver.ChromeOptions()
# Установка Опции "detach" в True для предотвращения закрытия браузера после завершения работы скрипта
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
# Базовый URL тестового сайта SauceDemo
base_url = 'https://www.saucedemo.com/'
# Переход на указанную страницу в браузере
driver.get(base_url)
# Установка размера окна браузера в разрешение 1920x1080 (FHD)
driver.set_window_size(1920, 1080)