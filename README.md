## Requirements

### Secret

#### `.secret/base.json`

```json
{
    "SECRET_KEY": "<Django secret key>"
}
```

#### `.secret/dev.json`

> PostgreSQL을 사용, DATABASES섹션의 설정이 필요

```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "mydbpractice.ccrdezcnkmuh.ap-northeast-2.rds.amazonaws.com",
      "PORT": 5432,
      "USER": "leesoo",
      "PASSWORD": "violet2129",
      "NAME": "ec2_deploy_rds"
    }
  }
}
```

## Installation

```
pipenv install
pipenv shell
cd app
./manage.py runserver
```