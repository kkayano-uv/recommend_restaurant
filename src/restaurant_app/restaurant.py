import csv
import os
from pathlib import Path

def get_restaurant_csv_path():
    return (Path(__file__).resolve().parent.parent.parent/ "data"/ "restaurant.csv")

def load_restaurants(csvfile):
    rows = []

    if os.path.exists(csvfile):
            with open(csvfile, 'r', newline='') as file:
                reader = csv.DictReader(file)
                rows = list(reader)          
    
    return rows


def recommend_restaurant(rows):
    for row in sorted(rows, key=lambda r: float(r['COUNT']), reverse=True):
        answer = input(f'私のおすすめのレストランは、{row["NAME"]}です。\n'
                       'このレストランはお好きですか？[Yes/No]').lower()
        if answer == 'yes':
            break

def update_restaurant_count(rows, favorite_restaurant):
    found = False
    for row in rows:
        if row['NAME'] == favorite_restaurant:
            row['COUNT'] = str(int(row['COUNT'].strip()) + 1)
            found = True
            break
    
    if not found:
        rows.append({'NAME': favorite_restaurant, 'COUNT': '1'})
    return rows


def save_restaurants(restaurant_csv, rows):
    with open(restaurant_csv, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['NAME', 'COUNT'])
            writer.writeheader()
            writer.writerows(rows)
