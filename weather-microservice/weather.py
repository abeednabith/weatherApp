from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/weather", methods=["GET"])
def get_weather():
    zipcode = request.args.get("zipcode")
    if zipcode:
        # make a request to a weather API using the zip code
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={zipcode},us&appid=2e1abf2d92294ee4d9726bded5f32d05")
        if response.status_code == 200:
            weather = response.json()["weather"][0]["description"]
            return {"weather": weather}
        else:
            return {"error": "Zip code not found"}
    else:
        return {"error": "Please provide a zip code"}

if __name__ == "__main__":
    app.run(debug=True, port=5002)