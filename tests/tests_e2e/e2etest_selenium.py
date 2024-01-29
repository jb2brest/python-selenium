import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import warnings



class ChromeSearch(unittest.TestCase):

    def setUp(self):
        # configuration du navigateur
        self.driver = webdriver.Chrome()
        ChromeOptions options = new ChromeOptions();
        options.addArguments("start-maximized"); // open Browser in maximized mode
        options.addArguments("disable-infobars"); // disabling infobars
        options.addArguments("--disable-extensions"); // disabling extensions
        options.addArguments("--disable-gpu"); // applicable to windows os only
        options.addArguments("--disable-dev-shm-usage"); // overcome limited resource problems
        options.addArguments("--no-sandbox"); // Bypass OS security model
        WebDriver driver = new ChromeDriver(options);

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
