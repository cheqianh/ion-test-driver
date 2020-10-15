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

import os

from tests.util import run_ion_test_driver, compare_two_files

TEST_FILE_NAME = 'res_diff_tests'
TEST_FILE_PATH = os.path.join(os.path.split(os.path.abspath(__file__))[0], TEST_FILE_NAME)
EXPECT_FILE_NAME = 'res_diff_expect'
EXPECT_FILE_PATH = os.path.join(os.path.split(os.path.abspath(__file__))[0], EXPECT_FILE_NAME)


# Empty report.
def test_empty_report():
    test_file = 'test_empty_report.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Both results are pass.
def test_result_both_pass():
    test_file = 'test_result_both_pass.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# One revision PASS but the other one FAIL.
def test_diff_results():
    test_file = 'test_diff_results.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Both of the results fail, it should go to the next phase of the same file rather than go to the next file immediately.
def test_result_both_fail():
    test_file = 'test_result_both_fail.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Old revision has a read_error but the new one doesn't, it shouldn't alert user.
def test_fix_read_errors():
    test_file = 'test_fix_read_errors.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Old revision doesn't have read_error but the new one create one, it should alert user.
def test_new_read_errors():
    test_file = 'test_new_read_errors.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Both revisions raise an read error, but the errors are different.
def test_diff_read_errors():
    test_file = 'test_diff_read_errors.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# New commit fixes read_compare_errors, it shouldn't alert user.
def test_fix_read_compare_errors():
    test_file = 'test_fix_read_compare_errors.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# New commit causes read_compare_errors, it should alert user.
def test_new_read_compare_errors():
    test_file = 'test_new_read_compare_errors.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Both revisions have read_compare_errors, but the errors are different.
def test_diff_read_compare_errors():
    test_file = 'test_diff_read_compare_errors.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Both revisions have read-Compare_failures, but the failures are different.
def test_diff_read_compare_failures():
    test_file = 'test_diff_read_compare_failures.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Two revisions agree with each other for read behavior.
def test_read_agree():
    test_file = 'test_read_agree.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Two revisions agree with each other but they have different disagree list, it should be a cli issue.
def test_revisions_with_diff_list():
    test_file = 'test_revisions_with_diff_list.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Two revisions have different disagree lists for read behavior.
def test_read_disagree():
    test_file = 'test_read_disagree.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# New commit fixes write_errors.
def test_fix_write_errors():
    test_file = 'test_fix_write_errors.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# New commit causes write_errors.
def test_new_write_errors():
    test_file = 'test_new_write_errors.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Both revisions have write_errors, but the errors are different.
def test_diff_write_errors():
    test_file = 'test_diff_write_errors.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# New revision fixes write_compare_errors.
def test_fix_write_compare_errors():
    test_file = 'test_fix_write_compare_errors.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# New revision causes write_compare_errors.
def test_new_write_compare_errors():
    test_file = 'test_new_write_compare_errors.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Both revisions have errors, but the errors are different.
def test_diff_write_compare_errors():
    test_file = 'test_diff_write_compare_errors.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Both revisions have failures, but the failures are different.
def test_diff_write_compare_failures():
    test_file = 'test_diff_write_compare_failures.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Two revisions agree with each other for write behavior.
def test_write_agree():
    test_file = 'test_write_agree.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# Two revisions disagree with each other for write behavior.
def test_write_disagree():
    test_file = 'test_write_disagree.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True


# complex report that includes multiple errors.
def test_complex_report():
    test_file = 'test_complex_report.ion'
    output_path = run_ion_test_driver(os.path.join(TEST_FILE_PATH, test_file), 'ion-java,1', 'ion-java,2')
    res = compare_two_files(output_path, os.path.join(EXPECT_FILE_PATH, test_file))
    os.remove(output_path)
    assert res is True









