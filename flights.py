from datetime import datetime
import pprint


# Convert time to AM/PM
def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('flights_data.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

    print('Original data')
    pprint.pprint(flights)
    print()

# Coverting time to AM/PM and destinations to title formart
fts = {convert2ampm(k): v.title() for k, v in flights.items()}

# Finally, sorting it based on destination
when = {dest: [k for k, v in fts.items() if v == dest]
        for dest in set(fts.values())}

print('Sorted data')
pprint.pprint(when)
print()
