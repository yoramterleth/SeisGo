from numpy.distutils.core import setup

setup(
    name='seispy',
    version='0.5.0',
    description='A Python package for seismic data analysis',
    author='Xiaotao Yang',
    author_email='stcyang@gmail.com',
    maintainer='Xiaotao Yang',
    maintainer_email='stcyang@gmail.com',
    download_url='https://github.com/xtyangpsp/SeisPy/archive/refs/tags/v0.5.0.tar.gz',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'],
    install_requires=['numpy',
                        'scipy',
                        'pandas',
                        'obspy',
                        'pyasdf',
                        'numba',
                        'pycwt'
        ],
    python_requires='>=3.6',
    packages=['seispy']) #scripts=scripts
