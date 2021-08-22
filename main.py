from array import array


column, row = 4, 11
array2D = [[0 for Row in range(row-4)],
[0 for Row in range(row-1)],
[0 for Row in range(row-1)],
[0 for Row in range(row)]]
col2=[10]
col3=[10]
col4=[11]
Count=1
mk=1

for Row in range(len(array2D)):
    for Col in range(len(array2D[Row])):
        temp=str(Count)
        if Count<10:temp='0'+temp
        array2D[Row][Col]=temp
        Count+=mk
        if Row==0 and Col>5:
            break
        if Row==1 and Col>8:
            break
        if Row==2 and Col>8:
            break
    if mk>0:mk=-1
    else:mk=1
    if(Row<3):Count+=len(array2D[Row+1])+mk
    print(array2D[Row])
print(array2D[-1])