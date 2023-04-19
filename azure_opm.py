import os
import openai
import requests
from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient
from azure.mgmt.monitor import MonitorManagementClient
from msrestazure.azure_exceptions import CloudError
from datetime import datetime, timedelta
from azure.mgmt.resource import ResourceManagementClient

# Set up Azure credentials
credential = DefaultAzureCredential()

subscription_id = "your subscription "
resource_group = "your subscription resource group"
resource_uri = f"/subscriptions/{subscription_id}/resourceGroups/{resource_group}"

# Set up Azure Cost Management client
cost_management_client = CostManagementClient(credential, subscription_id)

# Set up Azure Monitor client
monitor_client = MonitorManagementClient(credential, subscription_id)

# Set up OpenAI API
openai.api_key = "your open ai api key"
def get_azure_cost_data():
    # Call Azure Cost Management API to get cost data
    # ...

    # Process the cost data and return a readable summary
    summary = "..."
    return summary

def get_resources():
    # Instantiate the ResourceManagementClient
    resource_client = ResourceManagementClient(credential, subscription_id)

    # Specify the target region
    target_region = "East US"

    # List resources in the target region
    resources = resource_client.resources.list(
        filter=f"location eq '{target_region}'"
    )
    return resources

def get_azure_usage_data(resources):
    # Define the time range for the usage data
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=7)

    # Call Azure Monitor API to get usage data
    metrics_data_list = []
    for resource in resources:
        try:
            metrics_data = monitor_client.metrics.list(
                resource.id,
                timespan=f"{start_time}/{end_time}",
                interval="PT1H",
                metricnames="Percentage CPU",
                aggregation="Average",
                metricnamespace="Microsoft.Compute/virtualMachines"
            )
            metrics_data_list.append(metrics_data)
        except CloudError as e:
            print(f"Error: {e}")

    # Process the usage data and return a readable summary
    summary = "..."
    return summary, metrics_data_list
def get_chatgpt_recommendations(cost_summary, usage_summary):
    prompt = f"Based on the following Azure cost and usage data, provide recommendations for better cloud usage:\n\nCost Data:\n{cost_summary}\n\nUsage Data:\n{usage_summary}\n\nRecommendations:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

# Main program
if __name__ == "__main__":
    resources = get_resources()
    cost_summary = get_azure_cost_data()
    usage_summary, metrics_data_list = get_azure_usage_data(resources)
    recommendations = get_chatgpt_recommendations(cost_summary, usage_summary)

    print("Azure Cost Data:")
    print(cost_summary)
    print("\nAzure Usage Data:")
    print(usage_summary)
    print("\nFinOPsGPT Cloud Recommendations:")
    print(recommendations)
   
