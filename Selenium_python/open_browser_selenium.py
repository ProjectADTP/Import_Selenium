#Импорт модуля time для работы с задержками
import time
# Импорт необходимых модулей Selenium для работы с Chrome, Firefox, Edge
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
# Импорт webdriver-manager для автоматической установки драйвера Chrome, Firefox, Edge последней версии
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_driver(driver_index): # Функция получения веб драйвера браузера по индексу
    if driver_index == 0:
        # Возврат вебдрайвера браузера Chrome последней версии с указанным ранее параметром options
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif driver_index == 1:
        #Возврат вебдрайвера браузера Firefox последней версии
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif driver_index == 2:
        #Возврат вебдрайвера браузера Edge последней версии с указанием адреса (поддержка дефолтного прекращена)
        return webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager(
                url="https://msedgedriver.microsoft.com/",
                latest_release_url="https://msedgedriver.microsoft.com/LATEST_RELEASE"
            ).install()))
    else:
        print("Неверный индекс браузера")
        return None


def open_browser(driver): #Открытие сайта указанным браузером
    try:
        # Базовый URL тестового сайта SauceDemo
        base_url = 'https://www.saucedemo.com/'
        # Переход на указанную страницу в браузере
        driver.get(base_url)
        # Установка размера окна браузера в разрешение 1920x1080 (FHD)
        driver.set_window_size(1920, 1080)
        # Задержка перед выполнением следующей команды в 10 секунд
        time.sleep(5)
        # Закрытие браузера
        driver.close()
    except Exception as e:
        print(f"Ошибка при работе с браузером: {e}") # Вывод ошибки в случае её возникновения
    finally:
        driver.quit()  # Закрытие браузера


def main(): #Основная программа
    open_browser(get_driver(0)) #Открытие сайта браузером Chrome
    open_browser(get_driver(1)) #Открытие сайта браузером Firefox
    open_browser(get_driver(2)) #Открытие сайта браузером Edge


if __name__ == '__main__':
    main()