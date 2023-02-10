from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route("/zipcode", methods=["GET"])
def get_zipcode():
    state = request.args.get("state")
    city = request.args.get("city")
    if city:
        # make a request to a zip code API using the city name
        response = requests.get(f"http://api.zippopotam.us/us/{state}/{city}")
        if response.status_code == 200:
            data = response.json()
            zipcode = [place["post code"] for place in data["places"]]
            # return {"zipcode": zipcode}
            response = requests.get(f"http://127.0.0.1:5002/weather?zipcode={zipcode[0]}")
            return json.dumps(response.json())
        else:
            return {"error": "City not found"}
    else:
        return {"error": "Please provide a city name"}

if __name__ == "__main__":
    app.run(debug=True, port=5001)