import os
import setuptools;

READ_ME_FILE  ="README.md";

long_description = "MVVM viewmodelbase to for other applications";
if(os.path.exists(READ_ME_FILE)):
    with open(READ_ME_FILE, "r") as fh:
        long_description = fh.read()
    
setuptools.setup(name = "mvvm-jimobama",
      version="0.0.1",
      description="A python string localisation class",
      long_description =long_description,
      url="https://github.com/miljimo/pymvvm.git",
      long_description_content_type="text/markdown",
      author="Obaro I. Johnson",
      author_email="johnson.obaro@hotmail.com",
      packages=['mvvm', ],
      install_requires=[],
      classifiers=[
        "Software Engineer :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
         
    ],python_requires='>=3.0');
