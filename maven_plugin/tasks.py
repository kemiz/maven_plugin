from cloudify.decorators import operation

MVN_PACKAGE = 'package'
__author__ = 'kemi'

import tempfile
from package_installer_plugin.utils import run, unzip, download_file


# def package(module_source_zip_path, app_name, **_):
#     """
#     Downloads application source as zip and uses maven to
#     build and package a deployable WAR file
#     """
#
#     unzip(module_source_zip_path, '/tmp')
#     _run_maven_command('/tmp/{0}/pom.xml'.format(app_name), MVN_PACKAGE)
#     return '/tmp/{0}/target/{0}.war'.format(app_name)
#
#
# def _run_maven_command(pom_xml, mvn_operation):
#     package_command = 'mvn -f {0} {1}'.format(pom_xml, mvn_operation)
#     # ctx.logger.info('Executing maven operation: ' + package_command)
#     run(package_command)