#nesting 
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting in Dictionary, passing a list as value  
Travel_log = {
    "France": ["Paris","lille","Dijon"],
    "Germany":["Berlin","Hamburg"]
}

# passing dictionary as value 
Travel_l = {
    "France": {
        "cities_travel":["Paris","lille","Dijon"],
        "total_visit":12
        }
}
print(capitals)
print(Travel_log)
print(Travel_l)

# Nesting dictionary in list 
logs = [
    {
        "country":"France",
        "cities_visted":["Paris","Lille"],
        "Total_visit":8
    },
    {
        "country":"Germany",
        "citites_visited":["Berlin","Hamburg"],
        "total_visit":4

    }
]

print(logs[0])

