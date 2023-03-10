#Wind Chill Calculator
import math


t = float(input('What is the temperature? '))

f_or_c = input('Fahrenheit or Celsius (F/C)? ')

v = 0

def to_celsius (f):
    return int ( (f - 32) / 1.8)

def to_fahrenheit (c):
    return int (c * 1.8 + 32)

def compute_wind_chill (temperature):
   
    wind = 35.74 + 0.6215*temperature - 35.75*math.pow(v, 0.16) + 0.4275*temperature*math.pow(v, 0.16)
    print(f'At temperature {t}F, and wind speed of {v} mph, the windchill is: {wind:.2f}F')   
    return wind

def compute_wind_chill_celsius (temperature):
   
    wind = 35.74 + 0.6215*temperature - 35.75*math.pow(v, 0.16) + 0.4275*temperature*math.pow(v, 0.16)
    print(f'At temperature {temperature}F, and wind speed of {v} mph, the windchill is: {wind:.2f}F')   
    return wind

if f_or_c.lower() == 'f':
    for v in range(5, 65, 5):
        compute_wind_chill(t)
        
elif f_or_c.lower() == 'c':
    celsius = to_fahrenheit(t)
    for v in range(5, 65, 5):
        compute_wind_chill_celsius(celsius)
        
        
 