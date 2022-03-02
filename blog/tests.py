from django.test import TestCase
from django.contrib.auth.models import User 
from blog.models import Post, Category

class TestCreatePost(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='Java')
        test_user1 = User.objects.create_user(username='user1', password='pass')
        test_post = Post.objects.create(category_id=1, title='Post test case', excert='Post excert', content='Post Content', slug='Post Title', author_id=1, status='Published')

    def testBlogContent(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excert = f'{post.excert}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'

        self.assertEqual(author, 'user1')
        self.assertEqual(title, 'Post test case')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'Published')
        self.assertEqual(str(post), 'Post test case')
        self.assertEqual(str(cat), 'Java')
        