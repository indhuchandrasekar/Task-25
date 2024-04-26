from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the IMDb search page
driver.get("https://www.imdb.com/search/name/")

# Define input data
input_data = {
    'name': 'Tom Cruise',
    'birth_month': 'July',
    'birth_day': '3',
    'birth_year': '1962',
    'profession': 'Actor',
    'gender': 'Male'
}

# Fill in the input fields
name_input = driver.find_element(By.ID, 'searchField')
name_input.send_keys(input_data['name'])

birth_month_select = driver.find_element(By.ID, 'birth_month')
birth_month_select.send_keys(input_data['birth_month'])

birth_day_select = driver.find_element(By.ID, 'birth_day')
birth_day_select.send_keys(input_data['birth_day'])

birth_year_select = driver.find_element(By.ID, 'birth_year')
birth_year_select.send_keys(input_data['birth_year'])

profession_select = driver.find_element(By.ID, 'profession')
profession_select.send_keys(input_data['profession'])

gender_select = driver.find_element(By.ID, 'gender')
gender_select.send_keys(input_data['gender'])

# Click the search button
search_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
search_button.click()

# Explicit wait for the search results to appear
wait = WebDriverWait(driver, 10)
search_results = wait.until(EC.visibility_of_element_located((By.ID, 'search-results')))

# Print the search results URL
print("Search Results URL:", driver.current_url)

# Close the browser
driver.quit()
