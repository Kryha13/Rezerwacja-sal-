from faker import Factory
import random

from booking.models import Room

RANDOM_GRADES_CNT = 10000


def create_name():
    fake = Factory.create("pl_PL")
    name = fake.color_name()
    return name


def create_capacity():
    capacity = random.choice(range(20,200))
    return capacity


def create_projector():
    projector = random.choice([True, False])
    return projector


def create_Rooms():
    for i in range(0, 100):
        Room.objects.create(name=''.join(create_name()), capacity=create_capacity(), projector=create_projector())



