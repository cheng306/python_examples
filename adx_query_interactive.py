from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from azure.kusto.data.helpers import dataframe_from_result_table
from azure.identity import InteractiveBrowserCredential

# Azure Data Explorer (ADX) cluster and database details
cluster = 'https://your-cluster.kusto.windows.net'
database = 'your-database'

# Authenticate using InteractiveBrowserCredential
credential = InteractiveBrowserCredential()
token = credential.get_token("https://kusto.kusto.windows.net/.default").token

# Create a connection string with the token
kcsb = KustoConnectionStringBuilder.with_aad_user_token_authentication(cluster, token)

# Create a Kusto client
client = KustoClient(kcsb)

# Define your KQL query
query = "Your Kusto Query Language (KQL) query here"

# Execute the query
response = client.execute(database, query)

# Convert the response to a pandas DataFrame
df = dataframe_from_result_table(response.primary_results[0])

# Display the DataFrame
print(df)
