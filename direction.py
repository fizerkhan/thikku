import requests
from stripper import strip_tags

def getDirection(origin, destination):
  payload = {'origin': origin, 'destination': destination}
  response = requests.get("http://maps.googleapis.com/maps/api/directions/json", params=payload)
  jsonResponse = response.json()
  if len(jsonResponse["routes"]) == 0:
    raise Exception('Unable to fetch from Google map!')
    return

  route = jsonResponse["routes"][0]
  legRoute = route["legs"][0]
  directionStr = "From: "+ origin + "\n"
  directionStr += "To: "+ destination + "\n"
  directionStr += "Distance: " + str(legRoute["distance"]["text"]) + "\n"
  directionStr += "Direction: \n"
  steps = legRoute["steps"]
  for idx, step in enumerate(steps):
    directionStr += str(idx + 1) + ". " + strip_tags(step["html_instructions"]) + "\n"

  return directionStr
