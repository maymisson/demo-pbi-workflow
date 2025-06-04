'''Pass the required SPN values directly into the credential object, does not require AZ PowerShell or AZ CLI'''

from pathlib import Path
import os
from azure.identity import ClientSecretCredential
from fabric_cicd import FabricWorkspace, publish_all_items

# Assumes your script is one level down from root
root_directory = Path(__file__).resolve().parent

# Sample values for FabricWorkspace parameters
workspace_id = os.getenv("FABRIC_WORKSPACE_ID")

print(f"Worspace ID: {workspace_id}")

# workspace_id = "81d945d2-a268-431b-a614-1be6911f4fa7"
repository_directory = "C:/workspace/Labs/demo-pbi-workflow/src/"
item_type_in_scope = ["SemanticModel", "Report"]

# Use Azure CLI credential to authenticate
client_id = os.getenv("FABRIC_CLIENT_ID")
client_secret = os.getenv("FABRIC_CLIENT_SECRET")
tenant_id = os.getenv("FABRIC_TENANT_ID")

print(f"Client ID: {client_id}")
print(f"Client Secret: {client_secret}")
print(f"Tenant ID: {tenant_id}")

# client_id = "335db6b4-24e7-4533-aa73-6cc740d36404"
# client_secret = "Meu8Q~qIPzyaEzTkKW7PYR.LKLCgYBWDI72ONdbj"
# tenant_id = "852dfdbb-be73-4699-8c7e-23895b6f9d26"
token_credential = ClientSecretCredential(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)

# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id=workspace_id,
    repository_directory=repository_directory,
    item_type_in_scope=item_type_in_scope,
    token_credential=token_credential,
)

# Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)
