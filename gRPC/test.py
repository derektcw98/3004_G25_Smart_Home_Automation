from tkinter.ttk import Separator
import pandas as pd
from io import StringIO
from pathlib import Path
import os


stringline = "nagl,273,234,766"
a=stringline.split(',')[-1]
print(a)