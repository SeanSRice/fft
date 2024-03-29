import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='fft',  
     version='1.0',
     scripts=['fft'] ,
     author="Rice",
     author_email="mrseanrice@gmail.com",
     description="A python fft package based on evergreenforest",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/SeanSRice/fft.git",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2.7",
         "License :: MIT License",
         "Operating System :: OS Independent*",
     ],
 )
