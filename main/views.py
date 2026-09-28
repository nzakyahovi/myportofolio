import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied 

from main.models import Experience, Education, Project
from .forms import ProjectForm, EducationForm, ExperienceForm


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Nurul Zakyah Ovi",
        "npm": "2506617582",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),   
        "last_login": last_login,   
    }
    return render(request, "index.html", context)


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Ovi",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Ovi",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


# PROJECT VIEWS

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


@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")
   
    context = {
        "name": "Nurul Zakyah Ovi",
        "form": form,
    }
    return render(request, 'project_form.html', context)


@login_required(login_url="/login/")
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")
    return redirect("main:show_projects")


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)
    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(projects_json, content_type="application/json")


@login_required(login_url="/login/")
def toggle_star_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")


# EXPERIENCE VIEWS

def show_experience(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [exp.object for exp in experiences]
    
    context = {
        "name": "Nurul Zakyah Ovi",
        "experience_list": experiences,
    }
    return render(request, "experience.html", context)


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ExperienceForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Data pengalaman berhasil ditambahkan!")
            return redirect('main:show_experience')  
    context = {'form': form}
    return render(request, 'experience_form.html', context)


@login_required(login_url="/login/")
def edit_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Data pengalaman berhasil diperbarui!")
            return redirect('main:show_experience')
    context = {'form': form, 'experience': experience}
    return render(request, 'experience_form.html', context)


@login_required(login_url="/login/")
def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Data pengalaman berhasil dihapus!")
        return redirect("main:show_experience")
    return redirect("main:show_experience")


def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()
    if title_query:
        experience = experience.filter(title__icontains=title_query)
    experience_json = serializers.serialize("json", experience, use_natural_foreign_keys=True)
    return HttpResponse(experience_json, content_type="application/json")


@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")


# EDUCATION VIEWS

def show_education(request):
    json_response = get_education_json(request)
    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [edu.object for edu in educations]
    query = request.GET.get("query", "").strip()
    
    context = {
        "name": "Nurul Zakyah Ovi",
        "education_list": educations,
        "query": query,
    }
    return render(request, "education.html", context)


@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = EducationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Data pendidikan berhasil ditambahkan!")
            return redirect('main:show_education')  
    context = {'form': form}
    return render(request, 'education_form.html', context)


@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
def delete_education(request, id):
    education = get_object_or_404(Education, pk=id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Data pendidikan berhasil dihapus!")
        return redirect("main:show_education")
    return redirect("main:show_education")


def get_education_json(request):
    query = request.GET.get("query", "").strip()
    education = Education.objects.all()
    if query:
        education = education.filter(institution__icontains=query)
    education_json = serializers.serialize("json", education, use_natural_foreign_keys=True)
    return HttpResponse(education_json, content_type="application/json")


@login_required(login_url="/login/")
def toggle_star_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        if request.user in education.starred_by.all():
            education.starred_by.remove(request.user)
        else:
            education.starred_by.add(request.user)

    return redirect("main:show_education")


# DATA DELIVERY VIEWS

def show_json(request):
    data = Project.objects.all()
    return HttpResponse(serializers.serialize("json", data, use_natural_foreign_keys=True), content_type="application/json")


def show_xml(request):
    data = Project.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_xml_by_id(request, id):
    data = Project.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Project.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data, use_natural_foreign_keys=True), content_type="application/json")