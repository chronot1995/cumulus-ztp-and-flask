from flask import Flask
from flask import request
import subprocess
import shlex
import sys

app = Flask(__name__)


@app.route('/Provision/<switchname>', methods=['POST'])
def ztp_switch(switchname):
    command = "ansible-playbook deploy-switches.yml -l %s" % switchname
    try:
        process = subprocess.Popen(
            shlex.split(command), stdout=subprocess.PIPE)
    except:
        print("ERROR {} while running {}".format(sys.exc_info()[1], command))
        return None
    while True:
        output = process.stdout.readline()
        if process.poll() is not None:
            break
        if output:
            print(output.strip().decode())
    output, err = process.communicate()
    return output


if __name__ == "__main__":
    app.run()
