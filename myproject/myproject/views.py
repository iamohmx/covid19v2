from django.shortcuts import render
import requests


def index(request):
    res = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all").json()
    # res = requests.get("https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases2_v1/FeatureServer/2/query?where=1%3D1&outFields=Long_,Confirmed,Country_Region,Deaths&outSR=4326&f=json").json()
    return render(request, 'index.html',{"res":res})

def about(request):
    return render(request, 'about.html')