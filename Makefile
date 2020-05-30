SHELL := /bin/bash

docker-build:
	@docker build -t "jbl_tests" -f Dockerfile .

run-tests:
	rm -rf /tmp/allure_results
	docker run -v /tmp/allure_results:/app/allure_results jbl_tests pytest -v --gherkin-terminal-reporter --alluredir=/app/allure_results || echo "There were failing tests!"

run-tests-locally:
	rm -rf /tmp/allure_results
	pytest -v --gherkin-terminal-reporter --alluredir=/tmp/allure_results

build-and-run-tests: docker-build run-tests

serve-report:
	docker run -d -p 4040:4040 -p 5050:5050 -e CHECK_RESULTS_EVERY_SECONDS=3 -e KEEP_HISTORY="TRUE" -v /tmp/allure_results:/app/allure-results frankescobar/allure-docker-service:2.13.3

serve-report-locally:
	allure generate --clean /tmp/allure_results -o /tmp/allure_report
	allure open /tmp/allure_report
