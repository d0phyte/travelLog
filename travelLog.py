
country = input("Which country did you visit now? ")
visits = int(input("How many times have you been? "))
listOfCities = (input("What city did you visit? "))



travel_log = [
{
    "country": "france", 
    "visits":12,
    "cities":["Paris","Lille","Dijon"]
},
{
    "country":"Germany",
    "visits":5,
    "cities":["Berlin","Hamburg","Stuttgart"]
},
]


def add_new_country(countryName,timesVisited,citiesVisited):

    new_country = {}
    new_country["country"] = countryName
    new_country["visits"] = timesVisited
    new_country["cities"] = citiesVisited
    travel_log.append(new_country)



add_new_country(country,visits,listOfCities)

print(travel_log)
    

