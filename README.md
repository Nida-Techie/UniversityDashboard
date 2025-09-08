University Dashboard & Website Integration

Project Overview

This project demonstrates the management and visualization of university data using MySQL and Apache Superset, deployed via Docker, and embedded into a custom website for public access. Users can explore university metrics such as student count by department and course enrollments.

Objectives

Import and manage university data in a MySQL database.

Visualize insights using Apache Superset dashboards.

Enable public embedding of dashboards into a custom HTML/CSS website.

Demonstrate end-to-end deployment using Docker.

Features

MySQL Database: Contains all university-related tables and records.

Apache Superset: Interactive charts and dashboards for data visualization.

Dashboard Embedding: Live dashboards integrated into a custom website.

Docker Deployment: Easy setup and reproducibility of the full environment.

🛠️ Setup Instructions
1. Import Database

Create a new MySQL database named university.

Import the SQL file largeRelationsInsertFile.sql into MySQL.

2. Install Apache Superset

Use Docker Compose to set up Superset:

docker-compose up


Access Superset at http://localhost:8088
.

3. Connect Superset to MySQL

Add a new database connection in Superset pointing to your local MySQL university database.

Verify tables are accessible and ready for visualization.

4. Create a Dashboard

Create at least 2 charts (e.g., student count by department, course enrollments).

Combine charts into a single dashboard.

Enable public embedding for the dashboard.

5. Build a Website

Create a simple HTML/CSS website.

Embed the Superset dashboard using <iframe> or Superset's Embedded SDK.

Ensure the website displays the live dashboard without requiring login.

Repository Structure
UniversityDashboard/
│
├── docker-compose.yml
├── superset_config.py
├── largeRelationsInsertFile.sql
├── website/
│   ├── index.html
│   └── style.css
└── README.md

Screenshots

(Add a screenshot of your live website with the embedded dashboard here)

![Dashboard Screenshot](website/screenshot.png)



🔗 Live Demo: https://yourwebsite.com
