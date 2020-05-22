def city_country(city_name, country_name):
    """Display the city-country pairs."""
    full_name = f"{city_name}, {country_name}"
    return full_name.title()

geography = city_country('denver', 'united states')
print(geography)

geography = city_country('seoul', 'korea')
print(geography)

geography = city_country('paris', 'france')
print(geography)

