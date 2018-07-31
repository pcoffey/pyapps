import csv
import os
import statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('-----------------------------------------')
    print('      Real Estate Data Mining App')
    print('-----------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        # Row will be collections.OrderedDict in Python 3.6 and above
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            # print(type(row), row)
            # print("Bed count: {}".format(row['beds']))
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases

        # header = fin.readline().strip()
        # reader = csv.reader(fin, delimiter=',')
        # for row in reader:
        #     print(type(row), row)
        #


# This is basic pure python way to read.
# Just use builtin csv support instead.
# def load_file_basic(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('found header: ' + header)
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             lines.append(line_data)
#
#         print(lines[:5])

# def get_price(p):
#     return p.price

def query_data(data):
    # if data was sorted by price:
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)

    # most expensive house?
    high_price = data[-1]
    print("The most expensive house is ${:,} with {} beds "
          "and {} baths".format(high_price.price, high_price.beds, high_price.baths))

    # least expensive house?RR
    low_price = data[0]
    print("The least expensive house is ${:,} with {} beds "
          "and {} baths".format(low_price.price, low_price.beds, low_price.baths))

    # average price house?
    # prices = []
    # for pur in data:
    #     prices.append(pur.price)

    prices = [
        p.price # projection of items
        for p in data # the set to process
    ]

    avg_price = statistics.mean(prices)
    print("The average home price is ${:,}".format(int(avg_price)))

    # average price of 2 bedroom houses
    # prices = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)

    # Generator Expressions use round brackets, works like yield, only pulls
    # what is needed, better memory use than List Comprehensions(but can index in here not Generators)
    # If use often List , if throwaway Generator
    two_bed_homes = (
        p  # projection of items
        for p in data  # the set to process/source
        if announce(p, '2-bedrooms, found {}'.format(p.beds)) and p.beds == 2 # test /condition/filter
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    avg_price = statistics.mean((announce(p.price, 'price') for p in homes))
    avg_baths = statistics.mean((p.baths for p in homes))
    avg_sqft = statistics.mean((p.sq__ft for p in homes))
    print("Average 2 bedroom house is ${:,}, baths={}, sq ft={:,}"
          .format(int(avg_price), round(avg_baths, 1), round(avg_sqft, 1)))


def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item


if __name__ == '__main__':
    main()
