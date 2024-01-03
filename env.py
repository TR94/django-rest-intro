import os

# django secret key 
os.environ['SECRET_KEY']= ""

# cloudinary connection
os.environ['CLOUDINARY_URL']= 'cloudinary://659183824575138:-cnW2HCg5Ocn2ETg6w2XHmX1kdA@dtgt7gfx7'

# during development session authentication is used. This will be changed to JSON Web Tokens for production release
os.environ['DEV'] = '1'

