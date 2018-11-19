from setuptools import setup, find_packages
setup(name='enmailer',
      description='Evernote Email Sender',
      version='1.0.0',
      url='https://github.com/chiantiscarlett/evernote-mailer',
      author='Chianti Scarlett',
      author_email='chianti.scarlett@gmail.com',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3'
      ],
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=[]
      )
