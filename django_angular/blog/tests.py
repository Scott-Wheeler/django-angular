from django.test import TestCase

from .models import Author, Blog, BlogEntry
from .views import (
    AuthorCreate, AuthorUpdate, AuthorDelete,
    BlogCreate, BlogUpdate, BlogDelete,
    BlogEntryCreate, BlogEntryUpdate, BlogEntryDelete,
    ContactView,
    IndexView,
    AuthorDetailView,
    BlogDetailView,
    BlogEntryDetailView
)

from datetime import timedelta
from django.utils import timezone
from django.urls import reverse

# Create your tests here.

## helper functions ##

def create_author(name):
    return Author.objects.create(name)

def create_blog(name, tagline):
    return Blog.objects.create(name=name, tagline=tagline)

def create_entry(blog, title, text, pub_date=None, days=None):
    if pub_date is None:
        if days is None:
            pub_date = timezone.now()
        else:
            pub_date = timezone.now() + timedelta(days=days)
    return BlogEntry.objects.create(blog=blog, title=title, text=text, pub_date=pub_date)



## Models ##

class AuthorModelTests(TestCase):
    ...

class BlogModelTests(TestCase):
    def test_get_blog_entries(self):
        test_blog = create_blog("First Test Blog", "This is the first Blog for use in tests")
        first_entry = create_entry(test_blog, "First Test BlogEntry", "This is the first BlogEntry for use in tests")
        second_entry = create_entry(test_blog, "Second Test BlogEntry", "This is the second BlogEntry for use in tests")
        third_entry = create_entry(test_blog, "Third Test BlogEntry", "This is the third BlogEntry for use in tests")
        
        entries = test_blog.get_blog_entries()
        self.assertIn(first_entry, entries)
        self.assertIn(second_entry, entries)
        self.assertIn(third_entry, entries)
        self.assertEqual(len(entries), 3)

    def test_get_published_entries(self):
        test_blog = create_blog("First Test Blog", "This is the first Blog for use in tests")
        first_entry = create_entry(test_blog, "First Test BlogEntry", "This is the first BlogEntry for use in tests", days=-3)
        second_entry = create_entry(test_blog, "Second Test BlogEntry", "This is the second BlogEntry for use in tests", days=5)
        third_entry = create_entry(test_blog, "Third Test BlogEntry", "This is the third BlogEntry for use in tests", days=2)

        entries = test_blog.get_published_entries()
        self.assertIn(first_entry, entries)
        self.assertNotIn(second_entry, entries)
        self.assertNotIn(third_entry, entries)
        self.assertEqual(len(entries), 1)
        
class BlogEntryModelTests(TestCase):
    ...



## Views ##

class AuthorCreateViewTests(TestCase):
    ...
class AuthorUpdateViewTests(TestCase):
    ...
class AuthorDeleteViewTests(TestCase):
    ...

class BlogCreateViewTests(TestCase):
    ...
class BlogUpdateViewTests(TestCase):
    ...
class BlogDeleteViewTests(TestCase):
    ...

class BlogEntryCreateViewTests(TestCase):
    ...
class BlogEntryUpdateViewTests(TestCase):
    ...
class BlogEntryDeleteViewTests(TestCase):
    ...

    
class ContactViewTests(TestCase):
    ...
    
class IndexViewTests(TestCase):
    def test_get_queryset_with_only_past_entries(self):
        """
        All Blogs that have BlogEntries published in the past should be shown
        """
        test_blog = create_blog("First Test Blog", "This is the first Blog for use in tests")
        first_entry = create_entry(test_blog, "First Test BlogEntry", "This is the first BlogEntry for use in tests", days=-1)
        second_entry = create_entry(test_blog, "Second Test BlogEntry", "This is the second BlogEntry for use in tests", days=-2)
        third_entry = create_entry(test_blog, "Third Test BlogEntry", "This is the third BlogEntry for use in tests", days=-3)
        
        second_test_blog = create_blog("Second Test Blog", "This is the second Blog for use in tests")
        second_blog_first_entry = create_entry(second_test_blog, "First Test BlogEntry of the Second Blog", "This is the fourth BlogEntry for use in tests", days=-4)
        second_blog_second_entry = create_entry(second_test_blog, "Second Test BlogEntry of the Second Blog", "This is the fifth BlogEntry for use in tests", days=-5)
        second_blog_third_entry = create_entry(second_test_blog, "Third Test BlogEntry of the Second Blog", "This is the sixth BlogEntry for use in tests", days=-6)

        response = self.client.get(reverse("blog:index"))
        self.assertContains(response, "First Test Blog")
        self.assertContains(response, "Second Test Blog")

    def test_get_queryset_with_only_future_entries(self):
        """
        No Blogs that have only future BlogEntries should be shown
        """
        test_blog = create_blog("First Test Blog", "This is the first Blog for use in tests")
        first_entry = create_entry(test_blog, "First Test BlogEntry", "This is the first BlogEntry for use in tests", days=1)
        second_entry = create_entry(test_blog, "Second Test BlogEntry", "This is the second BlogEntry for use in tests", days=2)
        third_entry = create_entry(test_blog, "Third Test BlogEntry", "This is the third BlogEntry for use in tests", days=3)
        
        second_test_blog = create_blog("Second Test Blog", "This is the second Blog for use in tests")
        second_blog_first_entry = create_entry(second_test_blog, "First Test BlogEntry of the Second Blog", "This is the fourth BlogEntry for use in tests", days=4)
        second_blog_second_entry = create_entry(second_test_blog, "Second Test BlogEntry of the Second Blog", "This is the fifth BlogEntry for use in tests", days=5)
        second_blog_third_entry = create_entry(second_test_blog, "Third Test BlogEntry of the Second Blog", "This is the sixth BlogEntry for use in tests", days=6)

        response = self.client.get(reverse("blog:index"))
        self.assertContains(response, "No blogs are available.")

    def test_get_queryset_with_past_and_future_entries(self):
        """
        Blogs that have some BlogEntries published in the past and some in the future should be shown
        Both first and second blogs should be shown
        """
        test_blog = create_blog("First Test Blog", "This is the first Blog for use in tests")
        first_entry = create_entry(test_blog, "First Test BlogEntry", "This is the first BlogEntry for use in tests", days=-1)
        second_entry = create_entry(test_blog, "Second Test BlogEntry", "This is the second BlogEntry for use in tests", days=2)
        third_entry = create_entry(test_blog, "Third Test BlogEntry", "This is the third BlogEntry for use in tests", days=-3)
        
        second_test_blog = create_blog("Second Test Blog", "This is the second Blog for use in tests")
        second_blog_first_entry = create_entry(second_test_blog, "First Test BlogEntry of the Second Blog", "This is the fourth BlogEntry for use in tests", days=4)
        second_blog_second_entry = create_entry(second_test_blog, "Second Test BlogEntry of the Second Blog", "This is the fifth BlogEntry for use in tests", days=-5)
        second_blog_third_entry = create_entry(second_test_blog, "Third Test BlogEntry of the Second Blog", "This is the sixth BlogEntry for use in tests", days=6)

        response = self.client.get(reverse("blog:index"))
        self.assertContains(response, "First Test Blog")
        self.assertContains(response, "Second Test Blog")

    def test_get_queryset_with_one_blog_all_past_and_one_blog_all_future_entries(self):
        """
        Blogs that have some BlogEntries published in the past and some in the future should be shown
        Only the first blog should be shown
        """
        test_blog = create_blog("First Test Blog", "This is the first Blog for use in tests")
        first_entry = create_entry(test_blog, "First Test BlogEntry", "This is the first BlogEntry for use in tests", days=-1)
        second_entry = create_entry(test_blog, "Second Test BlogEntry", "This is the second BlogEntry for use in tests", days=-2)
        third_entry = create_entry(test_blog, "Third Test BlogEntry", "This is the third BlogEntry for use in tests", days=-3)
        
        second_test_blog = create_blog("Second Test Blog", "This is the second Blog for use in tests")
        second_blog_first_entry = create_entry(second_test_blog, "First Test BlogEntry of the Second Blog", "This is the fourth BlogEntry for use in tests", days=4)
        second_blog_second_entry = create_entry(second_test_blog, "Second Test BlogEntry of the Second Blog", "This is the fifth BlogEntry for use in tests", days=5)
        second_blog_third_entry = create_entry(second_test_blog, "Third Test BlogEntry of the Second Blog", "This is the sixth BlogEntry for use in tests", days=6)

        response = self.client.get(reverse("blog:index"))
        self.assertContains(response, "First Test Blog")
        self.assertNotContains(response, "Second Test Blog")

    def test_get_queryset_ordering_past_and_future_entries(self):
        """
        Get all Blogs that have published (in the past) BlogEntry(ies)
        order the blogs by the most recently published entry
        """
        ...

class AuthorDetailViewTests(TestCase):
    ...

class BlogDetailViewTests(TestCase):
    def test_get_queryset_with_only_past_entries(self):
        """
        Blogs that have BlogEntries published in the past should be shown
        """
        ...
    def test_get_queryset_with_only_future_entries(self):
        """
        Blogs that have only future BlogEntries should not be shown
        """
        ...
    def test_get_queryset_with_past_and_future_entries(self):
        """
        Blogs that have some BlogEntries published in the past and some in the future should be shown,
        but the blog entries from the future should not be shown
        """
        ...

class BlogEntryDetailViewTests(TestCase):
    def test_get_queryset_with_only_past_entries(self):
        """
        BlogEntries published in the past should be shown
        """
        ...
    def test_get_queryset_with_only_future_entries(self):
        """
        BlogEntries published in the future should not be shown
        """
        ...




## Forms ##

class ContactForm(TestCase):
    ...

class BlogForm(TestCase):
    ...


class BlogEntryForm(TestCase):
    ...



