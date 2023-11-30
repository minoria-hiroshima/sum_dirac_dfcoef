from typing import List


def space_separated_parsing(line: str) -> List[str]:
    import re

    words = re.split(" +", line.rstrip("\n"))
    return [word for word in words if word != ""]


def debug_print(message: str):
    from sum_dirac_dfcoef.args import args

    # print debug message if --debug option is used
    if args.debug:
        print(message)


def is_float(parameter: str):
    if not parameter.isdecimal():
        try:
            float(parameter)
            return True
        except ValueError:
            return False
    else:
        return False
