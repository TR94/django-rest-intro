import os

# django secret key 
os.environ.setdefault('SECRET_KEY', "django-nowsecure-5qsmz-$rg!o*fm+3l^=616az_2h4%*=db_81#!huc(%lsiip8&")

# cloudinary connection
os.environ['CLOUDINARY_URL']= 'cloudinary://659183824575138:-cnW2HCg5Ocn2ETg6w2XHmX1kdA@dtgt7gfx7'

# during development session authentication is used. This will be changed to JSON Web Tokens for production release
os.environ['DEV'] = '1'

os.environ['DATABASE_URL'] = "postgres://gtrcuszs:5bIWrF50ags5GzDJ1Tt2qlDvaowch0Ym@tyke.db.elephantsql.com/gtrcuszs"

