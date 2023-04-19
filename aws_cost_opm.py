import boto3
import openai
import json

# Set up AWS connection
session = boto3.Session(
    aws_access_key_id="AKIAT4TUZVK5F3EWUPPL",
    aws_secret_access_key="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",
    region_name="us-east-1"
)

ce = session.client("ce")

# Set up OpenAI API
openai.api_key = "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"

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
    print("\nOptimism Cloud Recommendations:")
    print(recommendations)
