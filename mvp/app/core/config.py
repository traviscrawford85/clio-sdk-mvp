# app/config.py
"""
Configuration module for FastAPI app.
Loads environment variables and provides settings for the application.
Edit as needed for your project.
"""
import os
from dotenv import load_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

# Load .env file if present
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

class Settings(BaseSettings):
    # General
    ENV: str = Field(default="development", env="ENV")
    DEBUG: bool = Field(default=False, env="DEBUG")
    SECRET_KEY: str = Field(default="your-secret-key", env="SECRET_KEY")

    # Database
    DATABASE_URL: str = Field(default="sqlite:///./app.db", env="DATABASE_URL")

    # OAuth/Clio
    CLIO_CLIENT_ID: str = Field(default="", env="CLIO_CLIENT_ID")
    CLIO_CLIENT_SECRET: str = Field(default="", env="CLIO_CLIENT_SECRET")
    CLIO_REDIRECT_URI: str = Field(default="", env="CLIO_REDIRECT_URI")
    CLIO_TOKEN_URL: str = Field(default="https://app.clio.com/oauth/token", env="CLIO_TOKEN_URL")

    # QuickBooks
    QBO_CLIENT_ID: str = Field(default="", env="QUICKBOOKS_CLIENT_ID")
    QBO_CLIENT_SECRET: str = Field(default="", env="QUICKBOOKS_CLIENT_SECRET")
    QBO_REDIRECT_URI: str = Field(default="", env="QUICKBOOKS_REDIRECT_URI")
    QBO_VERIFICATION_TOKEN: str = Field(default="", env="QUICKBOOKS_VERIFICATION_TOKEN")
    QBO_REALM_ID: str = Field(default="", env="QUICKBOOKS_REALM_ID")
    QBO_ENVIRONMENT: str = Field(default="", env="QUICKBOOKS_ENVIRONMENT")
    QBO_API_URL: str = Field(default="", env="QUICKBOOKS_API_URL")
    QBO_REFRESH_TOKEN: str = Field(default="", env="QUICKBOOKS_REFRESH_TOKEN")

    # Slack
    SLACK_CLIENT_ID: str = Field(default="", env="SLACK_CLIENT_ID")
    SLACK_CLIENT_SECRET: str = Field(default="", env="SLACK_CLIENT_SECRET")
    SLACK_SIGNING_SECRET: str = Field(default="", env="SLACK_SIGNING_SECRET")

    # Celery
    CELERY_BROKER_URL: str = Field(default="redis://localhost:6379/0", env="CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND: str = Field(default="redis://localhost:6379/0", env="CELERY_RESULT_BACKEND")

    class Config:
        env_file = Path(__file__).parent.parent / ".env"
        env_file_encoding = "utf-8"

settings = Settings()
