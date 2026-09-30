
from csv_reader import *

def main():
    append_to_csv(file_destination="../data/transactions.csv", data_rows=[["Orlen", 5, 55.20, 0, "20/04/2025"], ["PZU", 15, 20.00, 0, "20/04/2025"]])
    arr = read_from_csv(file_destination="../data/transactions.csv")
    print(arr)

    portfolio_data = read_from_csv(file_destination="../data/portfolio.csv")
    print(portfolio_data)
    if (portfolio_data == []):
        print("empty")
    else:
        print("full")

    dictionary = {}
    for row in arr:
        if row[0] in dictionary.keys():
            
            if "amount" in dictionary[row[0]].keys():
                dictionary[row[0]]["amount"] += float(row[1])
            else:
                dictionary[row[0]]["amount"] = float(row[1])
        else:
            dictionary[row[0]] = {}
        print(dictionary)

main()