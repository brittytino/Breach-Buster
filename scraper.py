from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Configure Selenium WebDriver (adjust path to chromedriver)
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode for scraping without a GUI
service = Service(executable_path='C:\chromedriver.exe')  # Update this to the correct path
driver = webdriver.Chrome(service=service, options=chrome_options)

def scrape_vulnerabilities(url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    vulnerabilities = []

    # Example parsing logic, adjust based on actual OEM HTML structure
    vuln_items = soup.find_all('div', class_='vuln-item')  # Adjust the class based on actual HTML
    for item in vuln_items:
        product_name = item.find('h2').text.strip()
        severity = item.find('span', class_='severity').text.strip()
        description = item.find('p', class_='description').text.strip()
        mitigation = item.find('a', class_='mitigation-link')['href']

        vulnerabilities.append({
            'product_name': product_name,
            'severity': severity,
            'description': description,
            'mitigation': mitigation
        })

    return vulnerabilities
