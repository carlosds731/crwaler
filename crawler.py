def start_crawler():
    from selenium.webdriver import Chrome

    browser = Chrome()

    browser.get("http://www.hauts-de-seine.gouv.fr/booking/create/11025/0")

    return browser