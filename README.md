# cvmfs-setup-autofs
RedHat and Debian Packages that configure the CernVM File System to mount with autofs

## Debian 8+
The package will install a file under /etc/auto.master.d that appropriately
configures autofs. After installation and removal it will issue
`systemctl reload autofs.service` to cause autofs to reload its mount maps.

## RHEL7
The package will install a file under /etc/auto.master.d that appropriately
configures autofs. The administrator must run `systemctl reload autofs.service`
to cause autofs to reload its mount maps.

## RHEL6
RHEL6-based systems are not aware of /etc/auto.master.d. On these systems, the script
automatically edits `/etc/auto.master` at installation and removal.

## Building
Build scripts are available for Debian and RedHat systems in the `packaging` directory.
