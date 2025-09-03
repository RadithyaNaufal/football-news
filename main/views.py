from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406365225',
        'name': 'Radithya Naufal Mulia',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)