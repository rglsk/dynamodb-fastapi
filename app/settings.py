from pydantic import BaseSettings


class GlobalConfig(BaseSettings):
    DB_HOST: str = "http://dynamodb:8000"
    ENVIRONMENT: str = "test"
    AWS_REGION: str = "eu-west-1"


config = GlobalConfig()
