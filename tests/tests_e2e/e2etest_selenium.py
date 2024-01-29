import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


import warnings



class ChromeSearch(unittest.TestCase):

    def setUp(self):
        # configuration du navigateur
        chrome_options = Options()
        chrome_options.add_argument("start-maximized"); # open Browser in maximized mode
        chrome_options.add_argument("disable-infobars"); # disabling infobars
        chrome_options.add_argument("--disable-extensions"); # disabling extensions
        chrome_options.add_argument("--disable-gpu"); # applicable to windows os only
        chrome_options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
        chrome_options.add_argument("--no-sandbox"); # Bypass OS security model
        self.driver = webdriver.Chrome(options=chrome_options)

    def teste2e_search_in_python_org(self):
        warnings.simplefilter("ignore", ResourceWarning)
        driver = self.driver
        # appel de la page de démarrage du scénario
        driver.get("https://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element("name","q")
        elem.send_keys("getting started with python")
        elem.send_keys(Keys.RETURN)
        assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == driver.current_url

    def teste2e_search_in_python_org_2(self):
        warnings.simplefilter("ignore", ResourceWarning)
        driver = self.driver
        # appel de la page de démarrage du scénario
        driver.get("https://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element("name","q")
        elem.send_keys("getting started with python")
        elem.send_keys(Keys.RETURN)
        assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == driver.current_url

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
