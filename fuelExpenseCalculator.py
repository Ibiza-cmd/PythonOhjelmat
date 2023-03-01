#Car consumption calculator tool in python that should fetch average prices for fuel and electricity and then calculate yearly expenses



import requests
from bs4 import BeautifulSoup

# Define the URLs to scrape the fuel and kWh price data from
fuel_url = "https://www.polttoaine.net/index.php?hakusana=&maa=5"
kwh_url = "https://www.sahkovertailu.fi/sahko-hinnat"

# Take input from user for car manufacturer, model, and consumption
car_manufacturer = input("Enter your car manufacturer: ")
car_model = input("Enter your car model: ")
consumption = float(input("Enter your car's fuel consumption (either 100km/litre or kWh per 100km): "))

# Take input from user for yearly drive kilometers
yearly_drive_km = float(input("Enter your yearly drive kilometers: "))

# Calculate yearly expenses for a petrol car
response = requests.get(fuel_url)
soup = BeautifulSoup(response.content, 'html.parser')
fuel_price_avg = float(soup.find_all("div", class_="price-value")[0].text.replace(',', '.'))
yearly_fuel_expenses = yearly_drive_km * (consumption / 100) * fuel_price_avg

# Calculate yearly expenses for an electric car
response = requests.get(kwh_url)
soup = BeautifulSoup(response.content, 'html.parser')
kwh_price_avg = float(soup.find("td", class_="energy-price__value").text.replace(',', '.'))
yearly_kwh_expenses = yearly_drive_km * (consumption / 100) * kwh_price_avg

# Print the results
print("For a", car_manufacturer, car_model, "driving", yearly_drive_km, "km per year, the yearly expenses are:")
print("For a petrol car, the yearly expenses are:", round(yearly_fuel_expenses, 2), "EUR")
print("For an electric car, the yearly expenses are:", round(yearly_kwh_expenses, 2), "EUR")
