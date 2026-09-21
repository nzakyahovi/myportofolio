from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from main.models import Experience, Education, Project
from .forms import ProjectForm, EducationForm


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


# Education

def show_education(request):
    json_response = get_education_json(request)
    Education = serializers.deserialize(
           "json",
        json_response.content.decode("utf-8"),
       )
    Education = [edu.object for edu in Education]
    
    context = {
        "name": "Nurul Zakyah Ovi",
        "education_list": Education,
    }
    return render(request, "education.html", context)

def create_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data pendidikan berhasil ditambahkan!")
            return redirect('main:show_education')  
    else:
        form = EducationForm()  
    context = {'form': form}
    return render(request, 'education_form.html', context)


def edit_education(request, id):
    education = get_object_or_404(Education, pk=id)
    form = EducationForm(request.POST or None, instance=education)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Data pendidikan berhasil diperbarui!")
            return redirect('main:show_education')
    context = {'form': form, 'education': education}
    return render(request, 'education_form.html', context)


def delete_education(request, id):
    education = get_object_or_404(Education, pk=id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Data pendidikan berhasil dihapus!")
        return redirect("main:show_education")
    return redirect("main:show_education")


 #Project

def show_projects(request):
    json_response = get_projects_json(request)
    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Nurul Zakyah Ovi",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")
    return redirect("main:show_projects")


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')  
    else:
        form = ProjectForm()  
    context = {'form': form}
    return render(request, 'project_form.html', context)


# DATA DELIVERY VIEWS

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)
    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def show_json(request):
    data = Project.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml(request):
    data = Project.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_xml_by_id(request, id):
    data = Project.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Project.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def get_education_json(request):
    data = Education.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
