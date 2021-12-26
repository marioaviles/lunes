from setuptools import setup

setup(
    name='lunes',
    version='0.1.0',    
    description='Amenities for Flask',
    url='https://github.com/marioaviles/',
    author='Mario Aviles',
    author_email='mariogaelaviles@gmail.com',
    license='BSD 2-clause',
    packages=['lunes'],
    install_requires=['flask>=2.0.1','uuid>=1.30'],
    classifiers=[
        'Development Status :: 0 - alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.5'
    ],
    scripts=['lunes/lunes'],
      package_data={'lunes': ['templates/controller.py','templates/app.py','templates/show.html','templates/edit.html','templates/index.html','templates/new.html','templates/app.html']},
)
