# from setuptools import find_packages, setup

# setup(
#     name='flaskr',
#     version='1.0.0',
#     packages=find_packages(),
#     include_package_data=True,
#     zip_safe=False,
#     install_requires=[
#         'flask',
#     ],
# )

"""MANIFEST.in : 
    include flaskr/schema.sql
    graft flaskr/static
    graft flaskr/templates
    global-exclude *.pyc"""