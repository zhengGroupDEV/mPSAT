"""
Description: build script, using nuitka
Author: Rainyl
LastEditTime: 2022-08-04 17:33:48
"""
from argparse import ArgumentParser
import os
import shutil

CPUS = os.cpu_count()

def main(version: str = "0.1", enable_debug=False, jobs=CPUS):
    std_out = "--force-stdout-spec=mpsat_out.log "
    std_err = "--force-stderr-spec=mpsat_error.log "
    disable_console = "--windows-disable-console "
    build_dir = "build"
    debug = ""
    if enable_debug:
        disable_console = ""
        build_dir = "build_debug"
        std_out = ""
        std_err = ""
        # debug = "--debug "
    cmd = (
        "nuitka "
        "--clang "
        # "--mingw64 "
        # "--recompile-c-only "
        "--standalone "
        f"{debug}"
        f"--output-dir={build_dir} "
        "--follow-imports "
        f"--no-follow-import-to=tk"
        f"{disable_console}"
        f"{std_out}"
        f"{std_err}"
        f"--jobs={jobs} "
        "--windows-file-description=mPAST "
        "--windows-company-name=zhengGroup@LZU "
        f"--windows-product-version={version} "
        f"""--windows-product-name="mPAST_v{version}" """
        # "--show-progress "
        # "--show-memory  "
        "--plugin-enable=pyside6 "
        "--plugin-enable=numpy "
        # "--plugin-enable=matplotlib "
        # "--plugin-enable=multiprocessing "
        # "--plugin-enable=upx "
        "--windows-icon-from-ico=theme/mpsat-logo.ico "
        "./mPSAT/mpsat.py "
    )

    os.system(cmd)

    # shutil.copytree("config/", f"{build_dir}/mpsat.dist/config/")
    shutil.copy(
        "depends/onnxruntime_providers_shared.dll",
        f"{build_dir}/mpsat.dist/onnxruntime/capi/",
    )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-v", dest="version", type=str, default="0.1")
    parser.add_argument("--debug", dest="debug", action="store_true", help="enable build for debug")
    parser.add_argument("-j", dest="jobs", type=int, default=CPUS)
    args = parser.parse_args()
    main(version=args.version, enable_debug=args.debug, jobs=args.jobs)
