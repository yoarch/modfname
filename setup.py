import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="modfname",
    version="1.0.2",
    python_requires='>=3',
    author="yoarch",
    author_email="yo.managements@gmail.com",
    description="file and folder name modifier on the all system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yoarch/modfname",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
	"console_scripts": [
	"modfname = modfname.modfname:main",
	"mfn = modfname.modfname:main"
        ]
    })
