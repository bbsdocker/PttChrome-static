#!/usr/bin/env python3

import sys
import os
import re

the_host = sys.argv[1]

_TO_REPLACE = r'wstelnet://localhost:48763/bbs'


def _update_host(filename):
    with open(filename, 'r') as f:
        content = f.read()

    to_replace = 'wstelnet://' + the_host + '/bbs'
    content = re.sub(_TO_REPLACE, to_replace, content)
    with open(filename, 'w') as f:
        f.write(content)


for root, the_dirs, the_filenames in os.walk('assets'):
    if root != 'assets':
        continue

    valid_filenames = list(filter(lambda x: x.endswith('.js'), the_filenames))

    [_update_host(os.sep.join([root, each])) for each in valid_filenames]
