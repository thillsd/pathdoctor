""""
PathDoctor
================

Finds copies of Python inside and outside of the Windows Path.
"""
import atexit
import os
import pprint
import sys
import typing as t
from dataclasses import dataclass
from pathlib import Path, WindowsPath

# todo: Windows Store
STANDARD_PYTHON_VERSION_DIRECTORY_NAMES = [
    Path(os.path.expandvars(r"%LocalAppData%")) / "Programs" / "Python",
    Path(r"C:\\"),
    Path(r"C:\\ProgramData"),  # default (ana|mini)conda global location
    Path(os.path.expandvars(r"%userprofile%")),  # default (ana|mini)conda user location
]

STANDARD_PYTHON_DIRECTORY_PREFIXES = [
    "miniconda",
    "anaconda",
    "bin",
    "Python",
]


@dataclass
class PythonInstallation:
    directory: Path
    interpreter: Path
    python_in_path: bool
    pip: t.Optional[Path] = None
    pip_in_path: bool = False
    is_default_interpreter_in_path: bool = False
    is_the_currently_running_interpreter: bool = False


PythonInstallations = t.List[PythonInstallation]


def main() -> None:
    installations = detect_python_installations()
    write_report(installations)

    user_input = input("Edit Windows Path [y/N]? ")
    if user_input in ("y", "Y"):
        # raises below vscode with no icon in taskbar :)
        os.system("rundll32 sysdm.cpl,EditEnvironmentVariables")


def detect_python_installations() -> PythonInstallations:
    path = [Path(d) for d in t.cast(str, os.getenv("path")).split(";")]

    python_installations = select_python_directories(path)
    set_pip_directories(python_installations)
    set_is_pip_in_path(path, python_installations)
    set_is_current_interpreter(python_installations)

    return sorted(
        python_installations,
        key=lambda installation: (
            installation.is_the_currently_running_interpreter,
            installation.python_in_path,
        ),
        reverse=True,
    )


def select_python_directories(path: t.Sequence[Path]) -> PythonInstallations:
    python_directories = select_python_directories_from_path(path)
    add_python_directories_from_standard_locations(python_directories)

    if python_directories and python_directories[0].python_in_path:
        # the first python.exe at the 'head' of the Path will take precedence
        python_directories[0].is_default_interpreter_in_path = True
    return python_directories


def write_report(installations: PythonInstallations) -> None:
    # monkey patch the repr for cleaner output
    old_repr = WindowsPath.__repr__
    WindowsPath.__repr__ = lambda self: f"'{self!s}'"

    for install in installations:
        pprint.pprint(install)

    WindowsPath.__repr__ = old_repr


def set_is_current_interpreter(
    python_installations: PythonInstallations,
) -> None:
    for python in python_installations:
        if python.interpreter == Path(sys.executable):
            python.is_the_currently_running_interpreter = True
            return


def set_is_pip_in_path(
    path: t.Sequence[Path], python_installations: PythonInstallations
) -> None:
    for python in python_installations:
        if not python.pip:
            continue

        pip_directory = python.pip.parent
        if pip_directory in path:
            python.pip_in_path = True


def set_pip_directories(python_installations: PythonInstallations) -> None:
    for python in python_installations:
        possible_pip_paths = (
            python.directory / "pip.exe",
            python.directory / "Scripts" / "pip.exe",
        )
        for pip in possible_pip_paths:
            if pip.exists():
                python.pip = pip


def select_python_directories_from_path(path: t.Sequence[Path]) -> PythonInstallations:
    python_directories = []

    for directory in path:
        executable_path = directory / "python.exe"
        if not executable_path.exists():
            continue

        python_directories.append(
            PythonInstallation(
                directory=directory, interpreter=executable_path, python_in_path=True
            )
        )

    return python_directories


def add_python_directories_from_standard_locations(
    python_directories: PythonInstallations,
) -> None:
    for directory in STANDARD_PYTHON_VERSION_DIRECTORY_NAMES:
        for python_directory_prefix in STANDARD_PYTHON_DIRECTORY_PREFIXES:
            for python_dir in directory.glob(f"{python_directory_prefix}*"):
                executable_path = python_dir / "python.exe"
                if not executable_path.exists():
                    continue

                if any(
                    python_dir == dir_
                    for dir_ in [python.directory for python in python_directories]
                ):
                    continue

                python_directories.append(
                    PythonInstallation(
                        directory=python_dir,
                        interpreter=executable_path,
                        python_in_path=False,
                    )
                )


@atexit.register
def on_exit():
    is_running_in_interactive_cmd = "PROMPT" in os.environ
    is_running_in_vscode = os.environ.get("TERM_PROGRAM", "") == "vscode"
    is_nuitka_exe = "__compiled__" in globals()

    if is_nuitka_exe or (
        not is_running_in_interactive_cmd and not is_running_in_vscode
    ):
        input("Press ENTER to exit...")


if __name__ == "__main__":
    main()
