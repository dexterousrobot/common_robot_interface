# -*- coding: utf-8 -*-
"""Setup file for Common Robot Interface.
"""

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="common_robot_interface",
    version="0.5.0",
    description="Common Robot Interface",
    license="GPLv3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="John Lloyd, Nathan Lepora",
    author_email="j.lloyd@bristol.ac.uk, n.lepora@bristol.ac.uk",
    url="https://github.com/robot-dexterity/common-robot-interface",
    packages=["cri", "cri.abb", "cri.ur", "cri.ur.rtde", "cri.dobot", "cri.dobot.mg400",  "cri.dobot.cr", "cri.dobot.magician"],
	package_data={'cri.ur': ['rtde_config.xml'],
            "cri.dobot.magician": ['DobotDll.dll',"msvcp120.dll","msvcr120.dll","Qt5Core.dll","Qt5Network.dll","Qt5SerialPort.dll"]},
    install_requires=["numpy", "transforms3d"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)