from csv_reader import *
from decimal import Decimal, ROUND_HALF_UP

def main():
    append_to_csv(file_destination="../data/transactions.csv", data_rows=[["Orlen", 5, 55.20, 0, "20/04/2025"], ["PZU", 15, 20.00, 0, "20/04/2025"],["XTB", 30, 30.00, 0, "20/04/2026"]])
    arr = read_from_csv(file_destination="../data/transactions.csv")
    portfolio_data = read_from_csv(file_destination="../data/portfolio.csv")
    dictionary = {}
    for row in arr:
        if row[0] not in dictionary.keys():
            dictionary[row[0]] = {}
        if row[0] in dictionary.keys():           
            if "amount" in dictionary[row[0]].keys():
                dictionary[row[0]]["amount"] = (dictionary[row[0]]["amount"] + Decimal(row[1])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            else:
                dictionary[row[0]]["amount"] = Decimal(row[1])
            if "price" in dictionary[row[0]].keys():
                dictionary[row[0]]["price"] = (dictionary[row[0]]["price"] + Decimal(row[2])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            else:
                dictionary[row[0]]["price"] = Decimal(row[2])
            if "provision" in dictionary[row[0]].keys():
                dictionary[row[0]]["provision"] = (dictionary[row[0]]["provision"] + Decimal(row[3])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            else:
                dictionary[row[0]]["provision"] = Decimal(row[3])
    write_to_csv(file_destination="../data/portfolio.csv",data_rows=dictionary)

main()