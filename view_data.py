import pandas
import os
import webbrowser
data_table = pandas.read_csv("sample_New - sample.csv", index_col=None)
html = data_table.head().to_html()
with open("data.html","w") as f:
    f.write(html)

full_filename= os.path.abspath("data.html")
webbrowser.open("file://{}".format(full_filename))
