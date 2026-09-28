from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateTimeInput
from main.models import Project, Education, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "tech_stack", "project_url", "project_image_url"]
        
        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/...",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/...",
                }
            ),
        }


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'field_of_study', 'start_year', 'end_year', 'education_image_url']

        labels = {
            'institution': 'Nama Institusi',
            'degree': 'Jenjang Pendidikan',
            'field_of_study': 'Jurusan / Bidang Studi',
            'start_year': 'Waktu Mulai',
            'end_year': 'Waktu Selesai',
            'education_image_url': 'URL Logo/Gambar Institusi',
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "Contoh: Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "degree": Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "field_of_study": TextInput(
                attrs={
                    "placeholder": "Contoh: Sistem Informasi",
                    "maxlength": 255,
                }
            ),
            "start_year": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
            "end_year": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
            "education_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/...",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "description", 'start_year', 'end_year', "experience_url", "experience_image_url"]
        
        labels = {
            "title": "Nama Experience",
            "description": "Deskripsi experience",
            'start_year': 'Waktu Mulai',
            'end_year': 'Waktu Selesai',
            "experience_url": "URL experience",
            "experience_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "start_year": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
            "end_year": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),

            "experience_url": URLInput(
                attrs={
                    "placeholder": "https://experience/...",
                }
            ),
            "experience_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/...",
                }
            ),
        }
        
       