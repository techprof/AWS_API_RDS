from chalice import Chalice
import psycopg2

#app = Chalice(app_name='helloworld')

app = Chalice(app_name='helloworld')
db_user = 'test'
db_pass = 'password'
db_host = 'https://.....'
db_port = 5432

@app.route('/get_data')
def get_data():
    with psycopg2.connect(user=db_user, password=db_pass, ...) as conn:
        with conn.cursor() as cur:    
            cur.execute("SELECT user_name, DOB FROM test")

@app.route('/')
def index():
    return {'hello': 'world': 'cur'}
	