from asyncio import subprocess
from subprocess import SubprocessError
from templateframework.runner import run
from templateframework.template import Template
from templateframework.metadata import Metadata
import subprocess

class RestTemplate(Template):

        def pre_hook(self, metadata: Metadata) -> Metadata:
            print("Project will be created at: " + str(metadata.target_path))
            return metadata

        def post_hook(self,metadata:Metadata):
            subprocess.run('sudo npx -p @angular/cli@12.x ng new beagle-angular-app --directory ./beagle-app-angular', shell=True, cwd=metadata.target_path)
            subprocess.run('sudo npm install @zup-it/beagle-angular --save', shell=True, cwd=str(metadata.target_path)+"/beagle-app-angular")
            subprocess.run('sudo npx beagle init', shell=True, cwd=str(metadata.target_path)+"/beagle-app-angular")
            print('Your Beagle Angular project is ready, navigate to ' + str(metadata.target_path) + ' to run it')
            return metadata

if __name__ == '__main__':
    run(RestTemplate())