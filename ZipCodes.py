
# coding: utf-8

# In[1]:


import altair as alt
import pandas as pd
import numpy as np
import json


# In[2]:


def loadData():
    import os
    cur_dir = os.path.dirname(__file__)
    data = json.load(open(os.path.join(cur_dir, 'nyc_restaurants_by_cuisine.json'), 'r'))
    df = pd.DataFrame(data).sort_values(by=['total'], ascending=False)
    return df


# In[3]:


def ZipCode(data, zip_code):
    try:
        data_perzip = pd.concat([data[['cuisine', 'perZip']], data.perZip.apply(pd.Series)], axis=1)[['cuisine', str(zip_code)]]        .dropna().rename(index=str, columns={str(zip_code): "total"}).sort_values(by=['total'], ascending=False)
    except:
        data_perzip = pd.DataFrame({'cuisine' : [np.nan], 'total' : [np.nan]})

    return alt.Chart(data_perzip).mark_bar(stroke="Black").encode(
            alt.X("total:Q", axis=alt.Axis(title="Restaurants")),
            alt.Y('cuisine:O', sort=alt.SortField(field="total", op="argmax")),
            alt.ColorValue("LightGrey"),
            ).properties(width=200)

