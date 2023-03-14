## Django CORS Headers

Django CORS Headers is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).

## Installation
``` bash 
pip install django-cors-headers
```
## Configuration
Add `corsheaders` to your `INSTALLED_APPS` setting:
``` python
INSTALLED_APPS = (
    ...
    'corsheaders',
    ...
)
```
Add `corsheaders.middleware.CorsMiddleware` to your `MIDDLEWARE_CLASSES` setting:
``` python
MIDDLEWARE_CLASSES = (
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
)
```
Add `corsheaders.middleware.CorsPostCsrfMiddleware` to your `MIDDLEWARE_CLASSES` setting:
``` python
MIDDLEWARE_CLASSES = (
    ...
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
)
```
Add `corsheaders` to your `ROOT_URLCONF` setting:
``` python
ROOT_URLCONF = 'myproject.urls'
CORS_ALLOW_ALL_ORIGINS = True


```
after allowing CORS headers we can use fetch API to perform CRUD operation on the API
## fetch API for creating new  item 

``` javascript
 fetch('http://127.0.0.1:8000/api/',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                title:title,
                description:description
            }),
        }).then(res=>{
            if (res.ok){
                return res.json()}
                else{
                    throw new Error('Something went wrong')
                }
            }).then (data=>{
                console.log(data)
            })
        })
``` 





