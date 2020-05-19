favorite_places = {
    'andy': ['gym', 'mountains', 'mall'],
    'brady': ['disney land', 'super bowk'],
    'peyton': ['farms', 'aspen', 'mexico']
    }
for name, places in favorite_places.items():
    print(f"\nThese are {name.title()}'s favorite places:")
    for place in places:
        print(f"- {place.title()}")

