import requests

# openai = RemoteRunnable("http://localhost:8000/configure_json/")
# response = openai.invoke({"query":'Generate a game configuration with six defenses. Of these six defenses, two are mortars placed at the center and center-right position. There are two towers at top-right and top-left corners. Also, two cannons are at the bottom-right and bottom-left positions. There are twenty agents available to us. Of these twenty, ten are shooters, five are tanks, and five are helicopters. I want to deploy five shooters from the top-right corner and five from the bottom-right corner. I want to deploy five tanks from the center-right and five helicopters from the bottom-left position.'})
response = requests.post(
    "https://dlair.eng.utah.edu:8000/configure_json/invoke",
    json={'input': {"question":'Generate a game configuration with six defenses. Of these six defenses, two are mortars placed at the center and center-right position. There are two towers at top-right and top-left corners. Also, two cannons are at the bottom-right and bottom-left positions. There are twenty agents available to us. Of these twenty, ten are shooters, five are tanks, and five are helicopters. I want to deploy five shooters from the top-right corner and five from the bottom-right corner. I want to deploy five tanks from the center-right and five helicopters from the bottom-left position.'}}
)
print(response.json())
