from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Menu_Item
from .forms import Menu_ItemForm

class MenuTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.menu_item = Menu_Item.objects.create(name="Vegan Burger", description="Delicious burger", price=10.99, category="Burgers")

    def test_menu_item_creation(self):
        menu_item = self.menu_item
        self.assertEqual(str(menu_item), "Vegan Burger - Delicious burger - 10.99")

    def test_menu_view(self):
        response = self.client.get(reverse('menu:menu_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Vegan Burger")
        self.assertTemplateUsed(response, 'menu.html')

    def test_add_menu_item(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse('menu:add_menu_item'), data={
            'name': 'Fries',
            'description': 'Crispy fries',
            'price': 5.99,
            'category': 'Sides',
            'item_image': None,
        })
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Menu_Item.objects.count(), 2)


class MenuFormTests(TestCase):
    def test_menu_item_form_valid(self):
        form = Menu_ItemForm(data={
            'name': 'Vegan Burger',
            'description': 'Delicious burger',
            'price': 10.99,
            'category': 'Burgers',
            'item_image': None,
        })
        self.assertTrue(form.is_valid())

    def test_menu_item_form_invalid(self):
        form = Menu_ItemForm(data={}) 
        self.assertFalse(form.is_valid())


