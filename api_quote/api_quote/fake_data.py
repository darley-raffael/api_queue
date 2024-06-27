from faker import Faker


fake = Faker("pt_BR")


def get_fake_data():

    list_fake_data = []
    count = 0
    for _ in range(10):
        count += 1
        list_fake_data.append(
            {
                "id": count,
                "name": fake.name(),
            }
        )

    return list_fake_data
