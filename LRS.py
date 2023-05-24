import streamlit as st

# CSS styling with background gradient
st.markdown(
    """
    <style>
    .title {
        font-size: 32px;
        color: #333;
        text-align: center;
        margin-bottom: 20px;
    }
    .label {
        font-size: 18px;
        color: #666;
        margin-bottom: 10px;
    }
    .recommendation {
        font-size: 22px;
        color: #007bff;
        margin-bottom: 20px;
        text-align: center;
    }
    body {
        background: linear-gradient(to right, #1CB5E0, #000046);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.markdown("<h1 class='title'>Laptop Recommendation System</h1>", unsafe_allow_html=True)

# Laptop recommendation function
def recommend_laptop(budget, usage, brand, sorting):
    # Add your recommendation logic here
    # Return the recommended laptop

    recommendation = "MacBook Pro"  # Example recommendation

    return recommendation

# User inputs
budget = st.slider("Select your budget:", 500, 5000, 1500)
usage = st.selectbox("Select your usage:", ("General Use", "Gaming", "Programming"))
brand = st.multiselect("Select preferred brand(s):", ["Apple", "Dell", "HP", "Lenovo", "ASUS"])
sorting = st.selectbox("Sort by:", ("Price: Low to High", "Price: High to Low", "Popularity"))

# Generate recommendation
recommendation = recommend_laptop(budget, usage, brand, sorting)

# Display recommendation
st.markdown("<p class='label'>Your Recommended Laptop:</p>", unsafe_allow_html=True)
st.markdown(f"<p class='recommendation'>{recommendation}</p>", unsafe_allow_html=True)
