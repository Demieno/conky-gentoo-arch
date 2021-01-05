#!/usr/bin/python

import datetime
import re

# lastsync.py by kamed
#
# This script is designed to read current timedata update portage.
#
# if not root Usage:
# .conkyrc:     ${execi [time] echo passwd|sudo /path/to/script/lastsync.py}
#
# Usage Example
#               ${execi 30 echo passwd|sudo /home/youruser/scripts/lastsync.py}


with open('/var/log/emerge.log', 'r') as read_file:
    item_list = []
    for str_item in read_file:
        str_date = re.search('(\d*)(?::\s*===\s*)(?:Sync)', str_item)
        if str_date is not None:
            datestr = datetime.datetime.utcfromtimestamp(int(str_date.group(1))).strftime('%Y-%m-%d %H:%M:%S')
            item_list.append(datestr)
    print(item_list[-1])
