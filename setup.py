from setuptools import setup, find_packages

setup(
    name = "PiUI",
    version = "0.1.0",
    packages = find_packages(),
    install_requires = [
        "PySide6",
        "Xlib",
        "colorlog"
    ],
    author = "haseeebz",
    description = "Qt-Based UI Toolkit for making bars, widgets, lockScreens and menus for Linux",
    scripts=['./PiUI/core/pi-cli']
)