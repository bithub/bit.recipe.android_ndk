import logging
import os
import shutil
import pkg_resources
import commands

class Recipe:
    def __init__(self, buildout, name, options):
        self.options = options
        self.logger = logging.getLogger(name)
        self.name = name

    def _update(self):
        install = pkg_resources.resource_filename(__name__, 'install_android_ndk')
        path = os.getcwd()
        target_install = os.path.join(path,'bin',self.name)
        revision = 'r7'
        part = os.path.join(path,'parts',self.name)
        if os.path.exists(target_install):
            os.unlink(target_install)
        open(target_install,'w').write('#/bin/bash\nBUILDOUT=%s\nNDK=%s\nPARTNAME=%s\n' %(path,self.options['ndk'],self.name)+open(install).read())
        commands.getoutput('chmod +x %s' %target_install)
        #open(os.path.join('bin', self.name),'w').write('BUILDOUT=%s\nexport ANDROIDNDKVER=%s\nexport ANDROIDNDK=%s\nexport PATH=$ANDROIDNDK:$PATH'%(path,revision,part))

    def install(self):
        self._update()
        return ['bin/%s' %self.name]

    def update(self):
        self._update()
        #print commands.getoutput('./bin/%s ' %self.name)
