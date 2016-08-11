from setuptools import setup

setup(
    name='django_dynamic_forms',
    version='0.1',
    description='Generate Django Forms on the fly',
    author='Kirt Gittens III',
    author_email='damagecontrolsoftware@gmail.com',
    packages=['dynamic_forms'],
    install_requires=[
        'Django'
    ],
    license='GNU'
)