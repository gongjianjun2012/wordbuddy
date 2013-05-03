from django.shortcuts import render_to_response

def Demo_index(request):
    return render_to_response('home/Demo_index.html')
