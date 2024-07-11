# Gemini Explorer 

## Mission
Create a chat interface using Streamlit and Google Gemini to explore large language chat models and their applications. 

## Requirments:

- Python version 3.11 or above
- [Streamlit Documentation](https://docs.streamlit.io/)
- Google Cloud account
- [Vertexai Documentation](https://cloud.google.com/vertex-ai)

## Task 1: Enabling Google Cloud

- Go to the [Google Cloud Platform](console.cloud.google.com) and select "Get Started for free".
- Sign in using your Google Account and complete the billing requirements.
- Create a new project.
- Navigation -> Artificial Intelligence -> Vertex AI -> Enable All Recommended APIs


## Task 2: Google Cloud Initialization

- Install the Google SDK using this [link](https://cloud.google.com/sdk/docs/install).
- Run the following command to initialize the SDK:
  ```
  gcloud init
- Sign in using your Google Account credentials.
- Select an existing project or Create a new project


## Task 3: Setting up Google Gemini

- Install the streamlit framework
  ```
  pip install streamlit
- In the project, we are using Gemini Pro as the LLM.
- Use the project ID instead of the project name, like this: `project = "project_id"`. This helps avoid encountering a 403 permission denied error.

### Step-by-Step Installation Guide

1. **Clone the Repository**
   
   Start by cloning the repository to your local machine. Use the following command:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

## Set Up a Virtual Environment (Optional but recommended)

It's a good practice to create a virtual environment for your Python projects. This keeps your project dependencies isolated. If you have `virtualenv` installed, create a new environment with:

```bash
virtualenv venv
source venv/bin/activate
```

## Install Dependencies
Inside the virtual environment, install all necessary dependencies by running:
```bash
pip install -r requirements.txt
```

## Starting the FastAPI Server

After the installation, you can start the FastAPI server using Uvicorn. Navigate to the project directory and run:

```bash
uvicorn main:app
```

## Accessing the API
With the server running, you can access the API at `http://127.0.0.1:8000.`

For interactive API documentation, visit `http://127.0.0.1:8000/docs`, where you can test the API endpoints directly from your browser.
