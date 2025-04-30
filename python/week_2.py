import os
import great_expectations as gx

# Set up context
context = gx.get_context()

# Create an Expectation Suite
suite = gx.ExpectationSuite(name="orders_suite")

# Define and add Expectations
expectations = [
    gx.expectations.ExpectColumnValuesToNotBeNull(column="Customer_ID"),
    gx.expectations.ExpectColumnValuesToBeUnique(column="Order_ID"),
]

for expectation in expectations:
    suite.add_expectation(expectation)

# Save the Expectation Suite
context.suites.add(suite)

# Load data and validate using the suite
batch = context.data_sources.pandas_default.read_csv(os.path.join(
    os.path.dirname(__file__),
    "orders.csv"
))
results = batch.validate(suite)

# Print results
print(results)