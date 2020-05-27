def make_car(manu, make, **car_info):
    """Build a dict about everything we know about a car."""
    car_info['manufacturer'] = manu
    car_info['model_name'] = make
    return car_info

car = make_car('honda', 'accord', 
        color = 'silver',
        moon_roof = True)
print(car)

