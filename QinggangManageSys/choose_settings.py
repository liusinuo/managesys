"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
# choose settings between Developement and Deploy
import os
import platform

lab_ip = '202.204.54.42'
master_ip = '10.30.0.152'
backuppwd= "xxxx"
node = platform.node()
print(node)
dev_machines = ('cheng-cx','cheng-cx.local')
win_machines = ('chyulia-PC',"TP-PC")


if node in dev_machines:
    # folder QinggangManageSys
    QinggangManageSys = os.path.dirname(os.path.dirname(__file__))
    # project dir, contains static and media folder under DEV environment
    PROJECT_DIR = os.path.dirname(QinggangManageSys)
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'qinggang',
            'USER': 'root',
            'PASSWORD': '123456',
            # 'HOST': master_ip,
            'HOST': lab_ip,
            'PORT': '3306',
        },
        'l2own': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME':'orcl',
            'USER': 'qg_user',
            'PASSWORD': '123456',
            'HOST': lab_ip,
            'PORT': '1521',
        },
        'sale': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME':'orcl',
            'USER': 'meskc',
            'PASSWORD': '123456',
            'HOST': lab_ip,
            'PORT': '1521',
        },
    }
    print(PROJECT_DIR)
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
    print(MEDIA_ROOT)
    MEDIA_URL = '/media/'
    STATICFILES_DIRS = (
        os.path.join(PROJECT_DIR, 'static'),
    )
    TEMPLATE_DIRS = [os.path.join(QinggangManageSys, 'templates')]
    ALLOWED_HOSTS = ['*']
elif node == "cheng-cx.local1":
    print("单独加了一个独立的分支,以便适应现场的环境")
    DEBUG = True
    DATABASES = {
        'l2own': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME':'qinggang',
            'USER': 'qg_user',
            'PASSWORD': '123456',
            'HOST': master_ip,
            'PORT': '1521',
        },
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'qinggang',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': 'localhost',
            'PORT': '3306',
        },
        'mes_backup': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'mesdbdg',#sid:mesdb2;service:mesdb
            'USER': 'report_query',
            'PASSWORD': backuppwd,
            'HOST': '10.30.0.160',
            'PORT': '1521',
        },
        'l2_backup': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'qgil2dbdg',
            'USER': 'report_query',
            'PASSWORD': backuppwd,
            'HOST': '10.30.0.161',
            'PORT': '1521',
        },
        'sale': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME':'mesdbdg',
            'USER': 'report_query',
            'PASSWORD': backuppwd,
            'HOST': '10.30.0.160',
            'PORT': '1521',
        },
        'l2query': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME':'qinggang',
            'USER': 'query',
            'PASSWORD': 'qdisqdis',
            'HOST': '10.30.0.152',
            'PORT': '1521',
        },
    }
    # PROJECT_DIR = '/home/maksim/qinggang/managesys'
    PROJECT_DIR = '/Users/changxin/qinggang/managesys'
    # MEDIA_ROOT = '/home/maksim/qinggang/media/'
    MEDIA_ROOT = '/Users/changxin/qinggang/media/'
    MEDIA_URL = '/media/'
    # STATIC_ROOT = '/home/maksim/qinggang/static/'
    STATIC_ROOT = '/Users/changxin/qinggang/static/'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(PROJECT_DIR, 'static'),
    )

    TEMPLATE_DIRS = (
        os.path.join(PROJECT_DIR, 'templates'),
    )

    ALLOWED_HOSTS = [
        '*',
    ]
elif node == "hadoop01":
    print("部署在hadoop主节点")
    DEBUG = True
    DATABASES = {
        'l2own': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME':'qinggang',
            'USER': 'qg_user',
            'PASSWORD': '123456',
            'HOST': master_ip,
            'PORT': '1521',
        },
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'qinggang',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': master_ip,
            'PORT': '3306',
        },
        'mes_backup': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'mesdbdg',#sid:mesdb2;service:mesdb
            'USER': 'report_query',
            'PASSWORD': backuppwd,
            'HOST': '10.30.0.160',
            'PORT': '1521',
        },
        'l2_backup': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'qgil2dbdg',
            'USER': 'report_query',
            'PASSWORD': backuppwd,
            'HOST': '10.30.0.161',
            'PORT': '1521',
        },
        'sale': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME':'mesdbdg',
            'USER': 'report_query',
            'PASSWORD': backuppwd,
            'HOST': '10.30.0.160',
            'PORT': '1521',
        },
        'l2query': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME':'qinggang',
            'USER': 'query',
            'PASSWORD': 'qdisqdis',
            'HOST': '10.30.0.152',
            'PORT': '1521',
        },
    }
    PROJECT_DIR = '/home/hadoop/qinggang/managesys'
    MEDIA_ROOT = '/home/hadoop/qinggang/media/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = '/home/hadoop/qinggang/static/'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(PROJECT_DIR, 'static'),
    )

    TEMPLATE_DIRS = (
        os.path.join(PROJECT_DIR, 'templates'),
    )

    ALLOWED_HOSTS = [
        '*',
    ]
elif node in win_machines:
    QinggangManageSys = os.path.dirname(os.path.dirname(__file__))
    # project dir, contains static and media folder under DEV environment
    PROJECT_DIR = os.path.dirname(QinggangManageSys)
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'qinggang',
            'USER': 'root',
            'PASSWORD': '123456',
            # 'HOST': master_ip,
            'HOST': lab_ip,
            'PORT': '3306',
        },
        'l2own': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME':'orcl',
            'USER': 'qg_user',
            'PASSWORD': '123456',
            'HOST': lab_ip,
            'PORT': '1521',
        },
        'sale': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME':'orcl',
            'USER': 'meskc',
            'PASSWORD': '123456',
            'HOST': lab_ip,
            'PORT': '1521',
        },
    }
    print(PROJECT_DIR)
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
    print(MEDIA_ROOT)
    MEDIA_URL = '/media/'
    STATICFILES_DIRS = (
        os.path.join(PROJECT_DIR, 'static'),
    )
    TEMPLATE_DIRS = [os.path.join(QinggangManageSys, 'templates')]
    ALLOWED_HOSTS = ['*']
else:
    DEBUG = True
    DATABASES = {
        'l2own': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME':'orcl',
            'USER': 'qg_user',
            'PASSWORD': '123456',
            'HOST': '202.204.54.42',
            'PORT': '1521',
        },
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'qinggang',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': '202.204.54.42',
            'PORT': '3306',
        },
        'mes_backup': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'mesdbdg',#sid:mesdb2;service:mesdb
            'USER': 'report_query',
            'PASSWORD': backuppwd,
            'HOST': '10.30.0.160',
            'PORT': '1521',
        },
        'l2_backup': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'qgil2dbdg',
            'USER': 'report_query',
            'PASSWORD': backuppwd,
            'HOST': '10.30.0.161',
            'PORT': '1521',
        },
        'sale': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME':'orcl',
            'USER': 'meskc',
            'PASSWORD': '123456',
            'HOST': '202.204.54.42',

        },
    }
    PROJECT_DIR = '/home/maksim/qinggang/managesys'
    PROJECT_DIR_BASE = '/home/maksim/qinggang/'
    # PROJECT_DIR = '/Users/changxin/qinggang/managesys'
    MEDIA_ROOT = os.path.join(PROJECT_DIR_BASE, 'media/')

    # MEDIA_ROOT = '/Users/changxin/qinggang/media/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(PROJECT_DIR_BASE, 'static/')
    # STATIC_ROOT = '/Users/changxin/qinggang/static/'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(PROJECT_DIR, 'static'),
    )

    TEMPLATE_DIRS = (
        os.path.join(PROJECT_DIR, 'templates'),
    )

    ALLOWED_HOSTS = [
        '*',
    ]

    # # cache entire site
    # MIDDLEWARE_CLASSES_ADDITION_FIRST = (
    #     'django.middleware.cache.UpdateCacheMiddleware',
    # )

    # MIDDLEWARE_CLASSES_ADDITION_LAST = (
    #     'django.middleware.cache.FetchFromCacheMiddleware',
    # )

    # CACHES = {
    #     'default': {
    #         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #         'LOCATION': '127.0.0.1:11211',
    #     }
    # }
