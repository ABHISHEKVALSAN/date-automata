import os
import time
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import omegaconf

env = os.environ.get('ENVIRONMENT')
config = omegaconf.OmegaConf.load(f'config/{env}.yaml')


def like_profile(driver):
        for j in [0,1]:
            for i in ['3','4','5']:
                try:
                    driver.find_element(
                        by=By.XPATH,
                        value=config.like_xpath[j].format(i)).click()
                    return
                except:
                    pass
        raise Exception('Could not find the like button')

def get_driver():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options,
    )
    driver.get(config.url)
    while True:
        try:
            like_profile(driver)
        except:
            time.sleep(5)
    driver.implicitly_wait(1)
    return driver


def main():
    """Main function."""
    driver = get_driver()
    driver.get(config.url)
    time.sleep(50)
    while True:
        print(type(config.like_xpath))
        print(config.like_xpath)
        try:
            driver.find_element(
                by=By.XPATH,
                value=config.like_xpath).click()
        except:
            traceback.print_exc()
        time.sleep(2)
    driver.close()


if __name__ == '__main__':
    main()
