
from parser_app.models import PricesRaw
import plotly.graph_objects as go
import plotly.offline as opy
import pandas as pd
import numpy as np
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class SnapshotManager:

    def __init__(self):
        self.last_succ_date = PricesRaw.objects.last().date # доделать

    def update_plot(self, wdw=5):
        path_db = os.path.join(BASE_DIR, 'db.sqlite3')
        df = pd.read_sql(sql='SELECT * FROM parser_app_basket',
                         con=sqlite3.connect(path_db), index_col=None) # TODO: изменить адрес
        df = df.set_index('date')
        df.loc[:, 'online_ma'] = pd.Series(index=df.iloc[wdw:-wdw + 1, :].index.values,
                                           data=[np.mean(df.online_price.values[i - wdw:i + wdw + 1]) for i in
                                                 range(wdw, len(df.online_price.values) - wdw + 1)])
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['gks_price'],
            name="Росстат",
            line_color='#921a1d',
            opacity=1))

        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['online_price'],
            name="Онлайн-ритейлеры",
            line_color='#f99b1c',
            opacity=1))

        '''
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['online_ma'],
            name="Онлайн-ритейлеры (ma)",
            line_color='red',
            opacity=0.8))
        '''
        # Use date string to set xaxis range
        fig.update_layout(xaxis_range=[df.index.min(), df.index.max()],
                          title_text="Стоимость условного (минимального) набора продуктов",
                          yaxis_title='руб.',
                          xaxis_rangeslider_visible=True)

        div = opy.plot(fig, auto_open=False, output_type='div')
        return div
