NOTE TO REVIEWER: 
- I have used playwright framework with pytest for UI tests, and just pytest framework for API tests. 
- All tests written are functional
- deally I would also write tests for data correctness against actual datastore
- If not already covered in unit tests by developers, I would also write schema validations for each API

SETUP ENV:
- clone the repo
- go to the repo on your terminal
- create a python virtual environment using command : python3 -m venv newenv
- activate the virtual environment : source newenv/bin/activate
- install requirements: pip3 install -r requirements.txt
- install playwright drivers: playwright install

RUN TESTS:
- command to run all ui and api tests together: pytest
- command to run just api tests: pytest -m api
- command to run just ui tests: pytest -m ui

REPORT:
- Whenever the tests will be run, a report.html will be generated in the directory from where tests are run (in this case the root repo directory)
- you can open the report using any browser of your choice. (open report.html) command will open it in default browser.
