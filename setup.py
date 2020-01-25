from setuptools import setup, find_namespace_packages


TEST_REQUIREMENTS = ['pylint']

setup(
    name='runner',
    version='2020.01.24.0',
    description='',
    url='http://github.com/',
    author='interifter',
    author_email='zachary@interift.com',
    license='MIT',
    install_requires=[
        'click'
    ],
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    scripts=[
        "scripts/run.py"
    ],
    zip_safe=False,
    entry_points='''
        [console_scripts]
        colorun=run:main
    ''',
    extras_require={
        'test':TEST_REQUIREMENTS
    }
    )