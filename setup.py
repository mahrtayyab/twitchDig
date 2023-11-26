from distutils.core import setup

setup(
    name='twitchDig',
    packages=['twitchDig', 'twitchDig.types'],
    version='0.1',
    license='MIT',
    description='An easy Twitch Scraper',
    author='Tayyab Kharl',
    author_email='tayyabmahr@gmail.com',
    url='https://github.com/mahrtayyab/twitchDig',
    keywords=['Twitch', 'Twitch Scrape', 'Twitch Stream'],
    install_requires=[
        'httpx',
        'dateutils',
        'websocket-client'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
)
