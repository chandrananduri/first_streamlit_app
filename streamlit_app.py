import streamlit
import pandas
streamlit.title('My Parents new Healthy Diner')
streamlit.header('🍌🥭Breakfast Menu')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.text('Idli - 2')
streamlit.text('🍜Dosa-1 and Coffee')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
# Display the table on the page.
