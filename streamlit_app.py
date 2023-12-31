import streamlit
import pandas
streamlit.title('My Parents new Healthy Diner')
streamlit.header('🍌🥭Breakfast Menu')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.text('Idli - 2')
streamlit.text('🍜Dosa-1 and Coffee')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_select = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_select]
streamlit.dataframe(fruits_to_show)
streamlit.text('Example Scenario... Checking...')
# Display the table on the page.
