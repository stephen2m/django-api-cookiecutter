import factory
from faker import Faker
from django.contrib.auth import get_user_model

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.LazyFunction(lambda: fake.user_name())
    email = factory.LazyFunction(lambda: fake.email())
    first_name = factory.LazyFunction(lambda: fake.first_name())
    last_name = factory.LazyFunction(lambda: fake.last_name())