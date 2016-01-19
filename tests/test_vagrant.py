from __future__ import absolute_import

import subprocess
import os
import re
from tests.test_utils import check_tests_run_from_base_dir, \
    run, run_galahad, run_arthur, setup, complete
from distutils.version import LooseVersion

@setup
def test_start():
    """
    Check that the student is in the base directory.
    """
    assert check_tests_run_from_base_dir()

@complete
def test_virtualbox_version():
    """
    Shell out to vboxmanage to get the version of virtualbox currently installed.

    TODO: Check to see if this works on windows.
    TODO: Make this less brittle with respect to versions of virtualbox.
    """
    correct_version = LooseVersion('5.0.6')
    try:
        version = LooseVersion(run(['vboxmanage','--version']))
    except FileNotFoundError:
        assert False, "Virtualbox is not yet installed."
    assert correct_version <= version, "Your version of virtualbox is {}.\n \
        This may not work with the rest of the tutorial,\n \
        which is written for Virtualbox {}.".format(version, correct_version)

@complete
def test_vagrant_version():
    correct_version = LooseVersion('1.7.4')
    try:
        version = LooseVersion(re.search('Vagrant ([0-9.]*)\n', run(['vagrant','--version'])).group(1))
    except FileNotFoundError:
        assert False, "Vagrant is not yet installed."
    assert correct_version <= version, "Your version of vagrant is {}.\n \
        This may not work with the rest of the tutorial,\n \
        which is written for vagrant {}.".format(version, correct_version)
