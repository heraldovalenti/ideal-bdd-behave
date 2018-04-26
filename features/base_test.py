import unittest
from behave import __main__ as runner_with_options


class BaseTest(unittest.TestCase):

    def execute_scenario(self):
        args = self.feature_list
        if hasattr(self, 'report_folder'):
            args = args + ' -f allure_behave.formatter:AllureFormatter -o ' + self.report_folder
        runner_with_options.main(args)
