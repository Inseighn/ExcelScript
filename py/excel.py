import os
from xlwings import Workbook, Range, Sheet
from pathlib import Path
import config

cwd = Path(__file__).parent.parent
wb = Workbook(str(cwd) + config.ExcelFile)

def sheet_count():
    return Sheet.count()

def get_all_links(sheet):
    links = Range(Sheet(sheet), config.LinkColumn + str(config.StartRow)).vertical.value
    if not links:
        return None
    link_key_dict = {}
    for index in range(len(links)):
        link_key_dict[links[index]] = config.PriceColumn + str(config.StartRow + index)
    return link_key_dict

def set_cell_value(sheet, cell, value):
    currentCell = Range(Sheet(sheet), cell)
    if currentCell:
        currentCell.value = value
def get_sheet_name(index):
    if Sheet(index):
        return Sheet(index).name;
