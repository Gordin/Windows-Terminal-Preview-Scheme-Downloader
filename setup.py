from setuptools import setup

setup(
    name='windows_terminal_scheme_manager',
    version='0.3',
    packages=['windows_terminal_scheme_manager'],
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'wtsm = windows_terminal_scheme_manager.scheme_manager:cli'
        ]
    },
)
