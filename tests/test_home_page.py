import unittest
import time
from config import get_driver, get_wait, BASE_URL

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.wait = get_wait(self.driver)
    
    def test_home_page_loading(self):
        self.driver.get(BASE_URL)
        
        # Test loading animation
        loader = self.wait.until(
            EC.visibility_of_element_located((By.ID, "loader")))
        time.sleep(3)
        self.assertFalse(loader.is_displayed())
        
        # Test main content
        content = self.wait.until(
            EC.visibility_of_element_located((By.ID, "mainContent")))
        self.assertTrue(content.is_displayed())
    
    def test_my_dreams_button(self):
        self.driver.get(BASE_URL)
        button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "myDreamsBtn")))
        button.click()
        self.assertEqual(len(self.driver.window_handles), 3)
    
    def tearDown(self):
        self.driver.quit()
