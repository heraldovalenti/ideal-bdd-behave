# Introduction
A simple but ideal project based on Python's Behave.

# Getting started
## Prerequisites
* Install Python and PyPI
* Install Google Chrome
* Download chromedriver from here: https://sites.google.com/a/chromium.org/chromedriver/downloads
* Pycharm: download Community version from here: https://www.jetbrains.com/pycharm/download/
* Execute the following: pip install -r required.modules 

## Running chromedriver
The project expects that chromedriver is running in server mode in port 9515, which is the default port.
Once downloaded and extracted, open a terminal where chromedriver package was extracted and just execute chromedriverto
start the server:
```commandline
./chromedriver
```
You should see some output similar to the following:
```commandline
Starting ChromeDriver 2.38.552518 (183d19265345f54ce39cbb94cf81ba5f15905011) on port 9515
Only local connections are allowed.
```

## Running project from the command line
Open a terminal on the root of this project and execute the following:
```commandline
behave
```
This will execute all the existing scenarios on the project and show you the results in the terminal output. 

## Running project with PyCharm
First, the project must be loaded:
1. Select "Open"
2. Navigate to the root of this project
3. Select the root folder to load the project.

### Executing a single scenario
To execute a single scenario just locate the associated unit test file, right click on it and select
*Run 'Unitests in unittest...'* from the contextual menu.

### Debugging a single scenario
The procedure to debug a single scenario is almost the same as running a single scenario. Just add some breakpoints in
the code, right click on the unit test file and select  *Debug 'Unitests in unittest...'* from the contextual menu.

# Adding new scenarios
Adding new scenarios can be done with these steps:
1. Creating a new .feature file and describe de scenario in Gherkin language.
2. Creating a new unit test class so the new scenario can be executed debugged. This new class needs to extend
base_test.py class, define a method named with the prefix "test_" that performs the execution and a "setUp" method which
defines the new scenario name, like the following example:
```python
import unittest

from features.base_test import BaseTest
class MyNewFeature(BaseTest):

    def setUp(self):
        self.feature_list = 'my_feature.feature'

    def test_scenario(self):
        self.execute_scenario()


if __name__ == '__main__':
    unittest.main()
```