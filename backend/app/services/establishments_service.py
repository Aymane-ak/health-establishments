import requests


def fetch_establishments() : 
    url                    = "https://jsonplaceholder.typicode.com/users"

    response               = requests.get(url)
    data                   = response.json()
    data_customized  = [{
        "id"               : user["id"],
        "name"             : user["name"],
        "username"         : user["username"],
        "street"           : user["address"]["street"],
        "zipcode"          : user["address"]["zipcode"],
        "company"          : user["company"]["name"]
    }
        for user in data 
    ]
    return   data_customized

    # [ expression for item in iterable if condition ]
    # [ RESULTAT  for element in liste  if condition ]
    # data.map(user => ({
    #   name: user.name,
    #   company_name: user.company.name
    # }))
