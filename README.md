## 📸 Excel Output Preview

| Preview 1 | Preview 2 | Preview 3 |
| :--- | :--- | :--- |
| ![Preview 1](output_preview1.png) | ![Preview 2](output_preview2.png) | ![Preview 3](output_preview3.png) |

# 🚀 Google Maps Business Lead Generator

A Python-based automation tool that collects publicly available local business information from map listings and exports the results into an Excel file.

---

## 📌 Overview
This project automates the process of collecting local business leads from map listings. It gathers key business information and saves the results into a structured Excel spreadsheet, making it useful for lead generation, market research, and data analysis.

## ⚡ Features
- **Collects business names**
- **Extracts phone numbers**
- **Extracts business addresses**
- **Extracts ratings**
- **Extracts website links** (when available)
- **Exports data to Excel (.xlsx)**
- **Automated data collection using Python**

## 🛠 Technologies Used
- **Python**
- **Playwright**
- **Pandas**
- **OpenPyXL**

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
   git clone [https://github.com/veerabhadrareddy31-lab/google-maps-lead-generator.git](https://github.com/veerabhadrareddy31-lab/google-maps-lead-generator.git)

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
