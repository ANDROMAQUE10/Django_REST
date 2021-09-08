from momentum_app.models import Etf
from scripts import defs

def run():
    Etf.objects.all().delete()

    etfs = {
        "IVV": "SP500",
        "DIA": "DJ30",
        "SHV": "Short treasury",
        "LQD": "Corporate bonds",
        "HYG": "High Yield Corporate Bond"
        }

    for key, val in etfs.items():
        symbol = key
        name = val
        momentum = defs.get_momentum(key)
        ma10 = defs.get_10ma(key)

        e = Etf(symbol=symbol, name=name, momentum_12_1=momentum, ma10=ma10)
        e.save()
