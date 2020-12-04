import operator
from Markov import Markov 

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

highestOccurance = {}

def rollup(list):
    return {i:list.count(i) for i in list}

for key in city_weather:
    city = key
    current = city_weather[key]
    weather_today = Markov(current)
    weather_today.load_data(file_path='./weather.csv')
    results = weather_today.get_weather_for_day(7,100)
    print(city + ": " + str(rollup(results)))
    highestOccurance[city] = max(rollup(results).items(), key=operator.itemgetter(1))[0]
    
print("\nMost likely weather in seven days\n" + "----------------------------------\n" + str(highestOccurance))