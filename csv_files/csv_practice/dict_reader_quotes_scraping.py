import csv
with open('web_scraping_data.csv', 'r', encoding='utf-8') as file:
    # Итератор
    csv_reader = csv.DictReader(file, delimiter='|')
    for quote in csv_reader:
        # print(car)
        print(f"Quoter: {quote['Quoter']}" + '\n' + f"Author: {quote['Author']}" + '\n' + f"Tags: {quote['Tags']}" + '\n')