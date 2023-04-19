import boto3
import openai
import json

# Set up AWS connection
# your AWS access details here, do not push the build with keys.
session = boto3.Session(
    aws_access_key_id="your access key id",
    aws_secret_access_key="your secret access key",
    region_name="us-east-1"
)

ce = session.client("ce")

# Set up OpenAI API
openai.api_key = "your open AI key"

# Function to fetch AWS cost data
def get_aws_cost_data():
    # Call AWS Cost Explorer API to get cost data
    # ...

    # Process the cost data and return a readable summary
    summary = "..."
    return summary

# Function to get recommendations from ChatGPT
def get_chatgpt_recommendations(cost_summary):
    prompt = f"Based on the following AWS cost data, provide recommendations for better cloud usage:\n\n{cost_summary}\n\nRecommendations:"

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
    recommendations = get_chatgpt_recommendations(cost_summary)

    print("AWS Cost Data:")
    print(cost_summary)
    print("\nFinOPs GPT Recommendations:")
    print(recommendations)
