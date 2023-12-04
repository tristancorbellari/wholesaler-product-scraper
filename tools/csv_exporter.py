import csv
import util.constants as c

from datetime import datetime


def export_to_csv(data):
    print("Exporting to CSV...")

    # Filename format: ProductList_dd-mm-YY_HMS
    filename = datetime.now().strftime("ProductList_%d-%m-%Y_%H%M%S.csv")

    with open(filename, "w", encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=c.FIELDNAMES)
        writer.writeheader()
        writer.writerows(data)

    f.close()

    print("Export complete! {}".format(filename))
