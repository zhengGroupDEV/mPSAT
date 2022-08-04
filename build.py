"""
Description: build script, using nuitka
Author: Rainyl
LastEditTime: 2022-08-04 17:33:48
"""
from argparse import ArgumentParser
import os


def main(version: str = "0.1"):
    cmd = (
        "nuitka "
        "--clang "
        # "--mingw64 "
        # "--recompile-c-only "
        "--standalone "
        "--output-dir=build "
        "--follow-imports "
        "--windows-disable-console "
        "--force-stdout-spec=mpsat_out.log "
        "--force-stderr-spec=mpsat_error.txt "
        "--windows-file-description=mPAST "
        "--windows-company-name=zhengGroup@LZU "
        f"--windows-product-version={version} "
        # "--windows-product-name=mPAST "
        # "--show-progress "
        # "--show-memory  "
        "--plugin-enable=pyside6 "
        "--plugin-enable=numpy "
        "--windows-icon-from-ico=theme/mpsat-logo.ico "
        "./mPSAT/mpsat.py"
    )

    os.system(cmd)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-v", dest="version", type=str, default="0.1")
    args = parser.parse_args()
    main(version=args.version)
