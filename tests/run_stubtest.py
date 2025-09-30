import site
import sys

site.addsitedir(sys.argv[1])

from mypy.stubtest import test_stubs, parse_options

exit_code = test_stubs(parse_options(["fontforge", "psMat", "--ignore-missing-stub"]))
sys.exit(exit_code)
