from momentum_app.models import Divs
from scripts import defs
import csv


def run():
    Divs.objects.all().delete()

    with open('scripts/dividend_aristocrats.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            symbol = row[1]
            name = row[0]
            div = defs.get_div(row[1])

            d = Divs(symbol=symbol, name=name, div_p=div)
            d.save()
