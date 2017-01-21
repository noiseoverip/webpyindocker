import stat
import os
import subprocess

def create_script_file(script_name, script_code):
    """Create executable python file by using pre-exisinting template and injecting provided code"""
    script_code = read_template().replace("#{{ USER_CODE }}", script_code)
    file_name = "runtime/script-%s.py" % script_name
    with open(file_name, "w") as pyfile:
        pyfile.write("%s" % script_code)
    st = os.stat(file_name)
    # Make file executable
    os.chmod(file_name, st.st_mode | stat.S_IEXEC)
    return file_name


def read_template():
    """ Read template contents into var"""
    with open("pyexec/script_wrapper.py") as f:
        return f.read()


def execute_file(file_name):
    """Execute given python file in docker container"""
    print("executing %s" % file_name)
    print(cli("pwd"))
    return cli("./pyexec/run_in_docker.sh %s" % file_name)


def cli(line):
    """ Execute given cli command"""
    print("Running command %s" % line)
    response = subprocess.check_output(line.split(" ")).decode('utf-8')
    print("Response %s " % response)
    return response