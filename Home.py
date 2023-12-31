import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/Aryanmartinian>
"""
st.sidebar.title("About")
st.sidebar.info(markdown)

logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Streamlit for Geospatial Applications")
st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/Aryanmartinian/Interactive_Map).
    """
)
st.header("Instructions")

markdown="""
1. For the [GitHub repository](https://github.com/Aryanmartinian) or [use it as a template](https://github.com/Aryanmartinian/Interactive_Map) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
"""

st.markdown(markdown)

m= leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
