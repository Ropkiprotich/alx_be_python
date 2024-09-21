weather_conditions1 = "sunny"
weather_conditions2 = "rainy"
weather_conditions3 = "cold"

current_weather = input("What's the weather like today? (sunny/rainy/cold):")
if current_weather == weather_conditions1:
    weather_conditions = "sunny"
    print("Wear a t-shirt and sunglasses.")
elif current_weather == weather_conditions2 :
    print("Don't forget your umbrella and a raincoat.")
elif current_weather == weather_conditions3:
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")