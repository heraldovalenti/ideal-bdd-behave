import json
import unittest
import os
import json2html
import glob
from behave import __main__ as runner_with_options


class SimtlixJobsFeature(unittest.TestCase):

    def setUp(self):
        self.feature_list = 'simtlix_jobs.feature'
        self.report_folder = '../allure-reports'

    def test_scenario(self):
        args = self.feature_list
        if self.report_folder:
            args = args + ' -f allure_behave.formatter:AllureFormatter -o ' + self.report_folder
        runner_with_options.main(args)

    def tearDown(self):
        json_files = glob.glob(self.report_folder + "/*.json")
        final_json = []
        for json_file in json_files:
            json_string = open(json_file, 'r').read()
            json_data = json.loads(json_string)
            final_json.append(json_data)
            os.remove(json_file)
        html_content = json2html.json2html.convert(final_json)
        html_report_file = open(self.report_folder + '/' + 'index.html', 'w')
        html_report_file.write(html_content)
        html_report_file.close()


if __name__ == '__main__':
    unittest.main()
