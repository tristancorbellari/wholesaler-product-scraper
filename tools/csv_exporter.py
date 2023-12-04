import csv
import util.constants as c

from datetime import datetime


def export_to_csv(data):
    print("Exporting to CSV...")

    # Filename format: ProductList_dd-mm-YY_HMS
    filename = datetime.now().strftime("ProductList_%d-%m-%Y_%H%M%S.csv")

    # Get fieldnames for header row from any product (choose first one for simplicity)
    fieldnames = data[0].keys()

    with open(filename, "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        writer.writerows(data)

    f.close()

    print("Export complete! {}".format(filename))
