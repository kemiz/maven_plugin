from setuptools import setup

setup(
    name='cloudify-maven-plugin',
    version='1.0',
    author='kemiz',
    packages=['maven_plugin'],
    license='LICENSE',
    dependency_links=[
        'https://github.com/kemiz/cloudify-package-installer-plugin/archive/master.zip'
    ], requires=[
        'cloudify==3.2.1'
    ]
)
