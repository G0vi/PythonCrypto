from distutils.core import setup
files = ['Qmath/*']
setup(name = 'Qmath', 
      version = '1.0',
      description = 'CTF Crypto',
      author = 'G0vi',
      author_email = 't2502903838@163.com',
      packages = [''], 
      package_data = {'': files},
      )

