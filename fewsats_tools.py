from llama_index.core.tools import FunctionTool
import subprocess

def search_file() -> str:
    """
    Search for files using the fewsatscli storage search command.
    
    
    Returns:
    dict: The search results as a dictionary.
    """
    result = subprocess.run(
        ['fewsatscli', 'storage', 'search'],
        capture_output=True, text=True
    )
    return result.stdout


def download_file(file_id: str) -> str:
    """
    Download a file using the fewsatscli storage download command.
    
    Args:
    file_url (str): The URL from which to download the file.
    
    Returns:
    str: The content of the downloaded file.
    """
    result = subprocess.run(
        ['fewsatscli', 'storage', 'download', file_id],
        capture_output=True, text=True
    )
    return result.stdout


def upload_file(file_name: str, file_path: str, price: float, description: str) -> str:
    """
    Upload a file using the fewsatscli storage upload command.
    
    Args:
        file_name (str): The name under which the file will be stored.
        file_path (str): The local path to the file.
        price (float): The price to set for the file.
        description (str): A description of the file.
    
    Returns:
        dict: The result of the upload operation as a dictionary.
    """
    command = [
        'fewsatscli', 'storage', 'upload',
        '--name', file_name,
        '--price', str(price),
        '--file-path', file_path,
        '--description', description
    ]

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Upload failed: {result.stderr}")
    return result.stdout


def create_fewsats_tools():
    """
    Create tools related to fewsatscli operations: search, download, and upload.
    
    Returns:
        tuple: A tuple containing the search, download, and upload tools.
    """
    search_tool = FunctionTool.from_defaults(
        name="search_tool",
        fn=search_file,
        description="Searches for files in the storage."
    )

    download_tool = FunctionTool.from_defaults(
        name="download_tool",
        fn=download_file,
        description="Downloads a file from a given URL."
    )

    upload_tool = FunctionTool.from_defaults(
        name="upload_tool",
        fn=upload_file,
        description="Uploads a file to storage with pricing and description."
    )

    return search_tool, download_tool, upload_tool