import pandas
import os

pathFile = os.getcwd() + os.getenv("pathfile")
dados = pandas.read_excel(pathFile)

data = []
for i in range(0, len(dados["id"])):
    data.append({"id": dados["id"][i], "desc": dados["desc"][i]})

print(data)