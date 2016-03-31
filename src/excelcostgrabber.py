import excel
import config
import costgrab
import sys
from urllib import parse


def getLinkValDict(sheet):
    linkVals = []
    for index in range(excel.columnLength(sheet, config.LinkColumn, start=config.StartRow)):
        currentRow = config.StartRow + index
        linkCell = config.LinkColumn + str(currentRow)
        priceCell = config.PriceColumn + str(currentRow)
        currentList = [parse.unquote(excel.trimVal(excel.getCell(sheet, linkCell))), priceCell]
        linkVals.append(currentList)
    return linkVals
def getAllPrices():
    for sheet in range(1, excel.sheetCount() + 1):
        linkVals = getLinkValDict(sheet)
        site = ""
        if(excel.getSheetName(sheet).lower() == "cdw"):
            site = "cdw"
        elif excel.getSheetName(sheet).lower() == "newegg":
            site = "newegg"
        elif excel.getSheetName(sheet).lower() == "pc connections":
            site = "pcon"
        elif excel.getSheetName(sheet).lower() == "pcm":
            site = "pcm"
        elif excel.getSheetName(sheet).lower() == "insight":
            site = "insight"
        elif excel.getSheetName(sheet).lower() == "provantage":
            site = "prov"
        elif excel.getSheetName(sheet).lower() == "zones":
            site = "zones"

        for index in range(len(linkVals)):
            cell = linkVals[index][1]
            link = linkVals[index][0]
            excel.setCell(sheet, cell, costgrab.Product.getPrice(link, site))

if __name__ == '__main__':
    getAllPrices()
