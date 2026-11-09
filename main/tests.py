from django.test import TestCase

from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

        data = self.client.get(reverse("main:get_experience_json")).json()
        self.assertEqual(data[0]["fields"]["title"], self.experience.title)
        self.assertEqual(data[0]["fields"]["description"], self.experience.description)
        self.assertTrue(data[0]["fields"]["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada experience yang ditambahkan atau ditemukan.")
        self.assertEqual(self.client.get(reverse("main:get_experience_json")).json(), [])   

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

class EducationViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    # 1. URL dapat diakses dan menggunakan template yang tepat
    def test_show_education_url_and_template(self):
        response = self.client.get(reverse('main:show_education'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'education.html')

    # 2. Halaman menampilkan pesan kondisi kosong ketika belum ada data
    def test_show_education_empty_condition(self):
        response = self.client.get(reverse('main:show_education'))
        self.assertContains(response, 'Belum ada riwayat pendidikan yang ditambahkan atau ditemukan.')
        self.assertEqual(self.client.get(reverse('api:education-list')).json(), [])

    # 3. Data model muncul di halaman HTML ketika ada data
 def test_show_education_with_data(self):
        Education.objects.create(
            institution="Universitas Indonesia",
            degree="bachelor",
            field_of_study="Sistem Informasi"
        )
        response = self.client.get(reverse('api:education-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["institution"], "Universitas Indonesia")
        self.assertEqual(response.json()[0]["field_of_study"], "Sistem Informasi")