import streamlit as st

st.set_page_config(
    page_title="ShopSense Admin",
    layout="wide"
)

# Login page
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("ShopSense Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    st.subheader("CAPTCHA")
    st.write("What is 3 + 4?")
    answer = st.text_input("Enter CAPTCHA answer")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            if answer == "7":
                st.session_state.login = True
                st.rerun()
            else:
                st.error("Incorrect CAPTCHA")
        else:
            st.error("Incorrect username or password")

else:
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

    if st.button("Logout"):
        st.session_state.login = False
        st.rerun()
