# Great Expectations Tests

This repository contains tests using Great Expectations 1.5 to validate data quality in CSV files.

## Current Tests

- `test_order_id_not_null.py`: Validates that the `Order_ID` column in the orders dataset is never null.

## Project Structure

```
.
├── data/
│   └── orders.csv       # Orders dataset
├── great_expectations/  # Auto-generated when tests are run
└── test_order_id_not_null.py  # Test script
```

## Requirements

The project requires Python 3.12 and the following dependencies (specified in pyproject.toml):
- great-expectations >= 1.5
- pandas >= 2.1.1
- numpy == 1.26.4

## Running Tests

To run the Order ID validation test:

```bash
python test_order_id_not_null.py
```

The test will:
1. Create a Great Expectations context
2. Load the orders.csv data
3. Create an expectation suite with the rule that Order_ID should never be null
4. Validate the data against this expectation
5. Output the results

## Test Results

After running the test, the results will be displayed in the console. Additionally, Great Expectations will generate documentation in the `great_expectations/uncommitted/data_docs/local_site/` directory that can be viewed in a web browser.

## Extending Tests

To add more data quality tests:
1. Duplicate the existing test file
2. Modify the expectations to include your new validation rules
3. Run the new test file