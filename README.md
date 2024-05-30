# Data Pipeline Creation using Microsoft Fabric API

This Python script allows you to create a data pipeline in Microsoft Fabric using its API. It provides a simple interface to create pipelines with various configurations.

## Prerequisites

Before using this script, make sure you have:

- A Microsoft Fabric workspace ID.
- An API token with appropriate permissions to create data pipelines in the workspace.
- A JSON template specifying the configuration of the data pipeline.

## Usage

1. Clone or download this repository to your local machine.

2. Ensure you have Python installed on your system.

3. Install the required Python libraries using pip:
   
4. Modify the script `pipeline_api.py` with your workspace ID, API token, and JSON template file path.

5. Run the script: This will create the data pipeline in your Microsoft Fabric workspace using the provided JSON template.

## File Structure

- `pipeline_api.py`: The Python script to create the data pipeline.
- `API_testpl_template.json`: Example JSON template file for the data pipeline configuration.

## JSON Template

The `API_testpl_template.json` file contains the configuration for the data pipeline. Make sure to customize it according to your requirements before running the script.

