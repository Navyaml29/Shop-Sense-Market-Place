import streamlit as st
import pandas as pd
from datetime import date, timedelta
import random

st.set_page_config(page_title="ShopSense", page_icon="🛍️", layout="wide")


USERS = {
    "Admin": ("admin@shopsense.com", "admin123"),
    "Vendor": ("vendor@shopsense.com", "vendor123"),
    "Customer": ("customer@shopsense.com", "customer123"),
}

CATEGORIES = [
    "Jewelry & Luxury", "Consumer Electronics", "Gourmet & Beverage",
    "Fashion & Apparel", "Home & Living", "Accessories"
]


st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f7f8ff, #eef8ff 55%, #fff4f8);
    color: #20233a;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #21145f, #4338a8, #176b87);
}
[data-testid="stSidebar"] * { color: white; }
.hero {
    padding: 1.2rem 1.4rem;
    border-radius: 18px;
    color: white;
    background: linear-gradient(110deg, #5428c7, #176bba, #13a89e);
    margin-bottom: 1rem;
}
.hero h1, .hero p { color: white; }
div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e3e8ff;
    border-left: 5px solid #6750d8;
    padding: 14px;
    border-radius: 14px;
    box-shadow: 0 4px 15px #232f6410;
}
div[data-testid="stMetricValue"] { color: #29205f; }
.stButton > button[kind="primary"] {
    background: linear-gradient(90deg, #6546dc, #1686c8);
    border: 0;
    border-radius: 10px;
    color: white;
    font-weight: 700;
}
.stButton > button { border-radius: 10px; }
h1, h2, h3 { color: #29205f; }
</style>
""", unsafe_allow_html=True)

def hero(title, subtitle):
    st.markdown(
        f'<div class="hero"><h1>{title}</h1><p>{subtitle}</p></div>',
        unsafe_allow_html=True
    )

def logout_button():
    if st.sidebar.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.role = ""
        st.rerun()


if "vendors" not in st.session_state:
    st.session_state.vendors = [
        {"Vendor ID": "V001", "Business Name": "Jewels", "Owner": "Sami",
         "Email": "sami@example.com", "Category": "Jewelry & Luxury", "Status": "Active"},
        {"Vendor ID": "V002", "Business Name": "Skills Store", "Owner": "Bheema",
         "Email": "skills@example.com", "Category": "Consumer Electronics", "Status": "Active"},
        {"Vendor ID": "V003", "Business Name": "Apex Gourmet", "Owner": "Ravi",
         "Email": "apex@example.com", "Category": "Gourmet & Beverage", "Status": "Pending"},
    ]


if "products" not in st.session_state:
    st.session_state.products = [
        {"Product ID": "P001", "Product": "Cups", "Category": "Home & Living",
         "Vendor": "Jewels", "Price (₹)": 2477, "Stock": 45},
        {"Product ID": "P002", "Product": "Laptop", "Category": "Consumer Electronics",
         "Vendor": "Skills Store", "Price (₹)": 25000, "Stock": 8},
        {"Product ID": "P003", "Product": "Bangles", "Category": "Jewelry & Luxury",
         "Vendor": "Jewels", "Price (₹)": 2230, "Stock": 6},
        {"Product ID": "P004", "Product": "Truffle Butter Jar", "Category": "Gourmet & Beverage",
         "Vendor": "Apex Gourmet", "Price (₹)": 280, "Stock": 64},
        {"Product ID": "P005", "Product": "Cotton Lounge Set", "Category": "Fashion & Apparel",
         "Vendor": "Skills Store", "Price (₹)": 1899, "Stock": 4},
    ]


if "transactions" not in st.session_state:
    random.seed(42)
    today = date.today()
    vendor_names = ["Jewels", "Skills Store", "Apex Gourmet"]
    product_details = [
        ("Cups", 2477),
        ("Laptop", 25000),
        ("Bangles", 2230),
        ("Truffle Butter Jar", 280),
        ("Cotton Lounge Set", 1899),
    ]
    order_statuses = ["Delivered", "Shipped", "Processing", "Cancelled"]
    transactions = []

    for i in range(683):
        product, price = random.choice(product_details)
        quantity = random.randint(1, 5)
        transactions.append({
            "Transaction ID": f"TXN{1001 + i}",
            "Date": str(today - timedelta(days=random.randint(0, 29))),
            "Vendor": random.choice(vendor_names),
            "Product": product,
            "Quantity": quantity,
            "Amount (₹)": price * quantity,
            "Status": random.choices(
                order_statuses, weights=[65, 20, 10, 5], k=1
            )[0],
        })
    st.session_state.transactions = transactions


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = ""


if not st.session_state.logged_in:
    _, center, _ = st.columns([1, 1.25, 1])
    with center:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            "<div class='hero' style='text-align:center'>"
            "<h1>🛍️ ShopSense</h1>"
            "<p>Multi-Vendor E-Commerce Analytics Platform</p></div>",
            unsafe_allow_html=True
        )
        st.subheader("🔐 Login to ShopSense")
        role_choice = st.selectbox("Login as", ["Admin", "Vendor", "Customer"])
        email = st.text_input("Email address", placeholder="Enter demo email")
        password = st.text_input("Password", type="password", placeholder="Enter password")

        if st.button("Sign In →", type="primary", use_container_width=True):
            expected_email, expected_password = USERS[role_choice]
            if email.strip().lower() == expected_email and password == expected_password:
                st.session_state.logged_in = True
                st.session_state.role = role_choice
                st.rerun()
            else:
                st.error("Incorrect email or password for the selected role.")

        with st.expander("Show demo credentials"):
            st.write("**Admin:** admin@shopsense.com / `admin123`")
            st.write("**Vendor:** vendor@shopsense.com / `vendor123`")
            st.write("**Customer:** customer@shopsense.com / `customer123`")
    st.stop()

role = st.session_state.role

if role == "Vendor":
    st.sidebar.markdown("## 🛍️ ShopSense")
    st.sidebar.caption("VENDOR PORTAL")
    st.sidebar.write("Signed in as **Vendor**")
    logout_button()
    hero("🏪 Vendor Dashboard", "Manage your store and review sample orders.")

    
    vendor_products = pd.DataFrame(st.session_state.products)
    if not vendor_products.empty:
        vendor_products = vendor_products[vendor_products["Vendor"] == "Jewels"]
    vendor_transactions = pd.DataFrame(st.session_state.transactions)
    if not vendor_transactions.empty:
        vendor_transactions = vendor_transactions[vendor_transactions["Vendor"] == "Jewels"]

    a, b, c = st.columns(3)
    a.metric("My Products", len(vendor_products))
    b.metric("My Orders", len(vendor_transactions))
    sales_total = vendor_transactions["Amount (₹)"].sum() if not vendor_transactions.empty else 0
    c.metric("Sample Sales", f"₹{sales_total:,.0f}")

    st.subheader("📦 My Products")
    st.dataframe(vendor_products, use_container_width=True, hide_index=True)
    st.subheader("🧾 My Orders")
    st.dataframe(vendor_transactions.head(100), use_container_width=True, hide_index=True)
    st.info("Demo account is linked to the sample store 'Jewels'. Vendor registration and vendor-specific account creation are not implemented.")
    st.stop()


if role == "Customer":
    st.sidebar.markdown("## 🛍️ ShopSense")
    st.sidebar.caption("CUSTOMER PORTAL")
    st.sidebar.write("Signed in as **Customer**")
    logout_button()
    hero("✨ Customer Marketplace", "Explore products from our demo vendors.")

    product_df = pd.DataFrame(st.session_state.products)
    query = st.text_input("🔎 Search products", placeholder="Search by product, category, or vendor")
    if query and not product_df.empty:
        mask = product_df.astype(str).apply(
            lambda col: col.str.contains(query, case=False, na=False)
        ).any(axis=1)
        product_df = product_df[mask]

    if product_df.empty:
        st.info("No products match your search.")
    else:
        cols = st.columns(3)
        for i, (_, product) in enumerate(product_df.iterrows()):
            with cols[i % 3]:
                st.markdown(f"### 🛒 {product['Product']}")
                st.write(product["Category"])
                st.write(f"Vendor: **{product['Vendor']}**")
                st.markdown(f"## ₹{product['Price (₹)']:,.0f}")
                st.caption(f"Stock available: {product['Stock']}")
                st.divider()

    st.info("Demo only: checkout, payments, and personal order history are not implemented.")
    st.stop()


st.sidebar.markdown("## 🛍️ ShopSense")
st.sidebar.caption("MARKETPLACE ANALYTICS")
page = st.sidebar.radio(
    "OVERVIEW & CONTROL",
    ["Dashboard", "Vendors", "Products", "Inventory", "Transactions",
     "Analytics", "Reports", "Settings"]
)
st.sidebar.divider()
st.sidebar.write("Signed in as **Admin**")
logout_button()

vendors_df = pd.DataFrame(st.session_state.vendors)
products_df = pd.DataFrame(st.session_state.products)
transactions_df = pd.DataFrame(st.session_state.transactions)


if page == "Dashboard":
    hero("📊 Dashboard Overview", "Here's what's happening with your marketplace today.")

    revenue = int(transactions_df["Amount (₹)"].sum()) if not transactions_df.empty else 0
    active_vendors = int((vendors_df["Status"] == "Active").sum()) if not vendors_df.empty else 0

    a, b, c, d = st.columns(4)
    a.metric("💰 Total Revenue", f"₹{revenue:,.0f}")
    b.metric("🧾 Orders", f"{len(transactions_df):,}")
    c.metric("🏪 Active Vendors", active_vendors)
    d.metric("📦 Products", len(products_df))

    x, y, z = st.columns([1.4, 1, 1])
    with x:
        st.subheader("📈 Sales Overview")
        st.caption("Sample revenue by transaction date")
        if not transactions_df.empty:
            sales = transactions_df.copy()
            sales["Date"] = pd.to_datetime(sales["Date"])
            daily_sales = sales.groupby("Date")["Amount (₹)"].sum().sort_index()
            st.line_chart(daily_sales, color="#16a6a0")
        else:
            st.info("No sales data available.")

    with y:
        st.subheader("🚚 Order Status")
        if not transactions_df.empty:
            st.bar_chart(transactions_df["Status"].value_counts(), color="#6546dc")
        else:
            st.info("No orders available.")

    with z:
        st.subheader("🧺 Top Categories")
        if not products_df.empty:
            st.bar_chart(products_df.groupby("Category").size(), color="#f28c45")
        else:
            st.info("No products available.")

    st.subheader("🧾 Recent Transactions")
    st.dataframe(transactions_df.head(10), use_container_width=True, hide_index=True)


elif page == "Vendors":
    hero("🏪 Registered Vendors", "Register and search merchant profiles.")

    with st.expander("➕ Register a Vendor"):
        with st.form("vendor_form", clear_on_submit=True):
            business = st.text_input("Business / Store Name")
            owner = st.text_input("Owner Full Name")
            email = st.text_input("Contact Email")
            category = st.selectbox("Category", CATEGORIES)
            submitted = st.form_submit_button("Complete Registration", type="primary")

            if submitted:
                if not business.strip() or not owner.strip() or not email.strip():
                    st.error("Please fill in all fields.")
                elif "@" not in email or "." not in email.split("@")[-1]:
                    st.error("Enter a valid email address.")
                elif email.lower() in [v["Email"].lower() for v in st.session_state.vendors]:
                    st.error("This vendor email already exists.")
                else:
                    new_id = f"V{len(st.session_state.vendors) + 1:03d}"
                    st.session_state.vendors.append({
                        "Vendor ID": new_id,
                        "Business Name": business.strip(),
                        "Owner": owner.strip(),
                        "Email": email.strip(),
                        "Category": category,
                        "Status": "Pending",
                    })
                    st.success(f"Vendor registered: {new_id}")
                    st.rerun()

    vendor_df = pd.DataFrame(st.session_state.vendors)
    query = st.text_input("🔎 Search vendor, owner, or email")
    status_filter = st.selectbox("Status filter", ["All", "Active", "Pending", "Suspended"])

    if query:
        mask = vendor_df.astype(str).apply(
            lambda col: col.str.contains(query, case=False, na=False)
        ).any(axis=1)
        vendor_df = vendor_df[mask]
    if status_filter != "All":
        vendor_df = vendor_df[vendor_df["Status"] == status_filter]

    st.dataframe(vendor_df, use_container_width=True, hide_index=True)


elif page == "Products":
    hero("🛍️ Product Catalog", "View and add marketplace products.")

    with st.expander("➕ Add New Product"):
        with st.form("product_form", clear_on_submit=True):
            name = st.text_input("Product name")
            category = st.selectbox("Product category", CATEGORIES)
            vendor_names = [v["Business Name"] for v in st.session_state.vendors]
            vendor = st.selectbox("Vendor", vendor_names if vendor_names else ["No vendors registered"])
            price = st.number_input("Price (₹)", min_value=0.0, step=50.0)
            stock = st.number_input("Initial stock", min_value=0, step=1)
            submitted = st.form_submit_button("Add Product", type="primary")

            if submitted:
                if not name.strip():
                    st.error("Enter a product name.")
                elif not vendor_names:
                    st.error("Register a vendor first.")
                else:
                    new_id = f"P{len(st.session_state.products) + 1:03d}"
                    st.session_state.products.append({
                        "Product ID": new_id,
                        "Product": name.strip(),
                        "Category": category,
                        "Vendor": vendor,
                        "Price (₹)": price,
                        "Stock": int(stock),
                    })
                    st.success("Product added.")
                    st.rerun()

    product_df = pd.DataFrame(st.session_state.products)
    query = st.text_input("🔎 Search product, category, or vendor")
    if query:
        mask = product_df.astype(str).apply(
            lambda col: col.str.contains(query, case=False, na=False)
        ).any(axis=1)
        product_df = product_df[mask]
    st.dataframe(product_df, use_container_width=True, hide_index=True)


elif page == "Inventory":
    hero("📦 Inventory Management", "Monitor stock and restock products.")
    product_df = pd.DataFrame(st.session_state.products)
    low_stock = product_df[product_df["Stock"] <= 15] if not product_df.empty else product_df

    if not low_stock.empty:
        st.warning(f"⚠️ {len(low_stock)} product(s) are at or below the 15-unit reorder threshold.")
    else:
        st.success("All products are above the reorder threshold.")

    st.dataframe(
        product_df[["Product ID", "Product", "Vendor", "Stock"]],
        use_container_width=True, hide_index=True
    )

    if not product_df.empty:
        selected_product = st.selectbox("Choose product to restock", product_df["Product"].tolist())
        quantity = st.number_input("Quantity to add", min_value=1, step=1)
        if st.button("Restock Inventory", type="primary"):
            index = next(
                i for i, item in enumerate(st.session_state.products)
                if item["Product"] == selected_product
            )
            st.session_state.products[index]["Stock"] += int(quantity)
            st.success(f"Added {int(quantity)} units to {selected_product}.")
            st.rerun()


elif page == "Transactions":
    hero("🧾 Transactions Ledger", "Review sample orders and sales.")

    transaction_df = pd.DataFrame(st.session_state.transactions)
    a, b, c = st.columns(3)
    total_amount = transaction_df["Amount (₹)"].sum() if not transaction_df.empty else 0
    a.metric("💰 Gross Revenue", f"₹{total_amount:,.0f}")
    b.metric("🧾 Total Orders", f"{len(transaction_df):,}")
    c.metric("🏷️ Catalog SKUs", len(st.session_state.products))

    query = st.text_input("🔎 Search vendor, product, or transaction ID")
    if query and not transaction_df.empty:
        mask = transaction_df.astype(str).apply(
            lambda col: col.str.contains(query, case=False, na=False)
        ).any(axis=1)
        transaction_df = transaction_df[mask]

    st.dataframe(transaction_df, use_container_width=True, hide_index=True)
    st.download_button(
        "⬇️ Export Transactions CSV",
        data=transaction_df.to_csv(index=False).encode("utf-8"),
        file_name="shopsense_transactions.csv",
        mime="text/csv"
    )


elif page == "Analytics":
    hero("📈 Marketplace Analytics", "Compare revenue and product categories.")

    transaction_df = pd.DataFrame(st.session_state.transactions)
    product_df = pd.DataFrame(st.session_state.products)

    if not transaction_df.empty:
        st.subheader("Vendor Revenue Comparison")
        vendor_revenue = transaction_df.groupby("Vendor")["Amount (₹)"].sum().sort_values(ascending=False)
        st.bar_chart(vendor_revenue, color="#6546dc")

        st.subheader("Revenue Over Time")
        dated_transactions = transaction_df.copy()
        dated_transactions["Date"] = pd.to_datetime(dated_transactions["Date"])
        daily_revenue = dated_transactions.groupby("Date")["Amount (₹)"].sum().sort_index()
        st.line_chart(daily_revenue, color="#16a6a0")

    if not product_df.empty:
        st.subheader("Product Category Distribution")
        st.bar_chart(product_df.groupby("Category").size(), color="#f28c45")


elif page == "Reports":
    hero("📑 Reports Center", "Download marketplace data as CSV files.")

    reports = [
        ("Vendors", pd.DataFrame(st.session_state.vendors), "shopsense_vendors.csv"),
        ("Products", pd.DataFrame(st.session_state.products), "shopsense_products.csv"),
        ("Transactions", pd.DataFrame(st.session_state.transactions), "shopsense_transactions.csv"),
    ]
    for label, data, filename in reports:
        st.download_button(
            f"⬇️ Download {label} CSV",
            data=data.to_csv(index=False).encode("utf-8"),
            file_name=filename,
            mime="text/csv",
            key=f"download_{label.lower()}"
        )


elif page == "Settings":
    hero("⚙️ Settings", "Application information and demo configuration.")
    st.write("**Application:** ShopSense – Multi-Vendor E-Commerce Analytics Platform")
    st.write("**Milestone:** Milestone 1 interface prototype")
    st.write("**Demo orders:** 683 generated sample transactions")
    st.write("*Data mode:* Sample data stored in Streamlit session state")
    st.warning(
        "Demo credentials are hardcoded. Data may reset when the app session restarts. "
        "Use a database and secure authentication before deployment."
    )
