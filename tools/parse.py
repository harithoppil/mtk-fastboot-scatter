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

# Parse MTK scatterfile and generate a list of partitions

import yaml

def parse_scatter(path):
    with open(path, "r") as f:
        try:
            scatter_dict = yaml.safe_load(f)
            return scatter_dict
        except yaml.YAMLError as exc:
            print(exc)

def partition_list_generate(path):
    partitions = {}
    scatter_dict = parse_scatter(path)
    scatter_dict.pop(0)
    for obj in scatter_dict:
        if (obj['is_download'] == True):
            partitions.update({obj['partition_name']: obj['file_name']})
    return partitions