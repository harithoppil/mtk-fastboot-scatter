#
# Copyright (C) 2022 Gagan Malvi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

import tools.parse as parser
import tools.fastboot as fastboot
import tools.adb as adb
import tools.warnings as warnings
import sys
from tabulate import tabulate

def flash(path):
    print("[-] Generating partition table...")
    partitions = parser.partition_list_generate(path)

    print(warnings.aboutwarning)

    partitionsList = []
    for case in partitions:
        partitionsList.append([case, partitions[case]])

    print(tabulate(partitionsList, headers = ['Partition', 'Image'], tablefmt = "fancy_grid"))

    print("[-] Flashing images...")
    for case in partitions:
        fastboot.flashPartition(case, partitions[case])
        print("[*] Flashed " + case + " successfully.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        flash(sys.argv[1])
    else:
        print("[-] Please provide a path to the scatter file in the SP Flash package.")