import streamlit as st
#st.set_page_config(layout="wide")


def main():
    st.set_page_config(layout="wide")

    #st.title("Vahan Dashboard 4 Regn")

    # Read the content of your HTML file
    with open("Chatbot.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    # Adjust the dimensions dynamically using custom CSS
    st.markdown(
        f'<div style="width: 100%; height: 100%; overflow: hidden;">{html_content}</div>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
