import os
import django
import random
from faker import Faker
from faker.providers import BaseProvider

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")  # Adjust if necessary
django.setup()

# Create two Faker instances: one for English and one for Arabic (SA)
english_fake = Faker('en_US')
arabic_fake = Faker('ar_SA')

# Custom Arabic Provider for ar_SA locale with RTL marker prefix
class ArabicProvider(BaseProvider):
    ARABIC_SENTENCES = [
        'مكرس للفن والثقافة.',
        'انضم إلينا لاستكشاف الإبداع.',
        'تجربة مزيج من التراث والفن الحديث.',
        'اكتشف التعبيرات الفنية الأصيلة.',
        'حيث يلتقي الشغف بالإبداع.',
        'منصة للمواهب الناشئة.',
        'إلهام الفن بلمسة تقليدية.',
        'احتفال بروح الفن والثقافة.'
    ]
    ARABIC_CATEGORY_NAMES = ["الخياطة", "النحت", "الرسم", "الخط", "التصوير", "التطريز", "الفخار", "الموسيقى", "الأدب", "العمارة"]

    def arabic_sentence(self):
        # Prefix with RTL marker to ensure proper direction
        return "\u200F" + random.choice(self.ARABIC_SENTENCES)
    
    def arabic_category(self):
        return "\u200F" + random.choice(self.ARABIC_CATEGORY_NAMES)

arabic_fake.add_provider(ArabicProvider)

# Import models
from accounts.models import CustomUser
from communities.models import Community
from clubs.models import Club
from category.models import Category
from products.models import Product

# Create 20 fake users
users = []
for _ in range(20):
    username = english_fake.unique.first_name() + str(random.randint(1, 1000))
    email = english_fake.email()
    full_name = "\u200F" + arabic_fake.name()  # Full name in Arabic with RTL marker
    # For specialization, use an Arabic word from the provider (or simply use arabic_fake.word())
    specialization = "\u200F" + arabic_fake.word()
    user = CustomUser.objects.create_user(
        username=username,
        email=email,
        password="test12345",
        full_name=full_name,
        specialization=specialization
    )
    users.append(user)

# Create 10 fake communities and assign random members
communities = []
for _ in range(10):
    name = "\u200F" + arabic_fake.sentence(nb_words=3)
    description = arabic_fake.arabic_sentence()
    community = Community.objects.create(
        name=name,
        description=description,
        image="default.jpeg"
    )
    num_members = random.randint(1, len(users))
    for member in random.sample(users, num_members):
        community.members.add(member)
    communities.append(community)

# Create 10 fake clubs and assign random members
clubs = []
for _ in range(10):
    name = "\u200F" + arabic_fake.sentence(nb_words=3)
    description = arabic_fake.arabic_sentence()
    club = Club.objects.create(
        name=name,
        description=description,
        image="default.jpeg",
        icon="default.jpeg"
    )
    num_members = random.randint(1, len(users))
    for member in random.sample(users, num_members):
        club.members.add(member)
    clubs.append(club)

# Create 10 fake categories using the fixed unique Arabic category names
categories = []
for cat_name in ArabicProvider.ARABIC_CATEGORY_NAMES:
    category = Category.objects.create(
        name="\u200F" + cat_name,
        description="\u200F" + arabic_fake.text(max_nb_chars=100)
    )
    categories.append(category)

# Create 20 fake products assigned to random categories and with random likes
products = []
for _ in range(20):
    category = random.choice(categories)
    name = "\u200F" + arabic_fake.sentence(nb_words=4)
    description = "\u200F" + arabic_fake.text(max_nb_chars=200)
    price = arabic_fake.pydecimal(left_digits=3, right_digits=2, positive=True)
    product = Product.objects.create(
        name=name,
        description=description,
        price=price,
        image="default.jpeg",
        category=category
    )
    num_likes = random.randint(0, len(users))
    for member in random.sample(users, num_likes):
        product.likes.add(member)
    products.append(product)

# Randomly assign some purchased products to users
for user in users:
    num_purchases = random.randint(0, len(products))
    purchased = random.sample(products, num_purchases)
    for product in purchased:
        user.purchased_products.add(product)

print("Fake data generation completed.")
