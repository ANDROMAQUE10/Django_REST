from momentum_app.models import DJ30

import csv
from scripts import defs


def run():
    DJ30.objects.all().delete()

    with open('scripts/DJ30.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            symbol = row[1]
            name = row[0]
            mom = defs.get_avg_momentum(row[1])
            mom_12_2 = defs.get_momentum_12_2(row[1])
            ep = defs.get_ep(row[1])
            low = defs.get_low_range(row[1])

            d = DJ30(symbol=symbol, name=name, avg_momentum=mom,
                     momentum_12_2=mom_12_2, ep=ep, low_range=low)
            d.save()
