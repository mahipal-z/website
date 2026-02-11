import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome to run in the background
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    print("Visiting app URL...")
    driver.get("https://mahipal-zanakat.streamlit.app/")
    
    # Wait to see if the 'Wake it back up' button from your image appears
    wait = WebDriverWait(driver, 20)
    button_text = "Yes, get this app back up!"
    
    try:
        # Looking for the specific blue button from your screenshot
        wake_button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(., '{button_text}')]")))
        wake_button.click()
        print("✅ Clicked 'Wake up' button successfully.")
        # Give it a few seconds to start the boot process
        time.sleep(10) 
    except:
        print("✅ App was already awake (button not found).")

finally:
    driver.quit()
