import http.client

conn = http.client.HTTPSConnection("app.nocodb.com")

headers = { 'xc-token': "-0Czyt0G8ZMbZC_peal62M7xR1kHzCyXKq35mKn8" }

conn.request("GET", "/api/v2/tables/m40rl03rfafbptv/records?offset=0&limit=25&where=&viewId=vwv0pv7b7noy9duc", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))