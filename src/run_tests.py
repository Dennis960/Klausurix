import unittest

if __name__ == '__main__':
    # Discover all tests in the 'tests' folder
    loader = unittest.TestLoader()
    tests = loader.discover('tests', pattern='test_*.py')

    # Create a test runner
    runner = unittest.TextTestRunner()

    # Run the tests
    runner.run(tests)
