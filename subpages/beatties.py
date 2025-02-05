import pandas as pd
import numpy as np
import streamlit as st
from matplotlib import pyplot as plt
import pydeck as pdk
from pydeck.types import String
import geopandas as gpd

import streamlit.components.v1 as components

def run():
    
    st.title('Beatties Ford Road Project')

    grocery = pd.read_csv('./grocery-data/Grocery_Stores.csv')
    grocery = grocery.rename(columns={'X': 'longitude', 'Y': 'latitude'})
    grocery = grocery[['longitude', 'latitude', 'Name']]
    coords = grocery[['longitude', 'latitude']]

    st.write(grocery)
    medianLong = grocery['longitude'].median()
    medianLat = grocery['latitude'].median()
    st.write(grocery.dtypes)

    beattiesGeoJson = "https://raw.githubusercontent.com/wesmith4/mat210-proj-beatties/main/beatties.geojson"
    roadLabel = pd.read_json("./roadLabel.json")

    tooltip = {"html": "<b>Store:</b> {Name}"}
    view_state = pdk.ViewState(
            **{"latitude": 35.33, "longitude": -80.89, "zoom": 10.50, "maxZoom": 22, "pitch": 0, "bearing": 0}
        )
    st.write("""## Grocery stores in Mecklenburg County""")
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/streets-v11',
        initial_view_state=view_state,
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=grocery,
                get_position=['longitude', 'latitude'],
                get_color='[200, 30, 0, 160]',
                get_radius=200,
                pickable=True,
                extruded=True,
                #  elevationScale=4,
                #  elevationRange=[0,1000]
            ),
            pdk.Layer(
                'GeoJsonLayer',
                data=beattiesGeoJson,
                filled=True,
                pickable=False,
                lineWidthMinPixels=3,
                get_line_color=[0,0,200],
                opacity=1,
                id='beatties-ford-road',
                use_binary_transport=False,
                extruded=True
            ),
            pdk.Layer(
                'TextLayer',
                data=roadLabel,
                id='label',
                pickable=False,
                get_size=16,
                get_color=[1, 1, 1],
                get_position="coordinates",
                get_text="name",
                get_angle=0,
                get_text_anchor=String("middle"),
                get_alignment_baseline=String("center")
            )

        ],
        tooltip=tooltip
    ))

    components.html("""
    <iframe frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.socialexplorer.com/bc9c206f28/embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"></iframe>
    """, width=640, height=480)

    components.html("""
        <iframe frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.socialexplorer.com/7e100dcc9b/embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"></iframe>
    """, width=640, height=480)
