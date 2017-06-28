#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kurt
import os
import re
import sys

MAPPING = [
    ['end', ''],
    ['move', 'robot.move()'],
    ['repeat', 'for i in range(%s):'],
    ['say', 'print(%s)'],
    ['stop', 'robot.stop()'],
    ['wait', 'rospy.sleep(int("%s".replace(" secs", "")))'],
]

# get current working directory
path = os.getcwd()
open_path = path[:path.rfind('scripts')] + 'data/'
save_path = path[:path.rfind('scripts')] + 'src/scratch2ros/'

if len(sys.argv) == 2:
    # template creation
    template = "\
#!/usr/bin/env python\n\
# -*- coding: utf-8 -*-\n\n\
import rospy\n\n\
def execute(robot):\n\
"

    # load the scratch project
    p = kurt.Project.load(open_path + sys.argv[1])

    # show the blocks included
    for scriptable in p.sprites + [p.stage]:
        for script in scriptable.scripts:
            s = script

    print s
    print

    for b in s.blocks:
        print b.stringify()
        sentences = b.stringify().split('\n')

    print sentences
    print

    tab_seq = "\t"
    python_program = "\t"

    for s in sentences:
        aux = s.replace('    ', tab_seq).split(' ', 1)
        for m in MAPPING:
            if m[0] in aux[0]:
                print m[0], aux[0]
                python_program += tab_seq * aux[0].count(tab_seq)
                if len(aux) > 1:
                    python_program += m[1] % aux[1]
                else:
                    python_program += m[1]
        python_program += "\n" + tab_seq

    file_text = template + python_program

    print "-------------------"
    print file_text
    print "-------------------"

    f = open(save_path + "scratch.py", "w")
    f.write(file_text)
    f.close()

else:
    print "ERROR: Number of parameters incorrect. Example:\n\tpython scratch2python.py hello_world.sb2"
