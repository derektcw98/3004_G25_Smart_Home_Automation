#test generateModel with data.csv
import pandas as pd
from generateModel import generateModel
from pathlib import Path
import os

df = pd.read_csv('data.csv', header = None)
df.columns = ["day", "hour", "minute", "temperature", "humidity","light_state", "air_state", "aircon_temp", "room", "label"]
df = df.drop("light_state", axis = 1)
df = df.drop("air_state", axis = 1)

generateModel("testRoom", df)
