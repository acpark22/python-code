def describe_city(city_name, country_name='Korea'):
    """Display the city and its country."""
    print(f"\n{city_name.title()} is in {country_name.title()}.")

describe_city('seoul')
describe_city('busan')
describe_city('waco', 'united states')

# write a func called 'describe_city' that accepts the name of a city and its country. The func should print a simple sentence, Give the parameter for the country a default value. Call your func for 3 different cities, at least one of which is not in the default country.

