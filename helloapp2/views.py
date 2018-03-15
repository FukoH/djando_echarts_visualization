from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
def hello(request):
    return render(request,"echarts.html")

def face(request):
    return render(request,"exercise.html")

def face_data(request):
    df = pd.read_csv('static/my_app/face.csv',encoding='gbk')
    json = df.to_json(force_ascii=False)
    # di = df.to_dict()
    #json = json.decode('gbk').encode('utf-8')
    return HttpResponse(json)
