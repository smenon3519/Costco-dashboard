import streamlit as st

st.title("Lean Cut Costco Dashboard")

st.metric("Calories", "1850")
st.metric("Protein Goal", "180g")

protein = [
    {
        "name": "Greek Yogurt",
        "image": "https://images.unsplash.com/photo-1571212515416-fef01fc43637?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Z3JlZWslMjB5b2d1cnR8ZW58MHx8MHx8fDA%3D"
    },
    {
        "name": "Eggs",
        "image": "https://plus.unsplash.com/premium_photo-1676686126965-cb536e2328c3?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZWdnc3xlbnwwfHwwfHx8MA%3D%3D"
    },
    {
        "name": "Turkey Burger",
        "image": "https://images.unsplash.com/photo-1521305916504-4a1121188589?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8dHVya2V5JTIwYnVyZ2VyfGVufDB8fDB8fHww"
    },
    {
        "name": "Turkey Bacon",
        "image": "https://images.unsplash.com/photo-1606851094655-b2593a9af63f?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8dHVya2V5JTIwYmFjb258ZW58MHx8MHx8fDA%3D"
    },
    {
        "name": "Liquid Egg Whites",
        "image": "https://images.unsplash.com/photo-1610328466269-1f36faad83c1?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8ZWdnJTIwd2hpdGVzfGVufDB8fDB8fHww"
    },
    {
        "name": "Chicken Sausage",
        "image": "https://images.unsplash.com/photo-1624772404867-08060beaaa1b?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8Y2hpY2tlbiUyMHNhdXNhZ2V8ZW58MHx8MHx8fDA%3D"
    }
]

carbs = [
    {
        "name": "Cream of Rice",
        "image": "https://plus.unsplash.com/premium_photo-1658527064466-df8ed3bbe6e7?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y3JlYW0lMjBvZiUyMHJpY2V8ZW58MHx8MHx8fDA%3D"
    },
    {
        "name": "Sweet Potato",
        "image": "https://images.unsplash.com/photo-1596097635121-14b63b7a0c23?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8c3dlZXQlMjBwb3RhdG98ZW58MHx8MHx8fDA%3D"
    },
    {
        "name": "Rice Cakes",
        "image": "https://plus.unsplash.com/premium_photo-1699519510499-41b626d8522e?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cmljZSUyMGNha2VzfGVufDB8fDB8fHww"
    }
]

fruits_veggies = [
    {"name": "Strawberries", "image": "https://images.unsplash.com/photo-1464965911861-746a04b4bca6"},
    {"name": "Blueberries", "image": "https://images.unsplash.com/photo-1502741338009-cac2772e18bc"},
    {"name": "Broccoli", "image": "https://images.unsplash.com/photo-1685504445355-0e7bdf90d415?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YnJvY2NvbGl8ZW58MHx8MHx8fDA%3D"},
    {"name": "Avocados", "image": "https://images.unsplash.com/photo-1612506266679-606568a33215?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YXZvY2Fkb3N8ZW58MHx8MHx8fDA%3D"},
    {"name": "Bananas", "image": "https://images.unsplash.com/photo-1603833665858-e61d17a86224?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8YmFuYW5hc3xlbnwwfHwwfHx8MA%3D%3D"},
    {"name": "Apples", "image": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8YXBwbGVzfGVufDB8fDB8fHww"},
    {"name": "Cinnamon", "image": "https://images.unsplash.com/photo-1636972955024-3b01f2236b01?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2luYW1vbnxlbnwwfHwwfHx8MA%3D%3D"}
]

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🥩 Protein")
    for i, item in enumerate(protein):
        st.write(item["name"])
        st.image(item["image"], width=150)
        st.checkbox("Add", key=f"protein_{i}")

with col2:
    st.subheader("🍚 Carbs")
    for i, item in enumerate(carbs):
        st.write(item["name"])
        st.image(item["image"], width=150)
        st.checkbox("Add", key=f"carbs_{i}")

with col3:
    st.subheader("🥦 Produce")
    for i, item in enumerate(fruits_veggies):
        st.write(item["name"])
        st.image(item["image"], width=150)
        st.checkbox("Add", key=f"produce_{i}")