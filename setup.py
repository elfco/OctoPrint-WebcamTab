# coding=utf-8
from setuptools import setup

########################################################################################################################

plugin_identifier = "webcamtab_g"
plugin_package = "octoprint_webcamtab_g"
plugin_name = "OctoPrint-WebcamTab_G"
plugin_version = "0.1.5"
plugin_description = """Show webcam stream in separate tab"""
plugin_author = "Sven Lohrmann, Bryan Rentoul"
plugin_author_email = "gruvin@gmail.com"
plugin_url = "https://github.com/gruvin/OctoPrint-WebcamTab"
plugin_license = "AGPLv3"
plugin_requires = []
plugin_additional_data = []
plugin_additional_packages = []
plugin_ignored_packages = []
additional_setup_parameters = {}

########################################################################################################################

try:
    import octoprint_setuptools
except ImportError:
    print("Could not import OctoPrint's setuptools, are you sure you are running that under "
          "the same python installation that OctoPrint is installed under?")
    import sys
    sys.exit(-1)

setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
    identifier=plugin_identifier,
    package=plugin_package,
    name=plugin_name,
    version=plugin_version,
    description=plugin_description,
    author=plugin_author,
    mail=plugin_author_email,
    url=plugin_url,
    license=plugin_license,
    requires=plugin_requires,
    additional_packages=plugin_additional_packages,
    ignored_packages=plugin_ignored_packages,
    additional_data=plugin_additional_data
)

if len(additional_setup_parameters):
    from octoprint.util import dict_merge
    setup_parameters = dict_merge(setup_parameters, additional_setup_parameters)

setup(**setup_parameters)
