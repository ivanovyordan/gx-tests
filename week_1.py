import great_expectations as gx

# Initialize Great Expectations context
context = gx.get_context()

# Define the source folder and data source name
source_folder = "./data"
data_source_name = "orders_data_source"
data_source = context.data_sources.add_pandas_filesystem(
    name=data_source_name,
    base_directory=source_folder
)

# Define the asset name and add the CSV file as an asset
asset_name = "orders_csv_file"
file_data_asset = data_source.add_csv_asset(name=asset_name)

# Define the batch definition name and path
batch_definition_name = "orders.csv"
batch_definition_path = "orders.csv"
batch_definition = file_data_asset.add_batch_definition_path(
    name=batch_definition_name,
    path=batch_definition_path
)

# Get the batch
batch = batch_definition.get_batch()
print(batch.head())