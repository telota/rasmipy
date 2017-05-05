from setuptools import setup


setup(
    name='rasmipy',
    version='0.2.1',
    python_requires='>=3',
    extras_require={'rest-service': ['hug']},
    packages=['rasmipy'],
    entry_points={'console_scripts':
                  ['rasmify-rest-service=rasmipy.rest_service:serve [rest-service]']},
    url='https://github.com/telota/rasmipy',
    license='LGPLv3',
    author='Oliver Pohl, Frank Sachsenheim',
    author_email='telota@bbaw.de',
    description='Reduce Arabic strings to their rasm, ie remove vocalization and other diacritics.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: Arabic',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Linguistic'
    ]
)
