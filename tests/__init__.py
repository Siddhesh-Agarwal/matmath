import unittest
import os


def load_tests(loader, tests, pattern):
    """
    Discovery and load all tests in the 'tests' directory.
    """
    suite = unittest.TestSuite()
    for test_file in os.listdir(os.path.dirname(__file__)):
        if test_file.startswith("test_") and test_file.endswith(".py"):
            module_name = f"tests.{test_file[:-3]}"
            suite.addTests(loader.loadTestsFromName(module_name))
    return suite


def run_all_tests():
    """
    Run all tests using unittest.main().
    """
    test_dir = os.path.dirname(__file__)
    loader = unittest.TestLoader()
    suite = loader.discover(test_dir, pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == "__main__":
    run_all_tests()
