import os
from apscheduler.schedulers.blocking import BlockingScheduler


def div():
    os.system("python manage.py runscript divs_script")

def dj30():
    os.system("python manage.py runscript dj30_script")

def sp500():
    os.system("python manage.py runscript sp500_script")

def index():
    os.system("python manage.py runscript etf_script")


"""
scheduler = BlockingScheduler()
scheduler.add_job(divs_script, 'interval', days=30, start_date="2020-07-01", end_date="2024-12-30")
scheduler.add_job(dj30_script, 'interval', days=25, start_date="2020-07-02", end_date="2024-12-30")
scheduler.add_job(sp500_script, 'interval', days=26, start_date="2020-07-03", end_date="2024-12-30")
scheduler.add_job(etf_script, 'interval', days=27, start_date="2020-07-04", end_date="2024-12-30")
scheduler.start()"""
