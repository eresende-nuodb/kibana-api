import setuptools

with open("README.md", "r", encoding="utf-8") as description:
    long_description = description.read()

setuptools.setup(
    name="kibana-api",
    version="0.0.5",
    author="Eusebio Resende",
    author_email="eresende@nuodb.com",
    description="This is an API mapping library for Kibana API to generate visualizations and dashboards automatically",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/eresende-nuodb/kibana-api",
    project_urls={
        "Bug Tracker": "https://github.com/eresende-nuodb/kibana-api/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords=["elasticsearch", "kibana", "development", "api mapping"],
    packages=["kibana_api"],
    package_data={
        'kibana_api': [
            'mappings/*.json',
        ]
    },
    install_requires=[
        "requests",
        "multipledispatch"
    ],
    python_requires=">=3.0",
)
