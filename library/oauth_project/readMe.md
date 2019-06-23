# 헤매였던 부분

> **{% load socialaccount %}**
>
> **{% provider_login_url 'kakao' method='oauth2' %}**
>
> ```html
> {% load socialaccount %}
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <meta name="viewport" content="width=device-width, initial-scale=1.0">
>     <meta http-equiv="X-UA-Compatible" content="ie=edge">
>     <title>Login</title>
> </head>
> <body>
>     <form method="POST">
>         {% csrf_token %}
>         <input type="text" name="auth_id">
>         <input type="password" name="auth_pwd">
>         <input type="submit" value="Login">
>     </form>
> 
>     <a href="{% provider_login_url 'kakao' method='oauth2' %}">Kakao_login</a>
> </body>
> </html>
> ```

이외 `애플리케이션 설정`