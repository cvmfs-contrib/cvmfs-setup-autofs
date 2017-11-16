# cvmfs-setup-autofs
RedHat and Debian Packages that configure the CernVM File System to mount with autofs

## RHEL7+ and Debian 8+
On these systems, the package will install a file under /etc/auto.master.d that automatically
configures autofs.

## RHEL6
RHEL6-based systems are not aware of /etc/auto.master.d. On these systems, the script
automatically edits `/etc/auto.master` at installation and removal.

## Building
Build scripts are available for Debian and RedHat systems in the `packaging` directory.
