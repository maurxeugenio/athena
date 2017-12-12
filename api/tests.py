from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from core.models import Scheduling


class ViewTestCase(TestCase):
    def setUp(self):
        """ Creates the test client and its variables """
        self.client = APIClient()
        self.scheduling_data = {
                                'patient': 'Odin',
                                'procedure': 'Avalição do globo ocular',
                                'date': '0803-12-25',
                                'start_time': '17:50:00',
                                'end_time': "18:50:00",
                                }

        self.response = self.client.post(reverse('create'), self.scheduling_data, format='json')

    def test_api_can_create_a_scheduling(self):
        """ Verify that you were able to create the element """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_scheduling(self):
        """ Make sure you can pick up an element """
        scheduling = Scheduling.objects.get(patient='Odin')
        response = self.client.get(reverse('details', kwargs={'pk': scheduling.pk}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_scheduling(self):
        """ Attempts to delete an element """
        scheduling = Scheduling.objects.get(patient='Odin')
        response = self.client.delete(reverse('details', kwargs={'pk': scheduling.pk}), format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_can_get_all_scheduling(self):
        """Try to get all the elements of schedules"""

        response = self.client.get(reverse('list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response, not None)
