from django.shortcuts import render

def map(request):
    return render(request,'placeapp/map.html')
def admin1(request):    
    return render(request,'placeapp/admin.html')
def ece(request):    
    return render(request,'placeapp/ece.html')
def eee(request):    
    return render(request,'placeapp/eee.html')
def cse(request):    
    return render(request,'placeapp/cse.html')
def rb(request):    
    return render(request,'placeapp/rb.html')
def girls(request):    
    return render(request,'placeapp/g.html')
def boys(request):    
    return render(request,'placeapp/b.html')


