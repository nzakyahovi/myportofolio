from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Experience,Education


def show_main(request):
    context = {
        "name": "Nurul Zakyah Ovi",
        "npm": "2506617582",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Nurul Zakyah Ovi",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Nurul Zakyah Ovi",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)