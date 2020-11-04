from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='auto_ohin',
    packages=['auto_ohin'],

    version='0.1.0',

    license='MIT',

    install_requires=['Pillow', 'reportlab', 'PyPDF4', 'jsonnet'],

    author='mitawaut',
    author_email='so.misawa.research@gmail.com',

    url='https://github.com/MitawaUT/auto-ohin',

    description='You can ohin on the input pdf easily.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='auto-ohin auto_ohin autoohin',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],

    entry_points={
        "console_scripts": [
            "auto-ohin = auto_ohin.auto_ohin:main",
            "auto_ohin = auto_ohin.auto_ohin:main"
        ]
    }
)
