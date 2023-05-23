import streamlit as st
import json
import textwrap
import rich


# Plot a text
titles = ['20230522_LD_These 8 Altcoins Just Flipped The Crypto Market.json',
         '20230516_BC_Bitcoin_ Year-To-Date ROI.json']

title_style = """
    <style>
        .title-text {
            font-family: "Arial", sans-serif;
            font-size: 24px;
            font-weight: bold;
        }
    </style>
"""

st.set_page_config(layout="wide")

for t in titles:
    
    with open(t, 'r') as file:
        data = json.load(file)
    
    # Extract the text from the JSON data
    text = data['summary']
    text_title = data['video_title']
    subtitle_text = data['date'] + ' - ' + data['channel']
    
    st.markdown(title_style, unsafe_allow_html=True)
    st.markdown(f'<p class="title-text">{text_title}</p>', unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: left; font-size: 16px'>{subtitle_text}</h3>", unsafe_allow_html=True)

    with st.expander("Click to expand"):
        markdown_template = '<div style="text-align: justify">{}</div>'

        # Render the Markdown template with the text content
        justified_text = markdown_template.format(text)

        # Display the justified text in Streamlit
        st.markdown(justified_text, unsafe_allow_html=True)

    