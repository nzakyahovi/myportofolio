from django.urls import path
from main.views import (
    create_project, delete_project, get_projects_json,
    show_experience, show_education, show_main, show_projects,
    create_education, edit_education, get_education_json, delete_education
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),

    # Education
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("education/<uuid:id>/edit/", edit_education, name="edit_education"),
    path("education/<uuid:id>/delete/", delete_education, name="delete_education"),
    path("api/education/", get_education_json, name="get_education_json"),

    path("experience/", show_experience, name="show_experience"),
]