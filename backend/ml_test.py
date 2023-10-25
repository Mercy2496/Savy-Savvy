#!/usr/bin/env python3
"""
ml test
"""

from models.ml.transformer import Transformer
from models.uitems import UItem
import os

tfm = Transformer()

# print(tfm.main_df.dtypes)

uitems = tfm.summarize_items(get_dicts=True)


# print("="*30)
# print(uitems[0])
# ui = UItem(uitems[0])
# ui.save()

for item in uitems[:1]:
    # for key, val in item.items():
    #     print(f"{key}: {val}: {type(val)}")
    ui = UItem(**item)
    ui.save()
