import os
import django
import random
from faker import Faker
from faker.providers import BaseProvider

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")  # Replace "project.settings" with your settings module
django.setup()

# Custom provider for Arabic data using ar_SA locale with RTL marker prefix
class ArabicProvider(BaseProvider):
    # Arabic names typical for the region
    ARABIC_NAMES = ['محمد', 'أحمد', 'علي', 'عمر', 'حسن', 'عبدالله', 'عبدالرحمن', 'فيصل', 'سعيد', 'خالد']
    # Arabic companies or artistic identifiers
    ARABIC_COMPANIES = ['الفارس', 'الهُدى', 'المدينة', 'النور', 'السفوة', 'الجزيرة', 'الأمل', 'القاسم', 'الرشيد', 'المجيد']
    # Arabic sentences for descriptions
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
    # Fixed, unique Arabic category names (related to art specialties)
    ARABIC_CATEGORY_NAMES = ["الخياطة", "النحت", "الرسم", "الخط", "التصوير", "التطريز", "الفخار", "الموسيقى", "الأدب", "العمارة"]

    def arabic_name(self):
        # Prefix with RTL marker to maintain proper order
        return "\u200F" + random.choice(self.ARABIC_NAMES)
    
    def arabic_company(self):
        return "\u200F" + random.choice(self.ARABIC_COMPANIES)
    
    def arabic_sentence(self):
        return "\u200F" + random.choice(self.ARABIC_SENTENCES)
    
    def arabic_category(self):
        return "\u200F" + random.choice(self.ARABIC_CATEGORY_NAMES)

# Initialize Faker with Arabic (Saudi Arabia) locale
fake = Faker('ar_SA')
fake.add_provider(ArabicProvider)

# Import models (ensure your project structure is correct)
from accounts.models import CustomUser
from communities.models import Community
from clubs.models import Club
from category.models import Category
from products.models import Product

# Create 20 fake users
users = []
for _ in range(20):
    # Using Faker's unique method ensures different names
    username = fake.unique.first_name() + str(random.randint(1, 1000))
    user = CustomUser.objects.create_user(
        username=username,
        email=fake.email(),
        password="test12345",
        full_name=fake.name(),
        specialization=fake.word()  # Using a random word as specialization
    )
    users.append(user)

# Create 10 fake communities and assign random members
communities = []
for _ in range(10):
    community = Community.objects.create(
        name=fake.arabic_company() + " مجتمع",
        description=fake.arabic_sentence(),
        image="default.jpeg"
    )
    num_members = random.randint(1, len(users))
    for user in random.sample(users, num_members):
        community.members.add(user)
    communities.append(community)

# Create 10 fake clubs and assign random members
clubs = []
for _ in range(10):
    club = Club.objects.create(
        name=fake.arabic_company() + " نادي",
        description=fake.arabic_sentence(),
        image="default.jpeg"
    )
    num_members = random.randint(1, len(users))
    for user in random.sample(users, num_members):
        club.members.add(user)
    clubs.append(club)

# Create 10 fake categories using the fixed unique list
categories = []
for name in ArabicProvider.ARABIC_CATEGORY_NAMES:
    category = Category.objects.create(
        name=name,
        description=fake.text(max_nb_chars=100)
    )
    categories.append(category)

# Create 20 fake products assigned to random categories and with random likes
products = []
for _ in range(20):
    category = random.choice(categories)
    product = Product.objects.create(
        name=fake.arabic_company() + " " + fake.word(),
        description=fake.text(max_nb_chars=200),
        price=fake.pydecimal(left_digits=3, right_digits=2, positive=True),
        image="default.jpeg",
        category=category
    )
    num_likes = random.randint(0, len(users))
    for user in random.sample(users, num_likes):
        product.likes.add(user)
    products.append(product)

# Randomly assign some purchased products to users
for user in users:
    num_purchases = random.randint(0, len(products))
    purchased = random.sample(products, num_purchases)
    for product in purchased:
        user.purchased_products.add(product)

print("Fake data generation completed.")
