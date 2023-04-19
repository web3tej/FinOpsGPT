import boto3
import openai
import json
from datetime import datetime, timedelta

# Set up AWS connection
# your AWS access details here, do not push the build with keys.
session = boto3.Session(
    aws_access_key_id="<your access key id>",
    aws_secret_access_key="<your secret access key",
    region_name="us-east-1"
)

ce = session.client("ce")
cw = session.client("cloudwatch")

# Set up OpenAI API
openai.api_key = "your Open AI API key"

# Function to fetch AWS cost data
def get_aws_cost_data():
    # Call AWS Cost Explorer API to get cost data
    # ...

    # Process the cost data and return a readable summary
    summary = "..."
    return summary

# Function to fetch AWS usage data
def get_aws_usage_data():
    # Define the time range for the usage data
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=7)

    # Call AWS CloudWatch API to get usage data
    response = cw.get_metric_data(
        MetricDataQueries=[
            {
                "Id": "m1",
                "MetricStat": {
                    "Metric": {
                        "Namespace": "AWS/EC2",
                        "MetricName": "CPUUtilization",
                        "Dimensions": [
                            {
                                "Name": "InstanceId",
                                "Value": "YOUR_INSTANCE_ID"
                            }
                        ]
                    },
                    "Period": 3600,
                    "Stat": "Average"
                },
                "ReturnData": True
            }
        ],
        StartTime=start_time,
        EndTime=end_time
    )

    # Process the usage data and return a readable summary
    summary = "..."
    return summary

# Function to get recommendations from ChatGPT
def get_chatgpt_recommendations(cost_summary, usage_summary):
    prompt = f"Based on the following AWS cost and usage data, provide recommendations for better cloud usage:\n\nCost Data:\n{cost_summary}\n\nUsage Data:\n{usage_summary}\n\nRecommendations:"

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
    cost_summary = get_aws_cost_data()
    usage_summary = get_aws_usage_data()
    recommendations = get_chatgpt_recommendations(cost_summary, usage_summary)

    print("AWS Cost Data:")
    print(cost_summary)
    print("\nAWS Usage Data:")
    print(usage_summary)
    print("\nFinOps-GPT Recommendations:")
    print(recommendations)
