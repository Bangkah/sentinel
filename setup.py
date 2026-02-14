from setuptools import setup, find_packages

setup(
    name="sentinel-ai-cli",
    version="1.0.3",
        description="Professional Python Cybersecurity CLI Tool (Sentinel AI CLI)",
    author="Muhammad Dhiyaul Atha",
    author_email="mdhyaulatha@gmail.com",
    url="https://github.com/Bangkah/sentinel",
    packages=find_packages(),
    py_modules=["sentinel_ai"],
    install_requires=[
        "psutil",
        "colorama",
        "autopep8"
    ],
    entry_points={
        "console_scripts": [
                "sentinel-ai=sentinel_ai:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: System :: Networking :: Monitoring",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)