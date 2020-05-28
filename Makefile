docker-build:
	@docker build -t "jbl_tests" -f Dockerfile .

run-tests:
	@docker run jbl_tests pytest -s --tb=auto
