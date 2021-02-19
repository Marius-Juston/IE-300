import csv
import os

if __name__ == '__main__':
    in_file = open('LabDemo.csv', 'r')
    csv_file = csv.reader(in_file, delimiter=',')

    new_line = os.linesep

    next(csv_file)

    customers = dict()
    stock_options = set()

    for line in csv_file:
        cust, stock, price = line[0], line[1], float(line[3])

        if cust not in customers:
            customers[cust] = {}

        if stock not in customers[cust]:
            customers[cust][stock] = []

        customers[cust][stock].append(price)
        stock_options.add(stock)

    stock_options = list(sorted(stock_options))

    with open("CustomerSummary.txt", 'w') as out_file:
        for name in sorted(customers.keys()):
            out_file.write(f"Customer: {name}")
            out_file.write('\n')

            for stock in stock_options:
                output = None

                if stock not in customers[name]:
                    output = 'No purchase history'

                    out_file.write(f"Average price for {stock}: {output}")
                else:
                    output = round(sum(customers[name][stock]) / len(customers[name][stock]), 2)
                    out_file.write(f"Average price for {stock}: ${output}")

                out_file.write('\n')

            out_file.write('\n')
