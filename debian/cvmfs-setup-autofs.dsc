# created by ../../ci/obsupdate.sh, do not edit by hand
Debtransform-Tar: cvmfs-setup-autofs-1.tar.gz
Format: 1.0
Version: 1.1-1
Binary: cvmfs-setup-autofs
Source: cvmfs-setup-autofs
Maintainer: Dave Dykstra <dwd@fnal.gov>
Section: utils
Priority: extra
Standards-Version: 3.9.6
Build-Depends: debhelper (>= 9), dh-systemd
Homepage: https://github.com/cvmfs-contrib/cvmfs-setup-autofs

Package: cvmfs-setup-autofs
Architecture: all
Depends: ${misc:Depends}, cvmfs, autofs (>= 5.1.2)
Description: Configure the CernVM File System to mount with autofs
 The CernVM File System is a client for accessing remote file systems
 using HTTP(S). This package provides the configuration to ensure that
 CVMFS filesystems are mounted automatically with autofs.
Files:
  ffffffffffffffffffffffffffffffff 99999 file1
  ffffffffffffffffffffffffffffffff 99999 file2
