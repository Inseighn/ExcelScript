import os
from xlwings import Workbook, Range, Sheet
from pathlib import Path
import config

cwd = Path(__file__).parent.parent
wb = Workbook(str(cwd) + config.ExcelFile)

def sheetCount():
    return Sheet.count()
def columnLength(sheet, column, start=1):
    col = Range(Sheet(sheet), column + str(start)).vertical.value
    return len(col)

def setCell(sheet, cell, value):
    currentCell = Range(Sheet(sheet), cell)
    if __debug__:
        print('Setting Cell:' + cell + 'in sheet ' + Sheet(sheet).name + '->' + str(value))
    if currentCell and value:
        try:
            currentCell.value = str(value)
        except:
            if __debug__:
                print ('Error with value: ' + value)
def getSheetName(index):
    if Sheet(index):
        return Sheet(index).name;
def getCell(sheet, cell):
    currentCell = Range(Sheet(sheet), cell)
    if(currentCell):
        return currentCell.value

def trimList(list):
    return [cell.replace("\xa0", "") if "\xa0" in cell else cell for cell in list]
def trimVal(value):
    return value.replace("\xa0", "")
