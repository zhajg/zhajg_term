from setuptools import setup

setup(
    name='TracTicketValidator',
    version='1.0',
    maintainer='Jianguo Zha',
    maintainer_email='zhajg@fullhan.com',
    description="Ticket validator plugin for Trac.",
    license='BSD',
    keywords='trac ticket validator',
    packages=['TracTicketValidator'],
    classifiers=[
        'Framework :: Trac',
    ],
    install_requires=['Trac'],
    entry_points={
        'trac.plugins': [
            'TracTicketValidator = TracTicketValidator.TicketValidator'
        ]
    },
)
