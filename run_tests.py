import unittest
from tests.test_home_page import TestHomePage
from tests.test_diary_page import TestDiaryPage
from tests.test_summary_page import TestSummaryPage
from tests.test_ai_classification import TestAIClassification

def run_tests():
    test_classes = [
        TestHomePage,
        TestDiaryPage,
        TestSummaryPage,
        TestAIClassification
    ]
    
    loader = unittest.TestLoader()
    suites = [loader.loadTestsFromTestCase(tc) for tc in test_classes]
    suite = unittest.TestSuite(suites)
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed.")

if __name__ == '__main__':
    run_tests()
