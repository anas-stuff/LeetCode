import subprocess
from os import sep, mkdir, chdir

def run(command: str, path: str = None) -> bool:
    """ Run a command  utility"""
    # Go to the directory of the project if there is one
    if path:
        chdir(path)
    result = subprocess.run(command.split(' '), capture_output=True)
    print(result.stdout.decode('utf-8'))

    # Go back to the root directory of the project
    if path:
        chdir(sep.join(__file__.split(sep)[:-2]))
    
    # Print the error if there is one
    if result.stderr:
        print(f"There was an error while running the command: {command}")
        print(result.stderr.decode('utf-8'))

    return result.returncode == 0

def create_rust_project(path: str) -> None:
    """ Create a rust project """
    run(f"cargo new --vcs none --lib {path}")

def create_c_project(path: str) -> None:
    """ Create a c project """
    run(f"touch {path}/main.c")
    run(f"touch {path}/Makefile")
    run(f"touch {path}/.gitignore")

def create_python_project(path: str) -> None:
    """ Create a python project """
    run(f"touch {path}/main.py")
    with open(f"{path}/test.py", "w") as f:
        f.write("import unittest\n")
        f.write("from main import *\n\n")
        f.write("class Test(unittest.TestCase):\n")
        f.write("\t def test(self):\n")
        f.write("\t\t self.assertEqual(True, True)\n\n")
        f.write("if __name__ == '__main__':\n")
        f.write("\t unittest.main()\n")

def create_java_project(path: str) -> None:
    if not run(f"mvn archetype:generate \
    -DarchetypeGroupId=org.apache.maven.archetypes \
    -DarchetypeArtifactId=maven-archetype-quickstart \
    -DarchetypeVersion=1.4 \
    -DgroupId=com.anas.leetcode.{path.split(sep)[-2]} \
    -DartifactId={path.split(sep)[-2]} \
    -Dversion=1.0-SNAPSHOT"):
        print("Failed to create java project")
        return

def create_cpp_project(path: str) -> None:
    with open(f"{path}/main.cpp", "w") as f:
        f.write("#include <iostream>\n\n")
        f.write("using namespace std;\n\n")
    
    with open(f"{path}/test.cpp", "w") as f:
        f.write("#include <catch2/catch.hpp>\n")
        f.write("#include \"main.cpp\"\n\n")

    with open(f"{path}/Makefile", "w") as f:
        f.write("all: main.cpp test.cpp\n")
        f.write("\t g++ -o main main.cpp\n")
        f.write("\t g++ -o test test.cpp -I /usr/local/include -L /usr/local/lib -lcatch2\n")
        f.write("\t ./test\n")

def create_go_project(path: str) -> None:
    if run(f"go mod init letcode/{path.split(sep)[-2]}", path):
        mkdir(f"{path}/src")
        with open(f"{path}/src/main.go", "w") as f:
            f.write("package main\n\n")
            f.write("import \"fmt\"\n\n")
            f.write("func main() {\n")
            f.write("\t fmt.Println(\"Hello, World!\")\n")
            f.write("}\n")
    
        with open(f"{path}/src/_test.go", "w") as f:
            f.write("package main\n\n")
            f.write("import \"testing\"\n\n")
            f.write("func TestHello(t *testing.T) {\n")
            f.write("\t fmt.Println(\"Hello, World!\")\n")
            f.write("}\n")

