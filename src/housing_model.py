import pandas as pd
import requests

url = "https://drive.google.com/file/d/1bYuwuOtEJQbS-0gS7gx4M_WXkCuXri4x/view?usp=sharing"

# Pull the dowload link
url='https://drive.google.com/uc?id=' + url.split('/')[-2]

data = pd.read_csv(url)