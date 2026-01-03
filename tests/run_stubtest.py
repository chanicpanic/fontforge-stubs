import site
import sys

from pathlib import Path

site.addsitedir(sys.argv[1])

from mypy.stubtest import test_stubs, parse_options

allowlists = sys.argv[2:]
options = ["fontforge", "psMat", "--ignore-unused-allowlist"]
for allowlist in allowlists:
    options.append("--allowlist")
    options.append(str(Path(__file__).parent.joinpath("allowlists", allowlist)))

exit_code = test_stubs(parse_options(options))
sys.exit(exit_code)
