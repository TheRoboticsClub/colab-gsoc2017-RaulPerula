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

MAPPING = [
    ['end', ''],
    ['if', 'if %s:'],
    ['move', 'robot.move(%s)'],
    ['move', 'robot.move()'],
    ['repeat', 'for i in range(%s):'],
    ['say', 'print(%s)'],
    ['stop', 'robot.stop()'],
    ['turn', 'robot.turn(%s)'],
    ['turn', 'robot.turn()'],
    ['wait', 'time.sleep(int("%s".replace(" secs", "")))'],
    ['while', 'while %s:'],
    ['forever', 'while True:'],
]

# get current working directory
path = os.getcwd()
open_path = path[:path.rfind('scripts')] + 'data/'
save_path = path[:path.rfind('scripts')] + 'src/scratch2robot/'

if len(sys.argv) == 2:
    # template creation
    template = "\
#!/usr/bin/env python\n\
# -*- coding: utf-8 -*-\n\n\
import sys\n\
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
        aux = s.replace('    ', tab_seq).split(' ', 1)
        print aux
        for m in MAPPING:
            if m[0] in aux[0]:
                num_tabs = aux[0].count(tab_seq)
                if num_tabs > 0:
                    python_program += tab_seq * (num_tabs + 1)
                
                # parse with params
                try:
                    python_program += m[1] % aux[1]
                except TypeError:
                    pass
                except:
                    python_program += m[1]

        python_program += "\n" + tab_seq

    file_text = template % python_program
    file_text = file_text.replace(tab_seq, ' ' * 4)

    print "-------------------"
    print file_text
    print "-------------------"

    f = open(save_path + "scratch.py", "w")
    f.write(file_text)
    f.close()

else:
    print "ERROR: Number of parameters incorrect. Example:\n\tpython scratch2python.py hello_world.sb2"
