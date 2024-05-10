from setuptools import find_packages, setup

setup(
    name="my_etl_project",
    packages=find_packages(exclude=["etl_tests"]),
    install_requires=[
        "dagster",
        "dagster-webserver"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
