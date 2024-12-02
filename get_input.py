import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_input(day):
    cookies = {
    "session": os.environ.get('SESSION')
    }
    base_url = f"https://adventofcode.com/2024/day/{day}/input"
    response = requests.get(f'{base_url}', cookies=cookies)
    return response.text.rstrip()
