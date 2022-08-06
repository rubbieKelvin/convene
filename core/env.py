import os
import dotenv
from typing import cast
from .constants import BASE_DIR

dotenv.load_dotenv(BASE_DIR / '.env')

env = lambda x : {
        **dotenv.dotenv_values(BASE_DIR / '.env'),
        **os.environ # system environ should override .env
    }.get(x)

class Env:
    SECRET_KEY: str = env('SECRET_KEY')
    DEBUG: bool = bool(env('DEBUG'))
    ALLOWED_HOSTS: list[str] = cast(str, env('ALLOWED_HOSTS') or '*').split(',')


