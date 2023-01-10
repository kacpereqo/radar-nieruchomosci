from pymongoarrow.monkey import patch_all
from pymongoarrow.api import Schema
import pandas as pd
from datetime import datetime

from app.mongodb.service import MongoDatabase


class Plotter():
    def __init__(self) -> None:
        patch_all()
        self.client = MongoDatabase()
        self.df = self.get_data_frame()  # df = data frame

    def get_data_frame(self):
        schema = Schema({"price": int, "area": int,
                        "rooms": int, "date": datetime, "city_id": int, "region_id": int, "floor": int, "is_furnished": bool, "is_owner_is_business": bool, "built_type": str})

        df = self.client.db.offers.flat_offers.find_pandas_all(
            {}, schema=schema)
        return df


plotter = Plotter()
