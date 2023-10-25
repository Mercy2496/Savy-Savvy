#!/usr/bin/env python3
"""
This class Transforms the data from the item table
"""
import pandas as pd
from models.item import Item
from datetime import datetime
import json

class Transformer():
    """
    """
    all_items = ""
    iitem = ""
    main_df = pd.DataFrame()

    def __init__(self, *args, **kwargs):
        """
        """
        self.iitem = Item()
        self.all_items = self.iitem.get_all_items()
        self.to_df(return_=False)


    def to_df(self, return_=True):
        """
        Returns a df
        """
        data = []
        for item in self.all_items:
            data.append(item.to_dict())

        if data:
            df = pd.DataFrame(data)
            self.main_df = self.clean_df(df).copy()
        if return_:
            return self.main_df

    def clean_df(self, df=main_df):
        try:
            df["created_at"] = pd.to_datetime(df["created_at"])
            df["updated_at"] = pd.to_datetime(df["updated_at"])
        except Exception as e:
            print(f"--E--(ERR): While converting dates to pd.datetime: {e}")
        try:
            df["type"] = df['type'].str.replace('+', ' ')
        except Exception as e:
            print(f"--E--(ERR): While replacing '+' in type: {e}")
        try:
            df['price'] = df['price'].str.split('-').str[0].str.split(' ').str[1].str.replace(',', '').astype('int32')
        except Exception as e:
            print(f"--E--(ERR): While extracting the price: {e}")
        return df

    def get_item_df(self, col=""):
        df = self.main_df
        item_df = pd.DataFrame()
        cols = ["id", "type", "price", "created_at", "updated_at"]

        if col in list(df['type'].unique()):
            item_df = df[df['type'] == col].reset_index()
            item_df = item_df[cols]
            item_df['year'] = item_df['updated_at'].dt.year
            item_df['month'] = item_df['updated_at'].dt.month
            item_df['day'] = item_df['updated_at'].dt.day
            item_df['hour'] = item_df['updated_at'].dt.hour
            item_df['minute'] = item_df['updated_at'].dt.minute
        else:
            print(f"--E--(ERR): Can't Find {col} in 'df[type]' col")

        return item_df

    def transform_prices(self, df=pd.DataFrame()):
        new_dict = {}

        new_dict["type"] = df["type"][0]
        new_dict["count"] = round(df["price"].count())
        new_dict["latest_update"] = (df["updated_at"].max()).strftime('%Y-%m-%d %H:%M:%S')
        new_dict["earliest_update"] = (df["updated_at"].min()).strftime('%Y-%m-%d %H:%M:%S')

        new_dict["min_price"] = round(df["price"].min())
        new_dict["median_price"] = round(df["price"].median())
        new_dict["max_price"] = round(df["price"].max())
        new_dict["mean_price"] = round(df["price"].mean())
        mode = list(df["price"].mode())

        if len(mode):
            freq_dict = {}
            new_dict["mode"] = json.dumps(df["price"].mode().tolist())
            for mod in mode:
                freq_dict[mod] = int((df["price"] == mod).sum())
            new_dict["freq"] = json.dumps(freq_dict)
        new_dict["nunique_price"] = df["price"].nunique()

        return new_dict

    def summarize_items(self, items=[], get_dicts=False):
        """..."""
        df = self.main_df
        new_df = pd.DataFrame()
        item_list = []

        if not items:
            items = list(df['type'].unique())
        for item in items:
            item_df = self.get_item_df(item)
            item_dict = self.transform_prices(item_df)
            item_list.append(item_dict)
        if get_dicts is True:
            return item_list
        else:
            new_df = pd.DataFrame(item_list)

        return new_df