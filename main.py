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
from tabulate import tabulate

# TODO: Take path from cmdline
path = "/home/malvi/Downloads/Teracube_2e_06_2020/Teracube_2e_06_20201116/MT6765_Android_scatter.txt"

partitions = parser.partition_list_generate(path)

print(warnings.aboutwarning)

# TODO: Make it functional
partitionsList = []

for case in partitions:
    partitionsList.append([case, partitions[case]])

print(tabulate(partitionsList, headers=["Partition", "Filename"], tablefmt="fancy_grid"))

# Begin flash
print("Beginning flash...")
for case in partitions:
    fastboot.flashPartition(case, partitions[case])
    print("Flashed " + case)