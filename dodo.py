DOIT_CONFIG = {
    "default_tasks": [""],
    "backend": "sqlite3",
    "verbosity": 2
}


def task_build():
    return {
        "actions": [
            r"python -m nuitka --onefile .\\pathdoctor\\pathdoctor.py --output-dir=nuitka-build"
        ]
    }


def task_format():
    return {
        "actions": [
            r"black .\\pathdoctor\\pathdoctor.py",
            r"isort .\\pathdoctor\\pathdoctor.py"
        ],
        "verbosity": 2,
    }
