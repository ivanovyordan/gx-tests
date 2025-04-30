import os
import great_expectations as gx

context = gx.get_context()

batch = context.data_sources.pandas_default.read_csv(os.path.join(
    os.path.dirname(__file__),
    "orders.csv"
))

expectation = gx.expectations.ExpectColumnValuesToNotBeNull(column="Customer_ID")

validation_results = batch.validate(expectation)

print(validation_results)