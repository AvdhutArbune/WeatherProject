import requests
api_key="ddf370592e60d12228f54aa39fe38f44"
city_name=input("Enter the city name :") 
Weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&APPID={api_key}")
if(Weather_data.json()["cod"] == "404"):
    print("No city found")
else:    
    Weather=Weather_data.json()['weather'][0]["main"]
    temp=round(Weather_data.json()["main"]["temp"])
    # print(f"The Weather in {city_name} is:{Weather}")
    print(f"The tempreature in {city_name} is:{temp}°C")