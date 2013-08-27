
from distutils.core import setup

requires_list = [
    'hashlib==20081119',
    'nose>=1.3.0']

setup(
    name='xorcrypt',
    description='A simple python XOR encryption/decryption/obfuscation library',
    version='0.1',
    packages=['xorcrypt',],
    license='MIT License',
    long_description=open('README.md').read(),
    author="Sunil Sadasivan",
    author_email="sunil@bufferapp.com.com",
    maintainer="Sunil Sadasivan",
    maintainer_email="sunil@bufferapp.com",
    install_requires=requires_list,
    url="http://github.com/sunils34/python-xorcrypt"
)
