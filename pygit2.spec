%define name pygit2
%define version 0.16.0
%define unmangled_version 0.16.0
%define unmangled_version 0.16.0
%define release 1

Summary: Python bindings for libgit2.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPLv2
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: J. David Ibáñez <jdavid.ibp@gmail.com>
Url: http://github.com/libgit2/pygit2

%description
This is pygit2!

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
