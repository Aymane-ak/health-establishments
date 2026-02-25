import requests

def fetch_establishments() : 
    url                    = "https://jsonplaceholder.typicode.com/users"

    response               = requests.get(url)
    data                   = response.json()
    data_customized  = [{
        "id"               : user.get("id"),
        "name"             : user.get("name","UNKNOWN"),
        "username"         : user.get("username","UNKNOWN"),
        "street"           : user.get("address",{}).get("street","UNKNOWN"),
        "zipcode"          : user.get("address",{}).get("zipcode","UNKNOWN"),
        "company"          : user.get("company",{}).get("name","UNKNOWN")
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
