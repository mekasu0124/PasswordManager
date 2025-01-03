from setuptools import setup, find_packages

setup(
    name='password_manager',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Click',  # Ensure Click is listed as a dependency
    ],
    entry_points={
        'console_scripts': [
            'pwm=app.main:cli',  # Replace 'cli' with the name of your Click command function
        ],
    },
)
