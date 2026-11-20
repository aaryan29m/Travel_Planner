
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Travel Recommendation System",
    page_icon="✈️",
    layout="wide"
)

# Title
st.title("✈️ Smart Travel Recommendation System")
st.write("Find your perfect destination according to your preferences!")

# Travel destination dataset
destinations = [
    {
        "Place": "Goa",
        "Country": "India",
        "Continent": "Asia",
        "Budget": 15000,
        "Age": "All",
        "Description": "Beautiful beaches, nightlife and water sports."
    },
    {
        "Place": "Dubai",
        "Country": "UAE",
        "Continent": "Asia",
        "Budget": 50000,
        "Age": "All",
        "Description": "Luxury shopping, skyscrapers and desert safari."
    },
    {
        "Place": "Tokyo",
        "Country": "Japan",
        "Continent": "Asia",
        "Budget": 80000,
        "Age": "All",
        "Description": "Technology, anime, culture and amazing food."
    },
    {
        "Place": "Paris",
        "Country": "France",
        "Continent": "Europe",
        "Budget": 100000,
        "Age": "All",
        "Description": "Eiffel Tower, museums and beautiful architecture."
    },
    {
        "Place": "Switzerland",
        "Country": "Switzerland",
        "Continent": "Europe",
        "Budget": 120000,
        "Age": "All",
        "Description": "Beautiful mountains, lakes and scenic train journeys."
    },
    {
        "Place": "New York",
        "Country": "USA",
        "Continent": "North America",
        "Budget": 150000,
        "Age": "All",
        "Description": "Times Square, Statue of Liberty and city life."
    },
    {
        "Place": "Cape Town",
        "Country": "South Africa",
        "Continent": "Africa",
        "Budget": 90000,
        "Age": "All",
        "Description": "Mountains, beaches and wildlife."
    },
    {
        "Place": "Sydney",
        "Country": "Australia",
        "Continent": "Oceania",
        "Budget": 130000,
        "Age": "All",
        "Description": "Opera House, beaches and adventure activities."
    },
    {
        "Place": "Rio de Janeiro",
        "Country": "Brazil",
        "Continent": "South America",
        "Budget": 110000,
        "Age": "All",
        "Description": "Beaches, mountains and colourful culture."
    }
]

df = pd.DataFrame(destinations)

# User input section
st.sidebar.header("🌍 Your Travel Details")

name = st.sidebar.text_input("Enter your name")

age = st.sidebar.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    value=20
)

budget = st.sidebar.number_input(
    "Your budget (₹)",
    min_value=1000,
    max_value=10000000,
    value=50000,
    step=5000
)

continent = st.sidebar.selectbox(
    "Choose your preferred continent",
    [
        "Asia",
        "Europe",
        "North America",
        "South America",
        "Africa",
        "Oceania"
    ]
)

# Recommendation button
if st.sidebar.button("Find My Destination"):

    if name.strip() == "":
        st.warning("Please enter your name!")

    else:
        st.subheader(f"Hello {name}! 👋")
        st.write(f"Here are your travel recommendations.")

        # Filter destinations
        recommendations = df[
            (df["Continent"] == continent) &
            (df["Budget"] <= budget)
        ]

        if recommendations.empty:
            st.error(
                "Sorry! No destinations found "
                "within your budget. Try increasing it."
            )

        else:
            st.success(
                f"We found {len(recommendations)} "
                "destinations for you!"
            )

            for index, row in recommendations.iterrows():

                with st.container(border=True):

                    st.subheader(
                        f"📍 {row['Place']}, {row['Country']}"
                    )

                    col1, col2 = st.columns(2)

                    with col1:
                        st.write(
                            f"**Estimated budget:** "
                            f"₹{row['Budget']:,}"
                        )

                        st.write(
                            f"**Continent:** "
                            f"{row['Continent']}"
                        )

                    with col2:
                        st.write(
                            f"**Your age:** {age}"
                        )

                        st.write(
                            f"**Description:** "
                            f"{row['Description']}"
                        )

                    st.progress(
                        min(row["Budget"] / budget, 1.0)
                    )

                    st.caption(
                        "Estimated budget usage: "
                        f"{row['Budget']/budget*100:.1f}%"
                    )

# Footer
st.divider()
st.caption("✈️ Smart Travel Recommendation System | Python + Streamlit")
