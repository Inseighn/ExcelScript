import excel
import priceparse

def main():
    for i in range(1, excel.sheet_count() + 1):
        link_price_dict = excel.get_all_links(i)
        if not link_price_dict:
            continue
        print(excel.get_sheet_name(i))
        for link, pricecell in link_price_dict.items():
            excel.set_cell_value(i, pricecell, priceparse.get_price(link, excel.get_sheet_name(i)))
if __name__ == "__main__":
        main()
