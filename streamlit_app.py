import streamlit
import pandas
import requests

# Started off by adding a title
streamlit.title('My Parents New Healthy Diner')
# Then added a header
streamlit.header('Breakfast Menu')
#Then added some text
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

#Added another header
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Added a dataframe using pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can pick the fruit they want to include
# This is the same code we will exapnd on in the next line - streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Let's put a pick list here so they can pick the fruit they want to include. We will call it fruits selected (variable)
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# New Section to display Fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# after that we put our results in a dataframe
streamlit.dataframe(fruityvice_normalized)







