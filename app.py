import streamlit as st
st.title("Lean Cut Costco Dashboard")

st.metric("Calories", "1850")
st.metric("Protein Goal", "180g")

protein = [
    "Greek Yogurt ",
    "Eggs ",
    "Turkey Burger ",
    "Turkey Bacon ",
    "Liquid Egg Whites ",
    "Chicken Sausage "
]

carbs = [
    "Cream of Rice ",
    "Sweet Potato ",
    "Rice Cakes ",
]

fruits_veggies = [
    "Strawberries ",
    "Blueberries ",
    "Broccoli ",
    "Avocados ",
    "Bananas ",
    "Apples ",
    "Cinamon ",
]

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🥩 Protein")
    for item in protein:
        st.checkbox(item)

with col2:
    st.subheader("🍚 Carbs")
    for item in carbs:
        st.checkbox(item)

with col3:
    st.subheader("🥦 Produce")
    for item in fruits_veggies:
        st.checkbox(item)


