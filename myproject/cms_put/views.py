from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from models import Table
from django.template.loader import get_template
from django.template import Context

# Create your views here.

@csrf_exempt
def show_css (request,recurso):
    
    if request.method == 'GET':
       
        try:
            record = Table.objects.get(resource=recurso)
            return HttpResponse(record.name, content_type="text/css")
        except Table.DoesNotExist:
            return HttpResponseNotFound('Page not found:')
        
    elif request.method == 'PUT':
        record = Table(resource= recurso,name =request.body)  
        record.save()
        return HttpResponse('<h1>Actualizando.../h1>'+ request.body)

def show_html(request,recurso):
     
      if request.method == 'PUT':
        pos_in= request.body.find("<body>")
        pos_fin= request.body.find("</body>")
        record = Table(resource= recurso,name =request.body[pos_in+7:pos_fin]) 
        record.save()
        return HttpResponse('<h1>Actualizando.../h1>'+ request.body)
      elif request.method == 'GET':
       
        try:
            record = Table.objects.get(resource=recurso)
            
            template = get_template("index.html")
            return HttpResponse(template.render(Context({'body': record.name})))
        except Table.DoesNotExist:
            return HttpResponseNotFound('Page not found:')
        
