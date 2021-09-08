from momentum_app.models import SP500

import csv
from scripts import defs


def run():
    SP500.objects.all().delete()

    with open('scripts/SP500_components.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            symbol = row[0]
            name = row[1]
            momentum = defs.get_avg_momentum(row[0])
            mom_12_2 = defs.get_momentum_12_2(row[0])
            ep_ = defs.get_ep(row[0])
            low = defs.get_low_range(row[0])

            s = SP500(symbol=symbol, name=name, avg_momentum=momentum,
                      momentum_12_2=mom_12_2, ep=ep_, low_range=low)
            s.save()
