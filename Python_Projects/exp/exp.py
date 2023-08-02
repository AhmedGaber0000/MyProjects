import pdfkit
import pandas as pd

df = pd.read_csv('ahmed.csv')
html_table = df.to_html()

print(html_table)