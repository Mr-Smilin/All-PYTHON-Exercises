# -*- coding: utf-8 -*-

import xlrd

book=xlrd.open_workbook('data.xlsx')
sheet=book.sheets()[0]

nrows=sheet.nrows

ncols=sheet.ncols

data=(ur"").encode('utf-8')

data2=[[0 for i in range(ncols)] for j in range(nrows)]

for i in range(0,nrows):
    for j in range(0,ncols):
        if type(sheet.cell(i,j).value) == float :
            data2[i][j]=sheet.cell(i,j).value
            data=data+str(data2[i][j])
        else:
            data2[i][j]=(sheet.cell(i,j).value).encode('utf-8')
            data=data+data2[i][j]
    data=data+'\n'
        
            

        
#data=print(str(data).decode('string_escape'))
   

        
