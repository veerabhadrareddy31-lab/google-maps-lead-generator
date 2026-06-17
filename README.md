## 📸 Excel Output Preview

| Preview 1 | Preview 2 | Preview 3 |
| :--- | :--- | :--- |
| ![Preview 1](output_preview1.png) | ![Preview 2](output_preview2.png) | ![Preview 3](output_preview3.png) |

# 🚀 Google Maps Business Lead Generator

A powerful Python-based automation tool built to scrape local business information from Google Maps listings and export data directly into structured Excel formats.

---

## 📌 Project Overview
Manual research for business leads is time-consuming. This tool streamlines the process by using **Selenium** and **Playwright** to interact with Google Maps, extract key business details, and organize them automatically for lead generation and market analysis.

## ⚡ Technical Features
- **Advanced Scraping:** Engineered with **Selenium** and **Playwright** for robust interaction with dynamic web elements.
- **Automated Intelligence:** Efficiently handles infinite scrolling to ensure complete data extraction.
- **Data Precision:** Captures Business Name, Phone Number, Address, Rating, and Website links.
- **Data Export:** Seamlessly processes and saves data into professional-grade **Excel (.xlsx)** or **CSV** formats using **Pandas**.

## 🛠 Tech Stack & Dependencies
- **Core Language:** Python
- **Automation Frameworks:** Selenium, Playwright
- **Data Handling:** Pandas, OpenPyXL
- **Environment:** WebDriver-Manager

## 🚀 Installation & Setup
1. **Clone the repository:**
```bash
git clone [https://github.com/veerabhadrareddy31-lab/google-maps-lead-generator.git](https://github.com/veerabhadrareddy31-lab/google-maps-lead-generator.git)

## 📊 Sample Output
The generated Excel file contains:
| Business Name | Phone Number | Address | Rating | Website |
| :--- | :--- | :--- | :--- | :--- |
| ABC Dental Clinic | +91 XXXXX XXXXX | Hyderabad | 4.7 | - |
| XYZ Dentists | +91 XXXXX XXXXX | Hyderabad | 4.5 | - |

## 🚀 Use Case
- **Input:** Business Type: Dentist | Location: Hyderabad
- **Output:** 100+ business leads collected.

## 📥 Installation
1. **Clone the repository:**   
  ```markdown
git clone https://github.com/veerabhadrareddy31-lab/google-maps-lead-generator.git
Install dependencies:
   pip install selenium playwright pandas openpyxl webdriver-manager
Run the script:
      python dentist_scraper.py
📊 Sample Data Structure
The final output is optimized for CRM or cold outreach workflows:
Business NamePhone NumberAddressRatingWebsite
Dental Clinic A+91 XXXXX XXXXXHyderabad4.8www.clinic-a.com
Dental Clinic B+91 XXXXX XXXXXHyderabad4.6-
📂 Project Structure:
google-maps-lead-generator/
│
├── dentist_scraper.py      # Main automation script
├── requirements.txt        # Project dependencies
├── output_data/            # Folder for generated Excel files
└── screenshots/            # Visual proof of results

⚠️ Disclaimer
This project is for educational purposes only. Ensure compliance with Google's Terms of Service and data privacy policies when scraping publicly available information.
Author: Veera Bhadra Reddy | GitHub: veerabhadrareddy31-lab
