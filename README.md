## 📸 Excel Output Preview

| Preview 1 | Preview 2 | Preview 3 |
| :--- | :--- | :--- |
| ![Preview 1](output_preview1.png) | ![Preview 2](output_preview2.png) | ![Preview 3](output_preview3.png) |

Google Maps Business Lead Generator

A Python-based automation tool that collects publicly available local business information from Google Maps and exports the results into an Excel file.

Overview

This project automates the process of collecting local business leads from Google Maps. It gathers important business information and saves the results into a structured Excel spreadsheet, making it useful for lead generation, market research, and business analysis.

Features

- Collects business names
- Extracts phone numbers
- Extracts addresses
- Extracts ratings
- Extracts website links (when available)
- Exports data to Excel (.xlsx)
- Automated data collection using Selenium and Playwright

Technologies Used

- Python
- Selenium
- Playwright
- Pandas
- OpenPyXL
- WebDriver Manager

Sample Output

The generated Excel file contains:

Business Name| Phone Number| Address| Rating| Website

Example Use Case

Input:

- Business Type: Dentist
- Location: Hyderabad

Output:

- 100+ business leads collected
- Business Name
- Phone Number
- Address
- Rating
- Website

Installation

Install the required dependencies:

pip install selenium playwright pandas openpyxl webdriver-manager

Usage

Run the script:

python dentist_scraper.py

After execution, the collected business data will be automatically exported to an Excel file.

Project Structure

google-maps-business-lead-generator/
│
├── dentist_scraper.py
├── README.md
├── sample_data.csv
└── screenshot.png

Disclaimer

This project is intended for educational purposes and for collecting publicly available information only. Users should respect Google Maps Terms of Service and applicable laws when using this tool.

Author

Veera Bhadra Reddy

GitHub: veerabhadrareddy31-lab
