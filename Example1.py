# 2.2.1 Show a temporary message with a button

import streamlit as st 

#Example: Show a temporary message with a button

animal_shelter = ['cat', 'dog', 'rabbit', 'bird'] 

animal = st.text_input('Type an animal!!') 

if st.button('Check availability'): 
	have_it = animal.lower() in animal_shelter 
	'We have that animal!' if have_it else 'We don\'t have that animal.'

print("danger!")