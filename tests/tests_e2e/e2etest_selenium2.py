import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import warnings



class ChromeSearch(unittest.TestCase):

    def setUp(self):
        # configuration du navigateur
        self.driver = webdriver.Chrome()

    def teste2e_search_in_python_org(self):
        warnings.simplefilter("ignore", ResourceWarning)
        driver = self.driver
        # appel de la page de démarrage du scénario
        driver.get("http://tpinfo.go.yj.fr/")
        self.assertIn("TP info 1", driver.title)
        elem = driver.find_element("name","login")
        elem.send_keys("captain")
        elem = driver.find_element("name","motdepasse")
        elem.send_keys("america")
        elem.send_keys(Keys.RETURN)
        assert "http://tpinfo.go.yj.fr/contenu.php?action=test" == driver.current_url

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()