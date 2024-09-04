from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306174135',
        'name': 'Andhika Nayaka Arya Wibowo',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)
