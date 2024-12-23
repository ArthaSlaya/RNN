import os

# Define the expected folder structure
folders = [
    "data/raw",                        # For raw datasets
    "data/processed",                  # For processed datasets
    "data/embeddings",                 # For pretrained embeddings
    "pipelines",                   # For ZenML pipeline definitions
    "steps",                       # For pipeline steps
    "deployment/app",                  # For deployment scripts
    "streamlit_app/components",        # For Streamlit web app components
    "models",                          # For saved models
    "logs",                            # For logs
]

# Function to check and create folders
def verify_and_create_folders(folders: list) -> None:
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(name= folder, exist_ok= True)
            print(f"Created folder: {folder}")
        else:
            print(f"Folder already exists: {folder}")

print("Verifying project folder structure...")
verify_and_create_folders(folders)
print("Folder structure verification complete!")
