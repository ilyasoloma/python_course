def EraseStopWord(string):
    stopList = ['Python', 'php', 'go', 'C']
    for word in stopList:
        string = string.replace(word,'')
    return string


string = "Test C string php go"
print(EraseStopWord(string))