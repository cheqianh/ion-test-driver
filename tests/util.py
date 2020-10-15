# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at:
#
#    http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the
# License.
import filecmp
import os
import sys
from subprocess import Popen, PIPE

ION_TEST_DRIVER_PATH = os.path.join(os.path.split(os.path.abspath(__file__))[0], '..', 'amazon', 'iontest', 'ion_test_driver.py')

COMMAND_SHELL = False
if sys.platform.startswith('win'):
    COMMAND_SHELL = True  # shell=True on Windows allows the .exe suffix to be omitted.


def run_ion_test_driver(test_file, first_desc, second_desc):
    dir_name, file = os.path.split(test_file)
    output_name = os.path.join(dir_name, 'test_' + file)
    _, stderr = Popen(('python3', ION_TEST_DRIVER_PATH, '-R', first_desc, second_desc, test_file, '-o', output_name),
                      stderr=PIPE, shell=COMMAND_SHELL).communicate()
    return output_name


def compare_two_files(first_file, second_file):
    return filecmp.cmp(first_file, second_file, shallow=False)


