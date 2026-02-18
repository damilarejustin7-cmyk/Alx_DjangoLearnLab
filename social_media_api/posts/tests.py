from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from posts.models import Post, Like
from accounts.models import CustomUser  # Adjust if using CustomUser

class LikeTests(APITestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(username='user1', password='pass')
        self.user2 = get_user_model().objects.create_user(username='user2', password='pass')
        self.post = Post.objects.create(user=self.user1, content='test')

    def test_like_post(self):
        self.client.force_authenticate(self.user2)
        response = self.client.post(f'/posts/{self.post.pk}/like/')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['liked'], True)
        self.assertEqual(Like.objects.count(), 1)

    def test_unlike_post(self):
        self.client.force_authenticate(self.user2)
        self.client.post(f'/posts/{self.post.pk}/like/')  # Like first
        response = self.client.post(f'/posts/{self.post.pk}/like/')  # Toggle off
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['liked'], False)
        self.assertEqual(Like.objects.count(), 0)

    def test_no_duplicate_likes(self):
        self.client.force_authenti
