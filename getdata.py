import os
import sys
import json

# from dotenv import load_dotenv # type: ignore
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv('MONGODB_URL')
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np




