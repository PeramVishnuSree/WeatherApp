from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']

        api_request = requests.get(
            'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zipcode + '&distance=5&API_KEY=291964E5-9925-4661-9A28-D8AA8C1DEC12')

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Airquality is considered satisfactory, and airpollution poses little to no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups (USG)":
            category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children area at a greater risk from exposure to ozone, whereas persons with heart and lung disease are at a greater risk from the presence of particles in the air."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups mayexperience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health Alert: everyone may experience more serious health effects. pro - tip: Runwhile you still can."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500) Run for your life"
            category_color = "hazardous"

        return render(request, 'home.html',{'api': api, 'category_description': category_description, 'category_color': category_color})

    else :

        api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=98087&distance=5&API_KEY=291964E5-9925-4661-9A28-D8AA8C1DEC12')

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Airquality is considered satisfactory, and airpollution poses little to no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups (USG)":
            category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children area at a greater risk from exposure to ozone, whereas persons with heart and lung disease are at a greater risk from the presence of particles in the air."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups mayexperience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health Alert: everyone may experience more serious health effects. pro - tip: Runwhile you still can."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500) Run for your life"
            category_color = "hazardous"


        return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})

def about(request):

    return render(request, 'about.html', {})
