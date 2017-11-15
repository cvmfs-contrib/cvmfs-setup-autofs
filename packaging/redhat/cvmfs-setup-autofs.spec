Summary: Configure the CernVM File System to mount with autofs
Name: cvmfs-setup-autofs
Version: 1.0
Release: 0%{?dist}
# download with:
# $ curl -L -o cvmfs-setup-autofs-%{version}.tar.gz \
#   https://github.com/opensciencegrid/cvmfs-setup-autofs/archive/v%{version}.tar.gz
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
Group: Applications/System
License: BSD
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%prep
%setup

%description
Configure the CernVM File System to mount with autofs

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%dir %{_sysconfdir}/auto.master.d
%{_sysconfdir}/auto.master.d/cvmfs.autofs

%changelog
* Wed Nov 15 2017 Tom Downes <downes@uwm.edu> - 1.0-0 
-  First commit to manage autofs under /etc/auto.master.d
