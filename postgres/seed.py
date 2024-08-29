from faker import Faker

from util import get_connection
import random
email_domains = [
    'com',
    'net',
    'org',
    'gov'
]


def fill_database(n=1000):
    status = ['new', 'in progress', 'completed']
    conn = get_connection('192.168.88.211', 'postgres', 'tasks', 'hw03')
    fake = Faker()

    with conn.cursor() as curr:
        for s in status:
            curr.execute(
                'insert into status(name) values (%s) on conflict do nothing', (s,))

    uquery = 'insert into users(fullname, email) values (%s, %s) returning id'
    tquery = 'insert into tasks(title, description, status_id, user_id) values(%s, %s, %s, %s)'

    with conn.cursor() as curr:
        for i in range(n):
            first_name = fake.first_name()
            last_name = fake.last_name()
            company = fake.company().split()[0].strip(',')
            dns_org = fake.random_choices(
                elements=email_domains,
                length=1
            )[0]

            email = f"{first_name}.{last_name}@{company}.{dns_org}".lower()
            name = f"{first_name} {last_name}"

            curr.execute(uquery, (name, email))
            res = curr.fetchone()
            for i in range(random.randint(2, 7)):
                curr.execute(
                    tquery, (fake.country(), fake.text(), random.randint(1, 3), res[0]))


if __name__ == "__main__":
    fill_database()
