# pyside6-uic -o  src/mpsatUI.py mpsat.ui

# pyside6-rcc -o  mpsat_rc.py mpsat.qrc

import os
import re
from argparse import ArgumentParser

CMD1 = """pyside6-uic -o """
CMD2 = """pyside6-rcc -o """

def main(uic_src: str, uic_dst: str, rcc_src: str, rcc_dst:str):
    if any([not uic_src, not uic_dst, not rcc_src, not rcc_dst]):
        raise ValueError("path error")
    os.system(f"{CMD1} {uic_dst} {uic_src}")

    os.system(f"{CMD2} {rcc_dst} {rcc_src}")

    with open(uic_dst, "r") as f:
        uic_dst_str: str = f.read()
    toolbars = re.findall(r"NavigationToolbar2QT\(.+\)", uic_dst_str)
    msg = f"find {len(toolbars)} NavigationToolbar2QT object, replacing..."
    print(msg)
    for tb in toolbars:
        uic_dst_str = uic_dst_str.replace(tb, tb.replace(")", ", self)"))
    with open(uic_dst, "w") as f:
        f.write(uic_dst_str)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-us", dest="uic_src", type=str, default="theme/mpsat.ui")
    parser.add_argument("-ud", dest="uic_dst", type=str, default="mPSAT/mpsatUI.py")
    parser.add_argument("-rs", dest="rcc_src", type=str, default="theme/mpsat.qrc")
    parser.add_argument("-rd", dest="rcc_dst", type=str, default="mpsat_rc.py")
    args = parser.parse_args()
    main(args.uic_src, args.uic_dst, args.rcc_src, args.rcc_dst)
