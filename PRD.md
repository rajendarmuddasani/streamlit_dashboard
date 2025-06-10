# Project Requirements Document (PRD) for Infineon Product Dashboard

## Goal

Build a modern, interactive dashboard for Infineon product sales data, focused on **geographical insights** (region-based analysis).

<!-- TODO: Want to focus on something else? Change the focus here! (e.g., category trends, highlighting and displaying top-selling products, etc.) -->

## Technology Stack

- **Frontend**: Streamlit (for building the dashboard)
- **Backend**: Python (for data processing and visualization)
- **Data Visualization Libraries**: Plotly (for creating charts and graphs)

<!-- TODO: Prefer Dash or another Python-based tool? Swap out the stack and see what Copilot does! -->

All project dependencies must be managed using a `requirements.txt` file. Use Python's built-in `venv` module to create an isolated virtual environment for development and deployment.

## Data

Our Infineon product data is stored in the data folder as a CSV file named `infineon_product_data.csv`. The data includes the following columns:

```
product_name, product_family, product_category, tags, applications, url, image_url, price, region, units_sold, date
```
An example row might look like this:

```
XENSIV™ BGT60ATR24C,XENSIV™,Sensor,"XENSIV™,60GHz radar sensors for automotive",Automotive,https://www.infineon.com/cms/en/product/sensor/radar-sensors/radar-sensors-for-automotive/60ghz-radar/bgt60atr24c/,https://www.infineon.com/export/sites/default/media/products/Sensors/PG-VFWLB-76-1-web.png_11474957.png,$25.92,South America,40,1/27/2025
```

## Directory Structure

Most of the directory structure is already set up, but here’s a quick overview of what it should look like:

```
GithubCopilotWorkshop/
├── data/
│   └── infineon_product_data.csv
├── pictures/
│   └── dashboard_mockup_1.png
│   └── Colour_palette.png
├── requirements.txt
├── PRD.md
├── README.md
└── streamlit_app.py
```

<!-- TODO: Want to organize differently? (e.g., have folders like 'preprocessing', 'notebooks', or 'tests')? Go for it! -->

## Dashboard Components

The dashboard should focus on **geographical sales insights** and match the following layout and style:

- **Sidebar (Dark Mode):**
  - Infineon logo
  - Filters:
    - Region (dropdown)
    - Product Category (dropdown)
    - Date Range (date picker)
- **Main Area (Light Mode):**
  - **Header:** "Infineon Sales & Revenue Dashboard"
  - **KPI Cards:**
    - Total Revenue
    - Units Sold
    - Unique Products
    - Regions
  - **Charts:**
    - **Revenue by Region:** Donut or polar bar chart, using Infineon brand colors for each region
    - **Revenue by Product Category:** Bar chart, colored by category
    - **Revenue and Units Sold Over Time:** Line chart, with region selection buttons/toggles

<!-- TODO: Want to add a map, a table, or a new KPI? Just add it here and see what Copilot builds! -->

<!-- TODO: OR: -->

<!-- TODO: Try describing a totally different app (like a product catalog or interactive explorer) and watch Copilot adapt! -->

### Visual Layout

Below is a wireframe-style layout for the dashboard:

```
+---------------------------------------------------------------+
|                        Infineon Sales & Revenue Dashboard     |
|---------------------------------------------------------------|
|  [KPI: Total Revenue]  [KPI: Units Sold]  [KPI: Unique Prod.] |
|  [KPI: Regions]                                            |
|---------------------------------------------------------------|
|  Revenue by Region (Donut/Polar Chart)   | Revenue by Product |
|                                          | Category (Bar)     |
|------------------------------------------+--------------------|
|  Revenue and Units Sold Over Time (Line Chart, region toggle) |
+---------------------------------------------------------------+

Sidebar (left, dark mode):
+-------------------+
|  Infineon Logo    |
|-------------------|
|  Filters:         |
|   - Region        |
|   - Product Cat.  |
|   - Date Range    |
+-------------------+
```

- Sidebar is always visible on the left in dark mode, with logo and filters.
- Main area is light mode, with header, KPIs, and charts as shown above.
- Charts use Infineon brand colors for clarity and consistency.

<!-- TODO: Draw your own wireframe, or describe your dream dashboard layout -->

## Acceptance Criteria
- Dashboard is built in Streamlit, fully deployable, and responsive.
- Sidebar stays in dark mode with Infineon logo and interactive filters.
- Main area uses a light mode theme with clear, readable text and modern layout.
- KPIs and charts use Infineon brand colors, are interactive, and update in real time with filters.
- Data is loaded, cleaned, and aggregated correctly for accurate, user-friendly visuals.

<!-- TODO: What does "success" look like for you? Add or change criteria to match your vision! -->

