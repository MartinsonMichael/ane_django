import pandas as pd
from datetime import datetime, timedelta, date
import parser_app
import os


class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class Global(Singleton):

    succ_proxies = []

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.links = pd.read_csv(os.path.join(self.base_dir, r'description\final_links.csv'), sep=';', index_col=0)
        self.gks_links = os.path.join(self.base_dir, r'description\gks_weekly_links.csv')
        self.path_desc = os.path.join(self.base_dir, r'description\categories.csv')
        self.desc_df = pd.read_csv(self.path_desc, sep=';', index_col='id')
        self.date = datetime.now().date()-timedelta(days=0)  # date(year=2019, month=12, day=7)
        self.max_links = None
        self.is_selenium_ozon = False
        self.is_selenium_okey = False
        self.is_selenium_utkonos = False
        self.is_shutdown = False
        self.path_chromedriver = 'C:\\Users\\evsee\\Downloads\\chromedriver.exe'

    def getproxies(self):
        parser_app.logic.handlers.tools.get_proxy('https://www.perekrestok.ru/', get_new=True, get_list=True)
        # print('self.proxies:', self.proxies)

    def setstatus(self, status):
        self.status = status





