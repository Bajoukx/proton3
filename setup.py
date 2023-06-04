"""Setup for the proton3 package."""

from setuptools import setup

REQUIRED_PACKAGES = [
    'absl-py', 'pylint', 'yapf', 'numpy', 'torch', 'torchvision', 'torchaudio'
]

setup(name='proton3',
      version='0.1.0',
      description='A package for the proton3 project.',
      author='bajoukx',
      install_requires=REQUIRED_PACKAGES)
