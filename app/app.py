from authlib.common.security import generate_token
from authlib.integrations.flask_client import OAuth
from db_functions import update_or_create_user
from dotenv import load_dotenv
from faker import Faker
from flask import Flask, jsonify, render_template, redirect, request, session, url_for 
from sqlalchemy import create_engine, text
import os
import sentry_sdk

# Initialize Sentry
sentry_sdk.init(
    dsn="https://2c6193acab781279eb94c357479f1413@o4506413687177216.ingest.sentry.io/4506413783711744",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

# Create a Flask app instance
app = Flask(__name__)

# Create a Faker instance
fake = Faker()

# Load environment variables from .env file
load_dotenv()

# Google OAuth connection settings 
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
app.secret_key = os.urandom(12)
oauth = OAuth(app)

# Database connection settings 
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

# Define a route for the login page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/.auth/login/google')
def google():
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    redirect_uri = url_for('google_auth', _external=True)
    print('REDIRECT URL: ', redirect_uri)
    session['nonce'] = generate_token()
    redirect_uri = 'https://beckieflaskapp.azurewebsites.net/.auth/login/google/callback'
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

@app.route('/.auth/login/google/callback')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    update_or_create_user(user)
    print(" Google User ", user)
    return redirect('/home')

# Define a route for the home page
@app.route('/home')
def base():
    return render_template('home.html')

# Define a route for the doctors page
@app.route('/doctors')
def doctors():
    with engine.connect() as connection:
        query1 = text('SELECT * FROM doctors_cardiology')
        result1 = connection.execute(query1)
        fetch_result1 = result1.fetchall()

        query2 = text('SELECT * FROM doctors_dermatology')
        result2 = connection.execute(query2)
        fetch_result2 = result2.fetchall()
    
        query3 = text('SELECT * FROM doctors_endocrinology')
        result3 = connection.execute(query3)
        fetch_result3 = result3.fetchall()

        query4 = text('SELECT * FROM doctors_gastroenterology')
        result4 = connection.execute(query4)
        fetch_result4 = result4.fetchall()

    return render_template('doctors.html', data1=fetch_result1, data2=fetch_result2, data3=fetch_result3, data4=fetch_result4)

# Define a route for the contact page
@app.route('/contact')
def contact():
    fake_address = fake.address()
    fake_phone = fake.phone_number()
    return render_template('contact.html', location=fake_address, phone=fake_phone)

# Define a route for the logout page
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

# Define a route for the API
@app.route('/api', methods=['GET'])
def api():
    try:
        specialization = request.args.get('specialization')
        with engine.connect() as connection:
            query = text(f"SELECT * FROM {specialization}")
            result = connection.execute(query)
        return render_template('api.html', result=result)
    except Exception as e:
        raise Exception(f'Error with your request: {e}')

# Query string = api?specialization=doctors_<name_of_specialization>

# Define a route for Flask application errors
@app.route('/error')
def error():
    raise Exception('Error with the Flask application')

# Define a route for database connection errors
@app.route('/db-error')
def db_error():
    conn = create_engine(f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_NAME}')
    try:
        conn.connect()
    except Exception as e:
        raise Exception(f'Error connecting to the database: {e}')

if __name__ == '__main__':
   app.run(debug=True)