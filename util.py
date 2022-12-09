def createDataArr(file):
    data = file.read_text()
    return data.split('\n')