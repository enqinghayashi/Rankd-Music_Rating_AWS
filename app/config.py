import os
from typing import Optional
basedir = os.path.abspath(os.path.dirname(__file__))
default_database_url = 'sqlite:///' + os.path.join(basedir, 'app.db')

def _normalize_database_url(url: Optional[str]) -> Optional[str]:
    if not url:
        return url
    # SQLAlchemy expects postgresql://, but some platforms provide postgres://
    if url.startswith('postgres://'):
        return 'postgresql://' + url[len('postgres://'):]
    return url

class Config(object):
    SQLALCHEMY_DATABASE_URI = _normalize_database_url(os.environ.get('DATABASE_URL')) or default_database_url
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"  
    UPLOAD_FOLDER = 'app/static/img/profile_pictures'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

class DeploymentConfig(Config):
    SQLALCHEMY_DATABASE_URI = _normalize_database_url(os.environ.get('DATABASE_URL')) or default_database_url

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

