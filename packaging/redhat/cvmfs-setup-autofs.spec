%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%bcond_without init_systemd
%bcond_with init_sysv
%else
%bcond_with init_systemd
%bcond_without init_sysv
%endif

Summary: Configure the CernVM File System to mount with autofs
Name: cvmfs-setup-autofs
Version: 1.0
Release: 0%{?dist}
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
Group: Applications/System
License: BSD
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:         cvmfs
Requires:         autofs
%if %{with init_systemd}
Requires(post):   systemd
Requires(postun): systemd
%endif
%if %{with init_sysv}
Requires(post):   coreutils 
Requires(post):   grep 
Requires(postun): sed
%fi

%prep
%setup

%description
Configure the CernVM File System to mount with autofs

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%endif

%post
%if %{with init_systemd}
# this is a no-op if the service is not running
/bin/systemctl try-reload-or-restart autofs.service
%endif
%if %{with init_sysv}
if /bin/grep -e '^/cvmfs[[:space:]]\+/etc/auto.cvmfs$' /etc/auto.master; then
	echo "/cvmfs	/etc/auto.cvmfs" >> /etc/auto.master
fi
%endif

%postun
%if %{with init_systemd}
# this is a no-op if the service is not running
/bin/systemctl try-reload-or-restart autofs.service
%endif
%if %{with init_sysv}
/bin/sed -i -e '\,^/cvmfs[[:space:]]\+/etc/auto.cvmfs$,d' /etc/auto.master
%endif

%files
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%dir %{_sysconfdir}/auto.master.d
%{_sysconfdir}/auto.master.d/cvmfs.autofs
%endif

%changelog
* Wed Nov 15 2017 Tom Downes <downes@uwm.edu> - 1.0-0 
-  First commit to manage autofs under /etc/auto.master.d
