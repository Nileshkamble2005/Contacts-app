import requests
import streamlit as st
import pandas as pd


st.set_page_config(page_title="Contact app",page_icon="📞")

st.title("Contact app using API") 

st.write("Click the button below to fetch the users data from the API ")

if st.button("Fetch Data"):    
    responce = requests.get("https://jsonplaceholder.typicode.com/users")
    users = responce.json()

    st.success("Data fetched successfully")
    

    user_list = []

    for user in users:
        user_data = {
            "ID": user["id"],
            "Name": user["name"],   
            "Username": user["username"],
            "Email": user["email"],
            "Phone": user["phone"],
            "city": user["address"]["city"],
            "Company": user["company"]
        }
        user_list.append(user_data) 

    df = pd.DataFrame(user_list)
    st.subheader("Users information")
    st.dataframe(df, use_container_width=True)
