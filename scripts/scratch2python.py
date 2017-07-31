#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__copyright__ = "JdeRobot project"
__credits__ = ["Raul Perula-Martinez"]
__license__ = "GPL v3"
__version__ = "0.0.0"
__maintainer__ = "Raul Perula-Martinez"
__email__ = "raules@gmail.com"
__status__ = "Development"

import kurt
import os
import re
import sys

from difflib import SequenceMatcher
from parse import parse, compile


GENERAL = [
    ['end', ''],
    ['forever', 'while True:'],
    ['if', 'if %s:'],
    ['repeat', 'for i in range(%s):'],
    ['say', 'print(%s)'],
    ['wait {} secs', 'time.sleep(%s)'],
    ['while', 'while %s:'],
]

ROBOTICS = [
    ['move robot {}', 'robot.move("%s")'],
    ['move robot {} speed {}', 'robot.move("%s", %s)'],
    ['stop robot', 'robot.stop()'],
    ['turn robot {}', 'robot.turn("%s")'],
    ['turn robot {} speed {}', 'robot.turn("%s", %s)'],
]

MAPPING = GENERAL + ROBOTICS


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


if __name__ == "__main__":
    # get current working directory
    path = os.getcwd()
    open_path = path[:path.rfind('scripts')] + 'data/'
    save_path = path[:path.rfind('scripts')] + 'src/scratch2robot/'

    if len(sys.argv) == 2:
        # template creation
        template = "\
#!/usr/bin/env python\n\
# -*- coding: utf-8 -*-\n\n\
import time\n\n\
def execute(robot):\n\
\ttry:\n\
\t\t%s\
except KeyboardInterrupt:\n\
\t\traise\n\
"

        # load the scratch project
        p = kurt.Project.load(open_path + sys.argv[1])

        # show the blocks included
        for scriptable in p.sprites + [p.stage]:
            for script in scriptable.scripts:
                if "define" not in script.blocks[0].stringify():
                    s = script

        print "Script:"
        print s
        print

        print
        print "Stringify:"
        for b in s.blocks:
            print b.stringify()
            sentences = b.stringify().split('\n')
        print

        print
        print "List:"
        print sentences
        print

        tab_seq = "\t"
        python_program = ""

        for s in sentences:
            # count number of tabs
            num_tabs = s.replace('    ', tab_seq).count(tab_seq)

            if num_tabs > 0:
                python_program += tab_seq * (num_tabs + 1)

            # mapping
            l = [(m[0], m[1], similar(s, m[0])) for m in MAPPING]
            map0 = max(l, key=lambda item: item[2])[0]
            map1 = max(l, key=lambda item: item[2])[1]

            # extract arguments
            p = compile(map0)
            args = p.parse(s.replace('    ', ''))

            python_program += map1 % args.fixed

            python_program += "\n" + tab_seq

        file_text = template % python_program
        file_text = file_text.replace(tab_seq, ' ' * 4)

        print "\n-------------------"
        print file_text
        print "-------------------\n"

        f = open(save_path + "scratch.py", "w")
        f.write(file_text)
        f.close()

    else:
        print "ERROR: Number of parameters incorrect. Example:\n\tpython scratch2python.py hello_world.sb2"
