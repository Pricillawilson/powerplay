import http.client

conn = http.client.HTTPSConnection("airport-info.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "airport-info.p.rapidapi.com",
    'x-rapidapi-key': "c514ef4eb9mshddc3d42e65b88c8p1b2e4ejsnd027bcf78714"
    }

conn.request("GET", "/airport?iata=${iataCode}", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))