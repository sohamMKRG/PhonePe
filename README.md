📘 PhonePe Pulse – Digital Payments Visualization (2018–2023)
Interactive Tableau Dashboard | FinTech | Geospatial Analytics

📌 Table of Contents

Overview

Dashboard Link

Key Features

Dataset Description

KPIs

Visualizations

Insights

Project Files

Tech Stack

How to Run

Author

🚀 Overview

This project visualizes 6 years of digital payment activity in India using data from the PhonePe Pulse GitHub Repository.

The goal was to:
✔ Clean & preprocess raw JSON data
✔ Build structured analytical datasets
✔ Create an interactive Tableau dashboard
✔ Reveal insights about user behavior, transaction trends, and geographical patterns

This dashboard is ideal for analysts, fintech companies, educators, and anyone studying India’s digital adoption.

🔗 Dashboard Link

👉 Live Tableau Dashboard:
https://public.tableau.com/shared/J4JWGXG7P?:display_count=n&:origin=viz_share_link

⭐ Key Features

📍 State-wise & district-wise payment insights

📈 Yearly & quarterly growth trends

🧭 Geospatial heatmaps (Users & Transactions)

🏆 Top 10 states & districts

💳 Transaction-type distribution

📊 KPIs summarizing national digital performance

🎛️ 10+ filters for deep exploration

📂 Dataset Description

The project uses cleaned and merged CSV datasets derived from PhonePe Pulse.

File	Description
master_transactions.csv	Txn amount, count, category, state, district, year, quarter
master_users.csv	Registered users, geography, device brands, yearly & quarterly data
master_full.csv	Combined data for validation
🧮 KPIs

Total Transactions: 200,709,555,401

Total Amount: ₹336,062,724,825,438

Total Users: 7,862,007,266

Average Ticket Size: ₹1,674.37

Top Performing State: Telangana

📊 Visualizations

Your dashboard includes:

1️⃣ Geo Visuals

State-wise transaction map

State-wise user map

2️⃣ Trend Charts

Yearly transactions

Yearly registered users

Quarterly transactions

Quarterly registered users

3️⃣ Top Analysis

Top 10 states by amount

Top 10 districts by users

4️⃣ Other Visuals

Transaction type donut chart

User heatmap by district

🔍 Insights
⭐ Geographic Insights

Telangana, Karnataka, and Maharashtra lead the digital payments ecosystem.

Bengaluru Urban is the top-performing district in India.

⭐ Trend Insights

Exponential growth from 2018 to 2023.

Q3 & Q4 show consistently higher activity.

⭐ User Insights

Registered user base nearly tripled post-2020.

Urban centers dominate user growth.

⭐ Transaction Insights

Recharge & Bill Payments lead the transaction mix.

P2P payments show steady year-on-year rise.

📁 Project Files

Your repo should contain:

📦 phonepe-pulse-data-visualization
 ┣ 📂 data
 ┃ ┣ master_users.csv
 ┃ ┣ master_transactions.csv
 ┃ ┗ master_full.csv
 ┣ 📂 docs
 ┃ ┗ PhonePe_Pulse_Project_Report.docx
 ┣ 📂 presentation
 ┃ ┗ PhonePe_Pulse_Project_Premium_Presentation.pptx
 ┣ 📂 screenshots
 ┃ ┣ dashboard_main.png
 ┃ ┣ yearly_trends.png
 ┃ ┣ quarterly_trends.png
 ┃ ┣ maps.png
 ┃ ┣ donut.png
 ┃ ┗ heatmap.png
 ┣ README.md

🛠 Tech Stack

Tableau Public – Dashboard & geospatial analytics

Python / Pandas – Data cleaning & merging

MS PowerPoint – Presentation

MS Word – Project report

▶ How to Run

Download the repository

Open the datasets to inspect the cleaned data

View the Tableau Public dashboard online

Optionally recreate the dashboard using the .twbx or dataset files
