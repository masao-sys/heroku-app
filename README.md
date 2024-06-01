Heroku コマンド
============

## 各種コマンド

### ログイン
```shell
heroku login
```

### ログアウト
```shell
heroku logout
```

### プロジェクト作成
```shell
heroku create
```

### Gitリモート確認
```shell
git remote -v
```

### SECRET_KEYをHerokuに設定
```shell
heroku config:set SECRET_KEY='***************************'
```

### 環境変数確認
```shell
heroku config
```

### HerokuにPush
```shell
git push heroku main
```

### テーブル作成
```shell
heroku run python manage.py migrate
```

### 管理者アカウント作成
```shell
heroku run python manage.py createsuperuser
```

### プロセス起動
```shell
heroku ps:scale web=1
```

### スーパーユーザー作成
```shell
heroku run python3 manage.py superuser
```
