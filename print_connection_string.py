import os

def print_connection_string():
    # Fetch the connection string from environment variables
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    
    if connection_string:
        print(f"Your Azure Storage Connection String is: {connection_string}")
    else:
        print("Azure Storage Connection String not found in environment variables.")

if __name__ == "__main__":
    print_connection_string()
