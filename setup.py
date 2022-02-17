from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='clean_folder_16022022',
      version='0.0.1',
      description='Sort all files in folder',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/Makson047/clean_folder',  # todo
      author='Makson_047',
      author_email='bogatyuk1998@gmail.com',
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      packages=find_namespace_packages(),
      python_requires=">=3.8",
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']},
      )

