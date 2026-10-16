import streamlit as st

st.set_page_config(
    page_title="ShopSense Admin",
    layout="wide"
)

st.title("ShopSense Admin - Marketplace Foundation")

# Sidebar menu
with st.sidebar:
    st.write("Dashboard")
    st.write("Vendors")
    st.write("Products")
    st.write("Transactions")

# Vendor onboarding form
st.header("Vendor Onboarding")

business_name = st.text_input("Business Name")
contact_email = st.text_input("Contact Email")

# Submit button
if st.button("Submit"):
    if business_name != "" and contact_email != "":
        st.success("Vendor submitted successfully")
    else:
        st.warning("Please enter both details")

# Vendor details
st.subheader("Vendors")

st.table({
    "Vendor ID": [""],
    "Status (Pending)": [""]
})