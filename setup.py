from setuptools import setup, find_packages

setup(
    name = "PiUI",
    version = "0.1.2",
    packages = find_packages(),
    install_requires = [
        "PySide6",
        "Xlib",
        "colorlog"
    ],
    author = "haseeebz",
    description = "Qt-Based UI Toolkit for making bars, widgets, lockscreens and menus for Linux",
    scripts=['./PiUI/core/pi-ctl']
)