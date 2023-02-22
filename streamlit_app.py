import streamlit

streamlit.title("My Parents New Healthy Diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

#Widget for picking fruit in smoothie
streamlit.header('🍓🥝Build Your OWN Fruit Smoothie 🍌🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# display list for fruit widget
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Banana','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#New Section to display the fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")


# normalize API response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output fruityvice api response and display as a table
streamlit.dataframe(fruityvice_normalized)
