import os
from dotenv import load_dotenv


load_dotenv()
mail_user = os.environ.get('MAIL_USER')
mail_passwd = os.environ.get('MAIL_PASSWORD')
