#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="""Generate a version header file with static values.
This script is a modified version to work without Git.""")
parser.add_argument('filename', metavar='version.h', help='Header output file')
parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
                    help='Verbose output', default=False)

args = parser.parse_args()
filename = args.filename
verbose = args.verbose

# Static values
git_tag = "v1.13.2"
git_version = "46a12a09bf11c8cbafc5ad905996645b4fe1a9df"
git_version_short = git_version[:16]
git_branch_name = "main"
oem_tag = ""
tag_or_branch = "v1.13.2"

# Generate the header content
header = f"""
/* Auto Magically Generated file */
/* Do not edit! */
#pragma once

#define PX4_GIT_VERSION_STR "{git_version}"
#define PX4_GIT_VERSION_BINARY 0x{git_version_short}
#define PX4_GIT_TAG_STR "{git_tag}"
#define PX4_GIT_BRANCH_NAME "{git_branch_name}"

#define PX4_GIT_OEM_VERSION_STR  "{oem_tag}"

#define PX4_GIT_TAG_OR_BRANCH_NAME "{tag_or_branch}" // special variable: git tag, release or master branch
"""

# ECL
ecl_git_version = "ecl_fake_version"
ecl_git_version_short = ecl_git_version[:16]
header += f"""
#define ECL_LIB_GIT_VERSION_STR  "{ecl_git_version}"
#define ECL_LIB_GIT_VERSION_BINARY 0x{ecl_git_version_short}
"""

# MAVLink
mavlink_git_version = "mavlink_fake_version"
mavlink_git_version_short = mavlink_git_version[:16]
header += f"""
#define MAVLINK_LIB_GIT_VERSION_STR  "{mavlink_git_version}"
#define MAVLINK_LIB_GIT_VERSION_BINARY 0x{mavlink_git_version_short}
"""

# NuttX
nuttx_git_version = "nuttx_fake_version"
nuttx_git_version_short = nuttx_git_version[:16]
nuttx_git_tag = "v11.0.0"
header += f"""
#define NUTTX_GIT_VERSION_STR  "{nuttx_git_version}"
#define NUTTX_GIT_VERSION_BINARY 0x{nuttx_git_version_short}
#define NUTTX_GIT_TAG_STR  "{nuttx_git_tag}"
"""

# Write to the file if content has changed
try:
    with open(filename, 'r') as fp_header:
        old_header = fp_header.read()
except FileNotFoundError:
    old_header = ""

if old_header != header:
    if verbose:
        print(f"Updating header {filename}")
    with open(filename, 'w') as fp_header:
        fp_header.write(header)

