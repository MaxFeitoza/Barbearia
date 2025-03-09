import factory
from datetime import datetime
from user.models import User


class UserAdminFactory(factory.django.DjangoModelFactory):
    email = factory.Sequence(lambda n: "user-{}@example.com".format(n))
    password = factory.Faker("password")
    name = factory.Faker("name")
    last_name = factory.Faker("last_name")
    phone_number = factory.Faker("msisdn")
    created_at = datetime.now()
    admin_user = 0

    class Meta:
        model = User


class UserClientFactory(factory.django.DjangoModelFactory):
    email = factory.Sequence(lambda n: "user-{}@example.com".format(n))
    password = factory.Faker("password")
    name = factory.Faker("name")
    last_name = factory.Faker("last_name")
    phone_number = factory.Faker("msisdn")
    created_at = datetime.now()
    admin_user = 1

    class Meta:
        model = User
