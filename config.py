import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

URL = os.environ.get('URL')

