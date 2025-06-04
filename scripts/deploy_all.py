import os
import glob
import subprocess

def fab_authenticate_spn(client_id, client_secret, tenant_id):
    """
    Authenticate the SPN using ms-fabric-cli.
    """
    print("Authenticating SPN...")
    command = f"fab auth login -u {client_id} -p {client_secret} --tenant {tenant_id}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Authentication failed: {result.stderr}")
    print("SPN authenticated successfully.")

def deploy_item(file_path, workspace_name):
    """
    Deploy a single item to the workspace using ms-fabric-cli.
    """
    print(f"Deploying {file_path} to workspace {workspace_name}...")
    if file_path.endswith(".SemanticModel"):
        command = f"fab semanticmodel deploy -f {file_path} -w {workspace_name}"
    elif file_path.endswith(".Report"):
        command = f"fab report deploy -f {file_path} -w {workspace_name}"
    elif file_path.endswith(".PaginatedReport"):
        command = f"fab paginatedreport deploy -f {file_path} -w {workspace_name}"
    elif file_path.endswith(".Dataflow"):
        command = f"fab dataflow deploy -f {file_path} -w {workspace_name}"
    else:
        print(f"Unsupported file type: {file_path}")
        return

    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Failed to deploy {file_path}: {result.stderr}")
    print(f"Successfully deployed {file_path}.")

def deploy_all(src_folder, workspace_name, client_id, client_secret, tenant_id):
    """
    Deploy all supported Power BI items in the src folder to the target workspace.
    """
    # Authenticate SPN
    fab_authenticate_spn(client_id, client_secret, tenant_id)

    # Verify workspace exists
    print(f"Ensuring workspace {workspace_name} exists...")
    command = f"fab workspace create -n {workspace_name} -c none"
    subprocess.run(command, shell=True, capture_output=True, text=True)

    # Find and deploy all items in src folder
    supported_extensions = [".SemanticModel", ".Report", ".PaginatedReport", ".Dataflow"]
    for extension in supported_extensions:
        for file_path in glob.glob(os.path.join(src_folder, f"*{extension}")):
            deploy_item(file_path, workspace_name)

if __name__ == "__main__":
    # Configuration
    SRC_FOLDER = "src"
    BASE_WORKSPACE_NAME = os.getenv("WORKSPACE_NAME")  # Variable from GitHub Actions
    BRANCH_NAME = os.getenv("GITHUB_REF_NAME")  # GitHub Actions branch name

    if not BASE_WORKSPACE_NAME:
        raise Exception("WORKSPACE_NAME is not set in environment variables.")
    if not BRANCH_NAME:
        raise Exception("GITHUB_REF_NAME is not set in environment variables.")

    # Determine workspace name based on branch
    if BRANCH_NAME == "develop":
        WORKSPACE_NAME = f"{BASE_WORKSPACE_NAME}_DEV"
    elif BRANCH_NAME == "main":
        WORKSPACE_NAME = f"{BASE_WORKSPACE_NAME}_PRD"
    else:
        raise Exception(f"Unsupported branch: {BRANCH_NAME}")

    CLIENT_ID = os.getenv("FABRIC_CLIENT_ID")
    CLIENT_SECRET = os.getenv("FABRIC_CLIENT_SECRET")
    TENANT_ID = os.getenv("FABRIC_TENANT_ID")

    if not CLIENT_ID or not CLIENT_SECRET or not TENANT_ID:
        raise Exception("SPN credentials are not set in environment variables.")

    deploy_all(SRC_FOLDER, WORKSPACE_NAME, CLIENT_ID, CLIENT_SECRET, TENANT_ID)