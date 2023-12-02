import csv

from datetime import datetime


def export_to_csv(data):
    fieldnames = ["Site Category", "Image Src", "Code", "Title", "Price", "Body (HTML)", "Collection", "Vendor", "Weight", "Weight Unit", "Status"]

    # Filename format: ProductList_dd-mm-YY_HMS
    filename = datetime.now().strftime("ProductList_%d-%m-%Y_%H%M%S.csv")
    
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    f.close()