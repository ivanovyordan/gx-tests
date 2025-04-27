import great_expectations as gx

context = gx.get_context()

file_path = "data/orders.csv"
batch = context.data_sources.pandas_default.read_csv(file_path)

expectation = gx.expectations.ExpectColumnValuesToNotBeNull(column="Customer_ID")

validation_results = batch.validate(expectation)

print(validation_results)