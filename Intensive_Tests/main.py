
import os
import sys


sys.path.append(os.getcwd())
import SystemPath

from Intensive_Tests.smoke_tests.flows.full_smoke.main import FullSmokeTests

FullSmokeTests().start()
