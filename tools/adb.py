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

# This requires adb to be installed on the host

import subprocess

vendor_device = "ro.product.vendor.device"

def getDeviceCodename():
    result = subprocess.run(['adb', 'shell', 'getprop', vendor_device], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return result.strip()

def rebootToFastboot():
    result = subprocess.run(['adb', 'reboot', 'fastboot'])
    return result.strip()

def rebootToBootloader():
    result = subprocess.run(['adb', 'reboot', 'bootloader'])
    return result.strip()