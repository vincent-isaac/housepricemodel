from django.shortcuts import render

# Create your views here.

def HouseModelTraining(request):
    context={}

    return render(request, 'housepriceprediction/HouseModelTraining.html', context) 

def HouseModelPrediction(request):
    context={}
    
    return render(request, 'housepriceprediction/HouseModelPrediction.html', context)     
