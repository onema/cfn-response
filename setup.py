import sys
from setuptools import setup

if sys.version_info < (3, 6):
    sys.exit('Sorry, Python < 3.6 is not supported')
setup(
    name='cfn-response',
    version='0.0.5',
    url='http://github.com/onema/cfn-response',
    license='BSD',
    author='Jorge Bastida, Juan Manuel Torres',
    author_email='me@jorgebastida.com, kinojman@gmail.com',
    description="""cfn-response is a micro package which exposes some
    helpers to talk with CloudFormation from within python Lambda functions.
    This package is intentionally small in order to be embedded lambda functions.
    If you are looking to create aws-lambda backed Custom CloudFormation
    resources using python, you are going to need this.""",
    keywords="aws lambda cloudformation custom resources",
    py_modules=["cfnresponse"],
    platforms='any',
    install_requires=[
        'requests>=2.18.4',
    ],
    test_suite='nose.collector',
    tests_require=['nose', 'coverage', 'mock'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ],
    zip_safe=False
)
