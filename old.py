import pandas
import os

pathFile = os.getcwd() + os.getenv("pathfile")
dados = pandas.read_excel(pathFile)

def getArrayData(dados: object, column: str) -> list:
    data = pandas.DataFrame(dados, columns=[column])
    return pandas.array(data)

def getIndex(toFind: str, hasAccent: bool) -> str:
    toSearch = getToSearch(hasAccent)
    start = toFind.find(toSearch[0]) + 1
    limit = toFind.find(toSearch[1], start)
    return toFind[start:limit]

def getToSearch(hasAccent: bool) -> list:
    return ['[', ']'] if not hasAccent else ['\'', '\'']

def treatExcelData(array: list) -> list:
    data_treated = []
    for data in array:
        toFind = data[0]
        hasAccent = toFind.find('\'') != -1
        data_treated.append(getIndex(toFind, hasAccent))
    
    return data_treated

def getExcelDataList(idList: list, descList: list) -> list[dict]:
    data = []
    id = treatExcelData(idList)
    desc = treatExcelData(descList)
    for i in range(0, len(treatExcelData(idList))):
        data.append({"id": id[i], "desc": desc[i]})
    return data

def getData(dados) -> list:
    idList = getArrayData(dados, 'id')
    descList = getArrayData(dados, 'desc')
    return getExcelDataList(idList, descList)

ciap2 = getData(dados)
print(ciap2)
