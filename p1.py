import requests

def get_weather(city_name, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()  
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            print(f"آب و هوای شهر {city_name}:")
            print(f"- وضعیت: {weather}")
            print(f"- دما: {temperature}°C")
            print(f"- رطوبت: {humidity}%")
            print(f"- سرعت باد: {wind_speed} متر بر ثانیه")
        else:
            print("شهر مورد نظر پیدا نشد یا مشکلی در ارتباط با API وجود دارد.")
    except Exception as e:
        print("خطا در دریافت اطلاعات:", e)

city_name = input("نام شهر را وارد کنید: ")
api_key = "b809a595f6649fd29a66c7a0d7ff96fc"  
get_weather(city_name, api_key)