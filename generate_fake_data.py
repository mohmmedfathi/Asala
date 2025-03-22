import os
import django
import random
from faker import Faker
from faker.providers import BaseProvider

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from accounts.models import CustomUser
from communities.models import Community
from clubs.models import Club
from products.models import Product

class ArabicProvider(BaseProvider):
    ARABIC_NAMES = [
        'Mohammed', 'Ahmed', 'Ali', 'Omar', 'Hassan',
        'Abdullah', 'Abdulrahman', 'Faisal', 'Saeed', 'Khalid',
        'Tariq', 'Majid', 'Salim', 'Nasser', 'Rashid'
    ]
    ARABIC_COMPANIES = [
        'AlFaris', 'AlHuda', 'AlMadina', 'AlNour',
        'AlSafwa', 'AlJazeera', 'AlAmal', 'AlQasim', 'AlRashid', 'AlMajid'
    ]
    ARABIC_SENTENCES = [
        'This community is dedicated to art and culture.',
        'Join us to explore creativity and tradition.',
        'Experience a unique blend of heritage and modern art.',
        'Discover authentic artistic expressions.',
        'Where passion meets creativity.',
        'A platform for emerging talents.',
        'Inspiring art with a touch of tradition.',
        'Celebrating the spirit of art and culture.'
    ]
    
    def arabic_name(self):
        return random.choice(self.ARABIC_NAMES)
    
    def arabic_company(self):
        return random.choice(self.ARABIC_COMPANIES)
    
    def arabic_sentence(self):
        return random.choice(self.ARABIC_SENTENCES)

fake = Faker('en_US')
fake.add_provider(ArabicProvider)

print("Creating fake users...")
users = []
for _ in range(20):
    username = fake.arabic_name() + str(random.randint(1, 1000))
    user = CustomUser.objects.create_user(
        username=username,
        email=fake.email(),
        password="test12345"
    )
    users.append(user)
print(f"Created {len(users)} users.")

print("Creating fake communities...")
communities = []
for _ in range(10):
    community = Community.objects.create(
        name=fake.arabic_company() + " Community",
        description=fake.arabic_sentence(),
        image="default.jpeg"
    )
    num_members = random.randint(1, len(users))
    members = random.sample(users, num_members)
    for user in members:
        community.members.add(user)
    communities.append(community)
print(f"Created {len(communities)} communities.")

print("Creating fake clubs...")
clubs = []
for _ in range(10):
    club = Club.objects.create(
        name=fake.arabic_company() + " Club",
        description=fake.arabic_sentence(),
        image="default.jpeg"
    )
    num_members = random.randint(1, len(users))
    members = random.sample(users, num_members)
    for user in members:
        club.members.add(user)
    clubs.append(club)
print(f"Created {len(clubs)} clubs.")

print("Creating fake products...")
products = []
for _ in range(20):
    product = Product.objects.create(
        name=fake.arabic_company() + " " + fake.word().capitalize(),
        description=fake.arabic_sentence(),
        price=fake.pydecimal(left_digits=3, right_digits=2, positive=True),
        image="default.jpeg"
    )
    num_likes = random.randint(0, len(users))
    liked_by = random.sample(users, num_likes)
    for user in liked_by:
        product.likes.add(user)
    products.append(product)
print(f"Created {len(products)} products.")

print("Fake data generation completed.")
