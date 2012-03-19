import logging
import os
import pkg_resources
import commands


class Recipe:

    def __init__(self, buildout, name, options):
        self.options = options
        self.logger = logging.getLogger(name)
        self.name = name

    def _update(self):
        install = pkg_resources.resource_filename(
            __name__, 'install_android_ndk')
        path = os.getcwd()
        target_install = os.path.join(path, 'bin', self.name)
        if os.path.exists(target_install):
            os.unlink(target_install)
        env_vars = {'BUILDOUT': path,
                    'NDK': self.options['ndk'],
                    'PARTNAME': self.name,
                    }
        bash = '#/bin/bash\n'
        bash += '\n'.join(['%s=%s' % (k, v)
                          for k, v in env_vars.items()])
        open(target_install, 'w').write(bash + open(install).read())
        commands.getoutput('chmod +x %s' % target_install)

    def install(self):
        self._update()
        return ['bin/%s' % self.name]

    def update(self):
        self._update()
