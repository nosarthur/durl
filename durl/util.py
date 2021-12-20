import os
import subprocess
from glob import glob
from typing import List

# https://github.com/nosarthur/durl/blob/
#           main/LICENSE#L12
# TODO: site => sep
sep = '#L'


def grep(path:str, keyword:str) -> List[str]:
    """

    """
    p = subprocess.run(
            f"grep -rin '{keyword}' *",
            shell=True,
            text=True,
            capture_output=True,
            )
    if p.stdout:
        got = []
        for l in p.stdout.split('\n'):
            if l:
                file, lno = l.split(':')[:2]
                got.append(file + sep + lno)
        return got
    return []


def find(path:str, keyword:str) -> List[str]:
    """

    """
    os.chdir(path)
    return glob('**/' + keyword)
