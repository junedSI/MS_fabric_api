import requests
import json

def create_data_pipeline(workspace_id, api_token, pipeline_template):
    url = f"https://api.fabric.microsoft.com/v1/workspaces/{workspace_id}/dataPipelines"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }

    response = requests.post(url, data=json.dumps(pipeline_template), headers=headers)

    if response.status_code == 201:
        print("Data pipeline created successfully.")
        return response.json()
    else:
        print(f"Failed to create data pipeline. Status code: {response.status_code}")
        print(response.text)
        return None

# Example usage:
workspace_id = "your_workspace_id"
api_token = "your_api_token"

# Load your JSON template from a file or define it directly
with open('API_testpl_template.json', 'r') as file:
    pipeline_template = json.load(file)

created_pipeline = create_data_pipeline(workspace_id, api_token, pipeline_template)
if created_pipeline:
    print("Created pipeline ID:", created_pipeline["id"])
