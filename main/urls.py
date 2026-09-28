from django.urls import path
from main.views import (
    create_project, delete_project, get_projects_json,
    show_experience, show_education, show_main, show_projects,
    create_education, edit_education, get_education_json, delete_education,
    register,  login_user,logout_user,create_experience,edit_experience,delete_experience, 
    get_experience_json,toggle_star_experience,toggle_star_education,toggle_star_project
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    # Project
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("projects/<uuid:project_id>/star/", toggle_star_project,name="toggle_star_project",),
    # Education
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("education/<uuid:id>/edit/", edit_education, name="edit_education"),
    path("education/<uuid:id>/delete/", delete_education, name="delete_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/star/", toggle_star_education,name="toggle_star_education",),
    # Experience
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/star/", toggle_star_experience ,name="toggle_star_experience",),

    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),



    
]
