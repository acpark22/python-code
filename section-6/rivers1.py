glossary = {
    'nile': 'egypt',
    'missouri': 'united states',
    'yellow river': 'china',
    }
for river, value in glossary.items():
    print(f"\nThe {river.title()} runs through {value.title()}.")

print(f"\nThe following rivers are:")
for river in glossary.keys():
    print(f"- {river.title()}")

print(f"\nThe following countries are:")
for value in glossary.values():
    print(f"- {value.title()}")

