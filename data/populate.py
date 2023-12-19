from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import create_engine, text
import os

# Load environment variables from .env file
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Create a connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
engine = create_engine(conn_string, echo=False)

# Create a faker instance
fake = Faker()

# Create a function to insert fake data into tables
def insert_fake_data(engine, table_name, specialization, num_doctors=10):
    with engine.connect() as connection:
        for _ in range(num_doctors):
            
            first_name = fake.first_name()
            last_name = fake.last_name()
            date_of_birth = fake.date_of_birth()
            address = fake.address()
            phone_number = fake.phone_number()

            query = text(
                f"""
                INSERT INTO {table_name} (first_name, last_name, date_of_birth, address, phone_number, specialization)
                VALUES (:first_name, :last_name, :date_of_birth, :address, :phone_number, :specialization)
                """
            )

            params = {
                'first_name': first_name,
                'last_name': last_name,
                'date_of_birth': date_of_birth,
                'address': address,
                'phone_number': phone_number,
                'specialization': specialization
            }

            connection.execute(query, params)

        connection.commit()

# Use function to insert fake data into doctors_cardiology table
insert_fake_data(engine, 'doctors_cardiology', 'Cardiology', 10)

# Use function to insert fake data into doctors_dermatology table
insert_fake_data(engine, 'doctors_dermatology', 'Dermatology', 10)

# Use function to insert fake data into doctors_endocrinology table
insert_fake_data(engine, 'doctors_endocrinology', 'Endocrinology', 10)

# Use function to insert fake data into doctors_gastroenterology table
insert_fake_data(engine, 'doctors_gastroenterology', 'Gastroenterology', 10)