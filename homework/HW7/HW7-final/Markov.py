import numpy as np
import random

class Markov:
    def __init__(self, *args): # You will need to modify this header line later in Part C
        self.data = []
        self.strings = ["sunny", "cloudy", "rainy", "snowy", "windy", "hailing"]
        self.dict = {"sunny":0, "cloudy":1, "rainy":2, "snowy":3, "windy":4, "hailing":5}
        if args: 
            self.day_zero_weather = args[0]
        else:
            self.day_zero_weather = None
            print("input the current day's weather to begin the simulation") 
        

    def load_data(self, file_path='./weather.csv'):
        # Your implementation here
        self.data = np.genfromtxt('weather.csv', delimiter=",")

    def get_prob(self, current_day_weather, next_day_weather): 
        # Your implementation here
        day1 = current_day_weather.lower()
        day2 = next_day_weather.lower()
        assert all(x in self.strings for x in [day1, day2]), "must be one of the specified weather strings"
        #assert day1 in self.strings, "must be one of the specified strings"
        return self.data[self.dict.get(day1)][self.dict.get(day2)]
    
    def __iter__(self):
        #Hint: self.get_prob() might come in handy here.
        assert (self.day_zero_weather in self.strings), "must input the current day weather as one of the specified weather strings"
        #probability_distribution = self.data[self.dict.get(self.day_zero_weather)]
        #feed in all probability data to iterator instance
        instance = MarkovIterator(self.data, self.day_zero_weather)
        return iter(instance)
    
    def _simulate_weather_for_day(self, day):
        assert day >= 0, "day must be non-negative"
        if day == 0:
            return self.day_zero_weather
        else:
            #instantiate iterator
            iterator = self.__iter__()
            indexDay = 0
            nextweather = None
            #repeat iteration for "day" number of days
            for x in range(0, day):
                nextweather = iterator.__next__()
            return nextweather
        
    def get_weather_for_day(self, day, trials):
        trialResults = []
        #already instantiates an iterator and returns a result
        for x in range(0, trials):
                weather = self._simulate_weather_for_day(day)
                trialResults.append(weather)
        #Assign a default value to trials
        return trialResults
        
    
class MarkovIterator:
    def __init__(self, data, day_zero_weather):
        self.day0 = day_zero_weather
        self.data = data
        self.dict = {"sunny":0, "cloudy":1, "rainy":2, "snowy":3, "windy":4, "hailing":5}
        self.index = self.dict.get(self.day0)
        #self.prob = self.data[self.index]
        

    def __next__(self): 
        #takes in probability and outputs a weather
        next_day_weather = random.choices(list(self.dict.keys()), weights=self.data[self.index], k=1)[0]
        self.index = self.dict.get(next_day_weather)
        return next_day_weather
        
    def __iter__(self):
        return self