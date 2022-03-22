import dotenv
import os
import pathlib
import requests
import subprocess

# Load environment variables from .env
dotenv.load_dotenv()

# Get codecov uploader
url = os.environ.get('codecov_uploader_url')
filename = 'codecov.exe'
request = requests.get(url, allow_redirects=True)
with open(filename, 'wb') as outfile:
    outfile.write(request.content)

# Run uploader
arguments = [
    filename,
    '-t',
    os.environ.get('codecov_token')
]
subprocess.run(arguments)

# Remove uploader
pathlib.Path(filename).unlink(missing_ok=True)
