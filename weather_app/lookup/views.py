from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    # api at 92606 for 10 mi:
    # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=92606&distance=10&API_KEY=5E2F932C-CD4B-410E-AAA2-2CF2226BFAB9
    
    
    
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        try:
            api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=10&API_KEY=5E2F932C-CD4B-410E-AAA2-2CF2226BFAB9")
        except Exception as e:
            api = "Error..."
            category_description = "Invalid zipcode. No data found, or website is down."
            category_color = "errorcode"
            return render(request, 'homepage.html', {'api': api, 'category_description': category_description, 'category_color': category_color})

    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=92606&distance=10&API_KEY=5E2F932C-CD4B-410E-AAA2-2CF2226BFAB9")
        
    try:
        api = json.loads(api_request.content) # load content from var into json var
        
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little to no risk."
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health alert: The risk of health effects is increased for everyone."
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
        
        if api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_color = "veryunhealthy"
        else:
            category_color = api[0]['Category']['Name'].lower()
        
    except Exception as e:
        api = "Error..."
        category_description = "Invalid zipcode. No data found, or website is down."
        category_color = "errorcode"
    


    return render(request, 'homepage.html', {'api': api, 'category_description': category_description, 'category_color': category_color})

def about(request):
    return render(request, 'about.html', {})
