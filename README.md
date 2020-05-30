# Test API for JPL
https://ssd-api.jpl.nasa.gov/cad.api

## Reporter
We use Allure for visual reports

### Install allure
* macOS *
`brew install allure`

### Collect test results for allure
```
timestamp=$(date +%Y-%m-%d_%H-%M-%S)
pytest --alluredir=/tmp/allure_results_$timestamp
```

### Serve tests results in the browser
`allure serve /tmp/allure_results_$timestamp`

### Analyze tests results
Now we can see that API works as expect
![Normal flight]("https://github.com/alekspog/jpl_api_example/blob/all_tests_passed.png")

If we have a problem we can see what steps in the scenarion is caused the error![Houston we have a problem]("https://github.com/alekspog/jpl_api_example/blob/some_wrong.png")

