from django.shortcuts import render

# Create your views here.
def msd(reqest):
    return render(reqest,'msd.html')