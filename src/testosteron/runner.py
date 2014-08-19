import unittest


class TestRunner(object):

    def __init__(self, manager, verbosity=1):
        self.manager = manager
        self.verbosity = verbosity
        self.loader = unittest.TestLoader()

    def create_suite(self):
        test_cases = [
            self.loader.loadTestsFromTestCase(test_case)
            for test_case in self.get_tests()
        ]
        return unittest.TestSuite(test_cases)

    def get_tests(self):
        return self.manager.get_all()

    def __call__(self):
        suite = self.create_suite()
        unittest.TextTestRunner(verbosity=self.verbosity).run(suite)
