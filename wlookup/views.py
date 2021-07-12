from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=7409B194-A8B9-42F8-ACAB-5A01514FCC26")
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			AQI_category_description = "A rating of GOOD means that the air quality is satisfactory, and air pollution poses little or no risk. Air Quality Index values between 0-50 are considered GOOD."
			AQI_category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			AQI_category_description = "A rating of MODERATE means that the air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution. Air Quality Index values between 51-100 are considered MODERATE."
			AQI_category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			AQI_category_description = "A rating of UNHEALTHY FOR SENSITIVE GROUPS means that members of sensitive groups may experience health effects. The general public is less likely to be affected. Air Quality Index values between 101-150 are considered UNHEALTHY FOR SENSITIVE GROUPS."
			AQI_category_color = "USG"
		elif api[0]['Category']['Name'] == "Unhealthy":
			AQI_category_description = "A rating of UNHEALTHY means that some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects. Air Quality Index values between 151-200 are considered UNHEALTHY."
			AQI_category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			AQI_category_description = "A rating of VERY UNHEALTHY means that there is a health alert. The risk of health effects is increased for everyone. Air Quality Index values between 201-300 are considered VERY UNHEALTHY."
			AQI_category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			AQI_category_description = "A rating of HAZARDOUS means that there are health warning emergency conditions. Everyone is more likely to be affected. Air Quality Index values of 301 and higher are considered HAZARDOUS."
			AQI_category_color = "hazardous"




		return render(request, 'home.html', {'api': api, 
											 'AQI_category_description': AQI_category_description,
											 'AQI_category_color': AQI_category_color
											})


	else:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=01810&distance=5&API_KEY=7409B194-A8B9-42F8-ACAB-5A01514FCC26")
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			AQI_category_description = "A rating of GOOD means that the air quality is satisfactory, and air pollution poses little or no risk. Air Quality Index values between 0-50 are considered GOOD."
			AQI_category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			AQI_category_description = "A rating of MODERATE means that the air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution. Air Quality Index values between 51-100 are considered MODERATE."
			AQI_category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			AQI_category_description = "A rating of UNHEALTHY FOR SENSITIVE GROUPS means that members of sensitive groups may experience health effects. The general public is less likely to be affected. Air Quality Index values between 101-150 are considered UNHEALTHY FOR SENSITIVE GROUPS."
			AQI_category_color = "USG"
		elif api[0]['Category']['Name'] == "Unhealthy":
			AQI_category_description = "A rating of UNHEALTHY means that some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects. Air Quality Index values between 151-200 are considered UNHEALTHY."
			AQI_category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			AQI_category_description = "A rating of VERY UNHEALTHY means that there is a health alert. The risk of health effects is increased for everyone. Air Quality Index values between 201-300 are considered VERY UNHEALTHY."
			AQI_category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			AQI_category_description = "A rating of HAZARDOUS means that there are health warning emergency conditions. Everyone is more likely to be affected. Air Quality Index values of 301 and higher are considered HAZARDOUS."
			AQI_category_color = "hazardous"




		return render(request, 'home.html', {'api': api, 
											 'AQI_category_description': AQI_category_description,
											 'AQI_category_color': AQI_category_color
											})

def about(request):
	return render(request, 'about.html', {})