from django.test import TestCase
from django.urls import reverse, resolve

from .views import agency, banana, fast, funflat, stand

# Create your tests here.

class DossierTests(TestCase):
    def test_agency_view_status_code(self):
        url = reverse('agency')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_agency_url_resolves_agency_view(self):
        view = resolve('/dossier/agency')
        self.assertEquals(view.func, agency )


    def test_banana_view_status_code(self):
        url = reverse('banana')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_banana_url_resolves_banana_view(self):
        view = resolve('/dossier/banana')
        self.assertEquals(view.func, banana )


    def test_fast_view_status_code(self):
        url = reverse('fast')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_fast_url_resolves_fast_view(self):
        view = resolve('/dossier/fast')
        self.assertEquals(view.func, fast )


    def test_funflat_view_status_code(self):
        url = reverse('funflat')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_funflat_url_resolves_funflat_view(self):
        view = resolve('/dossier/funflat')
        self.assertEquals(view.func, funflat )


    def test_stand_view_status_code(self):
        url = reverse('stand')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_stand_url_resolves_stand_view(self):
        view = resolve('/dossier/stand')
        self.assertEquals(view.func, stand )