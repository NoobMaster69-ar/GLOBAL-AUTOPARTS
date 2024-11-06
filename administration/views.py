from django.http import JsonResponse
from django.shortcuts import render
from .functions import load_data, delete_data
from .models import Supplier, Items, Parameters

def login(request):
    return render(request, 'pages/login.html')

def panel(request):
    return render(request, 'pages/panel.html')

def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        item = Items.objects.filter(id=search).first()
        revenue = Parameters.objects.get(name="revenue").value
        if item:
            data = {
                'description': item.description,
                'origin': item.origin,
                'price': round(item.price * (1 + revenue / 100)),
                'supplier': item.supplier.name,
                'image': item.image,
            }
            return JsonResponse({'status': 'success', 'data': data})

    search = request.GET.get('search')

    if search:
        items_data = []
        items = Items.objects.filter(description__icontains=search)
        for item in items:
            items_data.append({
                'id': item.id,
                'description': item.description
        })
        
        return JsonResponse({'status': 'success', 'data': items_data})

def administration(request):
    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES['file']
        supplier_id = request.POST['supplier']

        response = load_data(uploaded_file, supplier_id)
        return JsonResponse({'status': response['status'], 'message': response['message']})
    
    suppliers = Supplier.objects.all()
    items = Items.objects.count()
    return render(request, 'pages/administration.html', {'suppliers': suppliers, 'items': items})

def erase(request):
    response = delete_data()
    return JsonResponse({'status': response['status'], 'message': response['message']})