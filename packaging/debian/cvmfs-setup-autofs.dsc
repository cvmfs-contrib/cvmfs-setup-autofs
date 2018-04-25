# created by obsupdate.sh, do not edit by hand
Debtransform-Tar: cvmfs-setup-autofs-1.0.tar.gz
Format: 1.0
Version: 1.0-0
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
Description: Configure the CernVM File System to mount with autofs
  This empty package uses postinst and postrm scripts to manage an autofs
  configuration file under /etc
Files:
  ffffffffffffffffffffffffffffffff 99999 file1
  ffffffffffffffffffffffffffffffff 99999 file2
