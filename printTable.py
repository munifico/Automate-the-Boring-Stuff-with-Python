tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)
    
    count = 0
    while count < len(tableData):
        for item in tableData[count]:
            if len(item) > colWidths[count]:
                colWidths[count] = len(item)
        count += 1

    print(colWidths)
    print()
    
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end=' ')
            #resultData = tableData[j][i].join(' ')
            #print(resultData)
        print()

printTable()