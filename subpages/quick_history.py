# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:32:40 2021

@author: liamc
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import os


def run():
    
    with st.beta_container():
        st.title('Looking at the data over time')
    st.markdown("""
    This page takes a look through at four selected variables spanning over time.
    In these charts below, note that the NPAs are ordered to roughly mirror their geographical positions from north to south along Beatties Ford Road.

    Reminder: As defined by the [Quality of Life Study](https://mcmap.org/qol/#15/):

    > *Neighborhood Profile Areas (NPAs) are geographic areas used for the organization and presentation of data in the Quality of Life Study.
    The boundaries were developed with community input and are based on one or more Census block groups.*

    """)

    DATA_FILE = os.path.join(os.path.dirname(__file__),'../qol-data/master.pkl')
    LOOKUP_FILE = os.path.join(os.path.dirname(__file__),'../qol-data/variableLookup.csv')
    METADATA_FILE = os.path.join(os.path.dirname(__file__),'../qol-data/csvFiles/metadata.csv')

    # master = pd.read_pickle('./qol-data/master.pkl')
    master = pd.read_pickle(DATA_FILE)
    master.columns = master.columns.str.replace(' ','')
    variableLookup = pd.read_csv(LOOKUP_FILE)
    metadata = pd.read_csv(METADATA_FILE)

    def showVariableDescription(long_name):
        varCode = variableLookup[variableLookup['name'] == long_name]['code'].values[0]
        description = metadata[metadata['Short _Name'] == varCode]['Long_Description'].values[0]
        with st.beta_expander("Variable description",expanded=True):
            st.write('*{}*'.format(description))
    # Construct dataframe for population by race

#sales price/value graphs
    #housing prices
    hp_graphs = {}
    for year in ['2013','2015']:
        data = master.loc[:,['NPA', 'order', 'Home_Sales_Price_{}'.format(year)]]
        data.columns = ['NPA', 'order', 'Home Sales Price']
        data.loc[:,['Home Sales Price']] = data[['Home Sales Price']].astype(float)

        melted = pd.melt(data, id_vars=['NPA', 'order'], value_vars=[
            'Home Sales Price'], value_name="price")

        fig = px.bar(melted, y="order", x="price",
                    orientation="h", labels=dict(order="NPA", price="Price"), title="Average Housing Prices by NPA ({})".format(year))
        fig.update_yaxes(autorange="reversed",
                        ticktext=data.NPA.tolist(), tickvals=data.order.to_list())
        fig.update_layout(legend=dict(
            yanchor="top",
            y=-.2,
            xanchor="left",
            x=0.01,
            orientation='h'
        ))

        hp_graphs[year] = fig
    st.markdown('## Average Housing Prices by NPA over time')
    showVariableDescription("Home_Sales_Price_2015")
    hp_col1,hp_col2= st.beta_columns([1,1])
    hp_col1.plotly_chart(hp_graphs['2013'],use_container_width=True)
    hp_col2.plotly_chart(hp_graphs['2015'],use_container_width=True)

    with st.beta_container():  #INSERT ANALYSIS
        st.markdown("""
        Looking at data taken from the years 2013 and 2015, we can see that the bar graphs trend similarly. Because NPAs are laid out with north-most NPAs higher on the y-axis and south-most NPAs lower, we can establish that average housing prices per NPA region remain higher in northern regions of Beatties Ford Road, and steadily decrease as the road progresses south-bound with a smaller jump in the most south-most NPA regions. 
        """)
    #insert rental costs from 2017-2018???

#household income
    hi_graphs = {}
    for year in ['2017','2018']:
        data = master.loc[:,['NPA', 'order', 'Household_Income_{}'.format(year)]]
        data.columns = ['NPA', 'order', 'Household Income']
        data.loc[:,['Household Income']] = data[['Household Income']].astype(float)

        melted = pd.melt(data, id_vars=['NPA', 'order'], value_vars=[
            'Household Income'], value_name="hh_inc")

        fig = px.bar(melted, y="order", x="hh_inc", 
                    orientation="h", labels=dict(order="NPA", hh_inc="Household Income"), title="Average Household Income ({})".format(year))
        fig.update_yaxes(autorange="reversed",
                        ticktext=data.NPA.tolist(), tickvals=data.order.to_list())
        fig.update_layout(legend=dict(
            yanchor="top",
            y=-.2,
            xanchor="left",
            x=0.01,
            orientation='h'
        ))

        hi_graphs[year] = fig
    st.markdown('## Average Household Income per NPA over Time')
    showVariableDescription("Household_Income_2018")
    hi_col1,hi_col2 = st.beta_columns([1,1])
    hi_col1.plotly_chart(hi_graphs['2017'],use_container_width=True)
    hi_col2.plotly_chart(hi_graphs['2018'],use_container_width=True)

    with st.beta_container():
        st.markdown("""
        Looking at data taken from the recent years of 2017 and 2018, there is a clear consistent trend of Average Household Income decreasing as one moves further south on Beatties Ford Road. This steady trend does not match that of Average Housing Price, which while taken a couple years before, showed a consistent trend of sharply increasing in the south-most NPAs of Beatties Ford Road.
        """)

# Public nutrition assistance

    pn_graphs = {}
    for year in ['2011','2015','2018']:
        data = master.loc[:,['NPA', 'order', 'Public_Nutrition_Assistance_{}'.format(year)]]
        data.columns = ['NPA', 'order', 'Public Nutrition Assistance']
        data.loc[:,['Public Nutrition Assistance']] = data[['Public Nutrition Assistance']].astype(float)

        melted = pd.melt(data, id_vars=['NPA', 'order'], value_vars=[
            'Public Nutrition Assistance'], value_name="pn_ast")

        fig = px.bar(melted, y="order", x="pn_ast", 
                    orientation="h", labels=dict(order="NPA", pn_ast="Public Nutrition Assistance"), title="Public Nutrition Assistance ({})".format(year))
        fig.update_yaxes(autorange="reversed",
                        ticktext=data.NPA.tolist(), tickvals=data.order.to_list())
        fig.update_layout(legend=dict(
            yanchor="top",
            y=-.2,
            xanchor="left",
            x=0.01,
            orientation='h'
        ))

        pn_graphs[year] = fig
    st.markdown('## Public Nutrition Assistance by NPA over Time')
    showVariableDescription("Public_Nutrition_Assistance_2018")
    pn_col1,pn_col2,pn_col3 = st.beta_columns([1,1,1])
    pn_col1.plotly_chart(pn_graphs['2011'],use_container_width=True)
    pn_col2.plotly_chart(pn_graphs['2015'],use_container_width=True)
    pn_col3.plotly_chart(pn_graphs['2018'],use_container_width=True)

    with st.beta_container():
        st.markdown("""
        Data taken on inhabitants receiving nutritional assistance shows a clear trend between the years of 2011 and 2018. In each year, the percentage of NPA population receiving nutritional asssitance received steadily increasing the further south one is on Beatties Ford Road, indicating that the nutritional environment of an NPA region gets worse the further south the NPA is. 
        """)



#employment rate
    er_graphs = {}
    for year in ['2017','2018']:
        data = master.loc[:,['NPA', 'order', 'Employment_Rate_{}'.format(year)]]
        data.columns = ['NPA', 'order', 'Employment Rate']
        data.loc[:,['Employment Rate']] = data[['Employment Rate']].astype(float)

        melted = pd.melt(data, id_vars=['NPA', 'order'], value_vars=[
            'Employment Rate'], value_name="e_rate")

        fig = px.bar(melted, y="order", x="e_rate",
                    orientation="h", labels=dict(order="NPA", e_rate="Employment Rate"), title="Employment Rate ({})".format(year))
        fig.update_yaxes(autorange="reversed",
                        ticktext=data.NPA.tolist(), tickvals=data.order.to_list())
        fig.update_layout(legend=dict(
            yanchor="top",
            y=-.2,
            xanchor="left",
            x=0.01,
            orientation='h'
        ))

        er_graphs[year] = fig
    st.markdown('## Employment Rates per NPA Region over Time')
    showVariableDescription("Employment_Rate_2018")
    er_col1,er_col2 = st.beta_columns([1,1])
    er_col1.plotly_chart(er_graphs['2017'],use_container_width=True)
    er_col2.plotly_chart(er_graphs['2018'],use_container_width=True)

    with st.beta_container():
        st.markdown("""
        Employment rates remain relatively steady throughought NPA regions between the years of 2017-2018, indicating relatively uniform employment rates across Beatties Ford Road.
        """)


#racial graphs
    graphs = {}
    for year in ['2000','2010','2018']:
        data = master.loc[:,['NPA', 'order', 'Population_{}'.format(year), 'White_Population_{}'.format(year),
                    'Black_Population_{}'.format(year), 'Asian_Population_{}'.format(year), 'Hispanic_Latino_{}'.format(year), 'All_Other_Races_{}'.format(year)]]
        data.columns = ['NPA', 'order', 'Total Population',
                        'White', 'Black', 'Asian', 'Hispanic/Latino', 'Other']
        data.loc[:,['White', 'Black', 'Asian', 'Hispanic/Latino', 'Other']
            ] = data[['White', 'Black', 'Asian', 'Hispanic/Latino', 'Other']].astype(float)
        data.loc[:,['White', 'Black', 'Asian', 'Hispanic/Latino', 'Other']] = data[['White', 'Black',
                                                                            'Asian', 'Hispanic/Latino', 'Other']].multiply(data['Total Population'], axis="index")/100

        melted = pd.melt(data, id_vars=['NPA', 'order'], value_vars=[
            'White', 'Black', 'Asian', 'Hispanic/Latino', 'Other'], var_name="Race", value_name="population")

        fig = px.bar(melted, y="order", x="population", color="Race",
                    orientation="h", labels=dict(order="NPA", population="Population"), title="Population by Race ({})".format(year))
        fig.update_yaxes(autorange="reversed",
                        ticktext=data.NPA.tolist(), tickvals=data.order.to_list())
        fig.update_layout(legend=dict(
            yanchor="top",
            y=-.2,
            xanchor="left",
            x=0.01,
            orientation='h'
        ))

        graphs[year] = fig
    st.markdown('## Racial Breakdowns by NPA over time')
    col1,col2,col3 = st.beta_columns([1,1,1])
    col1.plotly_chart(graphs['2000'],use_container_width=True)
    col2.plotly_chart(graphs['2010'],use_container_width=True)
    col3.plotly_chart(graphs['2018'],use_container_width=True)

    with st.beta_container():
        st.markdown("""
        Between the years of 2000 and 2018, we can observe that population in further out NPAs steadily increase, with the increasing population predominantly being white. It is also clear that the further south an NPA region is on Beatties Ford Road, the higher the percentage of population being black, with a smaller jump of population that is white increasing over time in the south-most NPAs of Beatties Ford.  
        """)

    with st.beta_container():
        st.title('Conclusions')
        st.markdown("""
        Between all the graphs over time displayed, despite varying years, we can see trends that persist over time that correlate with the further south an NPA region is on Beatties Ford Road. Moving from north to south clearly correlates with lower housing prices, lower household income, higher prescence of nutritional assistance, and a shift from a higher percentage of population that is white to a higher percentage of population that is black. There are also remarkable reversal most of these trends in the south-most two to three NPA regions, which are regions closest to downtown Charlotte.
        """)

    

if __name__ == "__main__":
    run()