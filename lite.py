import csv
import json

car_data_dict = [{'Brand': 'Nissan', 'Model': 'juke', 'Fuel_con': 8.5, 'Price': 1200000},
                 {'Brand': 'Toyota', 'Model': 'Hilux', 'Fuel_con': 10, 'Price': 3200000},
                 {'Brand': 'Isuzu', 'Model': 'Mu-x', 'Fuel_con': 9, 'Price': 4200000},
                 ]

# csv

fieldnames = ['Brand','Model', 'Fuel_con', 'Price']

with open('cars.csv', 'w') as f:
    writer = csv.DictWriter(f,delimiter = ';',fieldnames =  fieldnames)
    writer.writeheader()
    for i in range(len(car_data_dict)):
        writer.writerow(car_data_dict[i])

# json
with open('cars.json', 'w') as f:
    json.dump(car_data_dict, f)
