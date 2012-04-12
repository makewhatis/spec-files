#
# spec file for package libgit2
#
# Copyright (c) 2011, Sascha Peilicke <saschpe@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           libgit2
Version:        0.16.0
Release:        1.6
License:        GPL-2.0 with linking
Summary:        C git library
Url:            http://libgit2.github.com/
Group:          Development/Libraries/C and C++
Source0:        https://github.com/downloads/libgit2/libgit2/libgit2-%{version}.tar.gz
Patch0:			patch.libgit2.pc.in
BuildRequires:  cmake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  openssl-devel

%define debuginfo_args

%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing
you to write native speed custom Git applications in any language
with bindings.

%package -n %{name}-0
Summary:        C git library
Group:          System/Libraries

%description -n %{name}-0
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing
you to write native speed custom Git applications in any language
with bindings.

%package devel
Summary:        C git library
Group:          Development/Libraries/C and C++
Requires:       %{name}-0 >= %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libgit2.

%prep
%setup -q
%patch0 

%build
cmake . \
    -DCMAKE_C_FLAGS:STRING="%{optflags}" \
    -DCMAKE_INSTALL_PREFIX:PATH=$RPM_BUILD_ROOT/%{_prefix} \
    -DINSTALL_LIB:PATH=$RPM_BUILD_ROOT/%{_libdir}
%{__make} %{?_smp_mflags}

%install
%{__make} install

%post -n %{name}-0 -p /sbin/ldconfig
%postun -n %{name}-0 -p /sbin/ldconfig

%files -n %{name}-0
%defattr (-,root,root)
%doc AUTHORS COPYING README.md
%{_libdir}/%{name}.so.*

%files devel
%defattr (-,root,root)
%doc CONVENTIONS examples
%{_libdir}/%{name}.so
%{_includedir}/git2*
%{_libdir}/pkgconfig/libgit2.pc

%changelog
* Thu Oct 27 2011 saschpe@suse.de
- Change license to 'GPL-2.0 with linking', fixes bnc#726789
* Wed Oct 26 2011 saschpe@suse.de
- Update to version 0.15.0:
  * Upstream doesn't provide changes
- Removed outdated %%clean section
* Tue Jan 18 2011 saschpe@gmx.de
- Proper Requires for devel package
* Tue Jan 18 2011 saschpe@gmx.de
- Set BuildRequires to "openssl-devel" also for RHEL and CentOS
* Tue Jan 18 2011 saschpe@gmx.de
- Initial commit (0.0.1)
- Added patch to fix shared library soname
