import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.remote.webdriver import WebDriver

log = logging.getLogger(__name__)


def get_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("window-size=1920x1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(chrome_options=options)
    # chrome드라이버가 PATH 환경변수 설정이 되어있지 않다면 executable_path 옵션으로 chromedriver 위치 지정
    # browser = webdriver.Chrome(chrome_options=options, executable_path="/usr/local/bin/chromedriver")
    return browser


def login_action(browser: WebDriver, url: str, id: str, password: str):
    browser.get(url)
    id_input = browser.find_element(
        by=By.CSS_SELECTOR, value="#basic_outlogin > div:nth-child(2) > div > input"
    )
    id_input.send_keys(id)
    password_input = browser.find_element(
        by=By.CSS_SELECTOR, value="#basic_outlogin > div:nth-child(3) > div > input"
    )
    password_input.send_keys(password)
    browser.find_element(
        by=By.CSS_SELECTOR, value="#basic_outlogin > div:nth-child(4) > button"
    ).click()

    time.sleep(5)

    try:
        alert = browser.switch_to.alert()
        log.info(alert.text)
        alert.accept()
    except Exception as e:
        log.info(e)


def logout_action(browser: WebDriver):
    browser.find_element(
        by=By.CSS_SELECTOR,
        value="#thema_wrapper > div.at-body > div > div > div.row > div.col-md-3 > div.hidden-sm.hidden-xs > div.miso-outlogin > a",
    ).click()


def login(url: str, id: str, password: str) -> str:
    browser = get_browser()
    login_action(browser, url, id, password)

    text = browser.find_element(
        by=By.CSS_SELECTOR,
        value="#thema_wrapper > div.at-body > div > div > div.row > div.col-md-3 > div.hidden-sm.hidden-xs > div.miso-outlogin > div.login-line > div.pull-left > a > b",
    ).text
    logout_action(browser)

    browser.close()

    log.info("text=%s", text)

    return text
