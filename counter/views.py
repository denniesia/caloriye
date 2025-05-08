from django.shortcuts import render
import requests

#3Fxq7nbiEcYpzkcqDHk9xVahhNugtSaeZkFNZxyq
# Create your views here.
def home(request):
    query = '1lb brisket and fries'
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': '/jzR+uMHkxAJ4Fh4Wb1yaQ==rokA0t7kn3n6jeeh'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

    return render(request, 'home.html')