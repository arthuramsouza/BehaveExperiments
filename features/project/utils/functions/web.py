"""
Module containing functions common to web features.
"""

from selenium import webdriver


def go_to(url, browser='chrome'):
    """
    Start instance of a browser and navigates to a url.
    :param url: web address to navigate to
    :param browser: which browser to start (default: chrome)
    :return: webdriver instance
    """
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception('The browser ' + browser + ' is not supported')

    url = url.strip()
    driver.get(url)

    return driver
