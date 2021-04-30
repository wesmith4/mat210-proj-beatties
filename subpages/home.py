import streamlit as st


def run():
    st.title("Disparities and Gentrification along Beatties Ford Road")
    st.write("""
    Final project by [Manny Abiad](https://www.linkedin.com/in/jose-manny-abiad-160888170/), [Liam Carriker](https://www.linkedin.com/in/liam-carriker-a9b40a156/), and [Will Smith](https://linkedin.com/in/williamesmithiv)

    **MAT210:** Math Modeling :bar_chart:
    
    [Dr. Tim Chartier](https://www.davidson.edu/people/tim-chartier), Spring 2021

    [**Davidson College**](https://davidson.edu)

    """)

    st.markdown("""
    The interactive data dashboard visualizes a journey down Beatties Ford Road in Mecklenburg County, NC, highlighting a variety of aesthetic, economic, and demographic differences that one observes while traveling from north to south. As you observe these differences through the combination of maps, photos, charts, and data tables on the pages of this dashboard, discover the disparities in socioeconomic and spatial privilege between the neighborhoods near the edge city of Huntersville and those closer to downtown Charlotte, and how these disparities are linked to racial composition in these areas.

    **In the sidebar to the left, you can navigate between the content pages of this dashboard.**
    """
    )


    st.markdown("""
    ### Drive down Beatties Ford Road on YouTube
    The video below by CharlotteBlackCar presents a drive down the road. As you watch the video (perhaps try it at 1.25 or 1.5 speed), take note especially of the changes in housing quality and the types of businesses and services available in different neighborhoods.
    """)
    st.video('https://youtu.be/-4C9mGXIc7s')

