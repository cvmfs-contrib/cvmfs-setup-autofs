%global autofs_map_entry "/cvmfs	/etc/auto.cvmfs"
%global autofs_map_entry_regex ^[[:space:]]*/cvmfs[[:space:]]+/etc/auto.cvmfs[[:space:]]*
%define is_fedora_auto_master_d %(test 0%{?fedora} -ne 0 && test %{?fedora} -ge 15 && echo 1 || echo 0)
%define is_rhel_auto_master_d %(test 0%{?rhel} -ne 0 && test %{?rhel} -ge 7 && echo 1 || echo 0)
%define is_centos_auto_master_d %(test 0%{?centos} -ne 0 && test %{?centos} -ge 7 && echo 1 || echo 0)
%define is_auto_master_d %( test %{is_rhel_auto_master_d} -eq 1 || test %{is_centos_auto_master_d} = 1 || test %{is_fedora_auto_master_d} = 1 && echo 1 || echo 0)

Summary:        Configure the CernVM File System to mount with autofs
Name:           cvmfs-setup-autofs
Version:        1
%define         release_prefix 1
Release:        %{release_prefix}%{?dist}
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
Group:          Applications/System
License:        BSD
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  coreutils
Requires:       cvmfs
Requires:       autofs
Requires(post): grep

%if %{is_auto_master_d}
Requires(post): sed
%endif

%if ! %{is_auto_master_d}
Requires(postun): sed
%endif

%prep
%setup

%description
Configure the CernVM File System to mount with autofs

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%if %{is_auto_master_d}
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/auto.master.d
ln -sf %{_datarootdir}/%{name}/cvmfs.autofs ${RPM_BUILD_ROOT}/%{_sysconfdir}/auto.master.d/cvmfs.autofs
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
%if %{is_auto_master_d}
if grep -qEe %{autofs_map_entry_regex} /etc/auto.master; then
	sed -i -r -e '\,%{autofs_map_entry_regex},d' /etc/auto.master
fi
%else
if ! grep -qEe %{autofs_map_entry_regex} /etc/auto.master; then
	echo %{autofs_map_entry} >> /etc/auto.master
fi
%endif

%if ! %{is_auto_master_d}
%postun
sed -i -r -e '\,%{autofs_map_entry_regex},d' /etc/auto.master
%endif

%files
%if %{is_auto_master_d}
%{_datarootdir}/%{name}
%dir %{_sysconfdir}/auto.master.d
%{_sysconfdir}/auto.master.d/cvmfs.autofs
%else
%exclude %{_datarootdir}/%{name}
%endif

%changelog
* Wed Nov 15 2017 Tom Downes <downes@uwm.edu> - 1.0-0
-  First commit to manage autofs under /etc/auto.master.d
