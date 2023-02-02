from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/zipcode", methods=["GET"])
def get_zipcode():
    # state = request.args.get("state")
    # city = request.args.get("city")
    state = 'ca'
    city = 'fremont'
    if city:
        # make a request to a zip code API using the city name
        response = requests.get(f"http://api.zippopotam.us/us/{state}/{city}")
        if response.status_code == 200:
            data = response.json()
            zipcode = [place["post code"] for place in data["places"]]
            return {"zipcode": zipcode}
        else:
            return {"error": "City not found"}
    else:
        return {"error": "Please provide a city name"}

if __name__ == "__main__":
    app.run(debug=True, port=5001)