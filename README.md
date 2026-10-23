# ShopSense -- Multi-Vendor E-Commerce Analytics Platform
ShopSense is a colorful web application prototype built with Python, Streamlit, and Pandas. It demonstrates a multi-vendor marketplace where administrators manage vendors, products, inventory, and transaction reports; vendors review sample store data; and customers browse products.

# Project status: Milestone 1 prototype. The application uses generated demo data and Streamlit session state. It is not connected to a permanent database, and checkout/payment functionality is not implemented.

# Features
# Admin
Dashboard cards for revenue, orders, active vendors, and products
Sales overview, order-status, and product-category charts
Register and search vendors
Add and search products
Monitor low-stock products and restock inventory
Browse and search transactions
Export vendor, product, and transaction data as CSV files

# Vendor
Demo vendor dashboard
View sample products and orders for the Jewels store
View sample sales totals

# Customer
Browse the product catalog
Search by product name, category, or vendor
View prices and available stock

# General
Colorful gradient theme
Separate demo logins for Admin, Vendor, and Customer
683 generated sample transactions for charts and reports
Logout functionality

# Technology Stack
Python -- application logic
Streamlit -- web interface
Pandas -- data tables, filtering, and calculations
HTML/CSS -- custom colors and layout
Python datetime and random -- generated demo transaction data

# Requirements
Python 3.9 or newer recommended
pip
VS Code or another code editor (optional)

# Installation and Run Instructions
Download and extract the project ZIP.
Open the project folder in VS Code.
Select Terminal → New Terminal.

# Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run app.py
Open the local URL shown in the terminal, usually http://localhost:8501.

# Demo Login Credentials
Role       Email                      Password
Admin      admin@shopsense.com      admin123 Vendor     vendor@shopsense.com     vendor123 Customer   customer@shopsense.com   customer123
These credentials are for local demonstration only. Do not use hardcoded credentials in a deployed application.

# Project Structure
ShopSense/
├── app.py
├── requirements.txt
└── README.md

# How the Application Works
The login page asks the user to select a role and enter matching demo credentials.
Admin opens the marketplace management dashboard.
Vendor sees sample data mapped to the Jewels store.
Customer sees the product catalog and search.
Admin can add vendors and products, restock products, inspect transactions, and download CSV reports.
Dashboard charts and summary cards use generated sample transactions.

# Data and Limitations
The 683 transactions are simulated data, not real customer orders or sales.
Data is held in st.session_state and may reset when the app session restarts.
The Vendor demo account is mapped to the Jewels sample store.
Vendor-specific account creation and full permissions are not implemented.
Customer checkout, payments, and personal order history are not implemented.
Login credentials are hardcoded and are not suitable for production.
No persistent database is currently connected.

# Future Enhancements
Integrate SQLite or PostgreSQL for persistent storage.
Add secure password hashing and role-based authorization.
Create vendor registration and individual vendor accounts.
Add shopping cart, checkout, order placement, and payment integration.
Save orders and update inventory automatically.
Add date filters, more detailed analytics, and automated tests.

# Project Information
Project: ShopSense -- Multi-Vendor E-Commerce Analytics Platform
Purpose: Prototype for inventory control, marketplace management, and sales analytics.
For an internship presentation, explain clearly which features are implemented and which are planned enhancements. The current version is a prototype using sample data.
