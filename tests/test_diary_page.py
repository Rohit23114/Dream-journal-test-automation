import unittest
from config import get_driver, get_wait, BASE_URL

class TestDiaryPage(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.wait = get_wait(self.driver)
    
    def test_dream_entries_count(self):
        self.driver.get(BASE_URL + "dreams-diary.html")
        dreams = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "table#dreamTable tbody tr")))
        self.assertEqual(len(dreams), 10)
    
    def test_dream_entry_contents(self):
        self.driver.get(BASE_URL + "dreams-diary.html")
        dreams = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "table#dreamTable tbody tr")))
        
        good, bad = 0, 0
        for dream in dreams:
            cols = dream.find_elements(By.TAG_NAME, "td")
            self.assertEqual(len(cols), 3)
            
            name, days, type_ = cols[0].text, cols[1].text, cols[2].text
            self.assertTrue(all([name, days, type_]))
            
            if type_ == "Good":
                good += 1
            elif type_ == "Bad":
                bad += 1
            else:
                self.fail(f"Invalid dream type: {type_}")
    
    def tearDown(self):
        self.driver.quit()
