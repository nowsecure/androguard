import unittest

import sys
PATH_INSTALL = "./"
sys.path.append(PATH_INSTALL)

from androguard.core.bytecodes import apk

APKS = [
  "examples/NowSecure/com.kaspersky.kes.apk",
  "examples/NowSecure/com.king.bubblewitch3_119351.apk",
]

class APKTest(unittest.TestCase):

    def testAPK(self):
        for apk_path in APKS:
            with open(apk_path, "r") as fd:
                a = apk.APK(fd.read(), True)
                self.assertTrue(a)


if __name__ == '__main__':
    unittest.main()
