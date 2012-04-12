#
# spec file for package python-pygit2
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           python-pygit2
Version:        0.1
Release:        2.4
Url:            http://github.com/dborowitz/pygit2
Summary:        Python bindings for libgit2
License:        Apache-2.0
Group:          Development/Languages/Python
Source:         libgit2-pygit2-v0.15.0-0-g1dde686.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libgit2-devel
BuildRequires:  python-devel
BuildRequires:  openssl-devel

%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%description
Bindings for libgit2, a linkable C library for the Git version-control system.

%prep
export CFLAGS="%{optflags}"
%setup -n libgit2-pygit2-1dde686
# Adjust include/lib paths to local system
sed -i 's|/usr/local/include|%{_includedir}|' setup.py
sed -i 's|/usr/local/lib|%{_libdir}|' setup.py

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

#%%check
#python setup.py test

%files
%defattr(-,root,root,-)
%doc README.md COPYING
%python_sitearch/pygit2*

%changelog
* Wed Jan 26 2011 saschpe@gmx.de
- Removed SUSE-specific --record-rpm for file lists
* Tue Jan 18 2011 saschpe@gmx.de
- Install documentation (README.md and COPYING)
- Fix install section for other distros
* Tue Jan 18 2011 saschpe@gmx.de
- Initial commit (0.1)
- Added patch include recent libgit2 changes
