cities = {
    'santiago': {
        'country': 'chile',
        'population': 6310000,
        'nearby mountains': 'andes',
        },
    'aurora': {
        'country': 'united states',
        'population': 420000,
        'nearby mountains': 'pikes peak',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 123000,
        'nearby mountains': 'mt everest',
        }
    }
for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"It has a population of {population}.")
    print(f"The nearest mountains are {mountains.title()}.")

