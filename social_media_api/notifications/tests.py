from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from notifications.models import Notification
from posts.models import Post

class NotificationTests(APITestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(username='user1', password='pass')
        self.user2 = get_user_model().objects.create_user(username='user2', password='pass')
        self.post = Post.objects.create(user=self.user1, content='test')

    def test_notification_on_like(self):
        self.client.force_authenticate(self.user2)
        self.client.post(f'/posts/{self.post.pk}/like/')
        self.assertEqual(Notification.objects.count(), 1)
        notif = Notification.objects.first()
        self.assertEqual(notif.recipient, self.user1)
        self.assertEqual(notif.actor, self.user2)
        self.assertEqual(notif.verb, 'liked your post')
        self.assertTrue(notif.unread)

    def test_list_notifications(self):
        self.client.force_authenticate(self.user2)
        self.client.post(f'/posts/{self.post.pk}/like/')  # Creates notif for user1
        self.client.force_authenticate(self.user1)
        response = self.client.get('/notifications/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['unread_count'], 1)

