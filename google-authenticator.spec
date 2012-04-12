%define snapshot d525a9bab875
%define snapdate 20110830
Name:           google-authenticator
Version:        0
Release:        0.3.%{snapdate}.hg%{snapshot}%{?dist}
Summary:        One-time passcode support using open standards
Group: Security
License:        ASL 2.0
URL:            http://code.google.com/p/google-authenticator/
# hg archive -r ${snapshot} %{name}-0.%{snapdate}.hg%{snapshot}.tar.gz
Source0:        %{name}-0.%{snapdate}.hg%{snapshot}.tar.gz
Patch1:         0001-Add-no-drop-privs-option-to-manage-secret-files-as-r.patch
Patch2:         0002-Allow-expansion-of-PAM-environment-variables-in-secr.patch
BuildRequires:  pam-devel qrencode-devel
BuildRoot:     %{_tmppath}/%{name}.%{version}-%{release}


%description
The Google Authenticator package contains a pluggable authentication
module (PAM) which allows login using one-time passcodes conforming to
the open standards developed by the Initiative for Open Authentication
(OATH) (which is unrelated to OAuth).

Passcode generators are available (separately) for several mobile
platforms.

These implementations support the HMAC-Based One-time Password (HOTP)
algorithm specified in RFC 4226 and the Time-based One-time Password
(TOTP) algorithm currently in draft.

%prep
%setup -q -n %{name}-0.%{snapdate}.hg%{snapshot}
%patch1 -p1
%patch2 -p1

%build
cd libpam
make CFLAGS="${CFLAGS:-%optflags}" LDFLAGS=-ldl %{?_smp_mflags}

%check
cd libpam
./pam_google_authenticator_unittest

%install
rm -rf $RPM_BUILD_ROOT
cd libpam
mkdir -p $RPM_BUILD_ROOT/%{_lib}/security
install -m0755 pam_google_authenticator.so $RPM_BUILD_ROOT/%{_lib}/security/pam_google_authenticator.so
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m0755 google-authenticator $RPM_BUILD_ROOT/%{_bindir}/google-authenticator

%files
/%{_lib}/security/*
%{_bindir}/google-authenticator
%doc libpam/FILEFORMAT libpam/README libpam/totp.html


%changelog
* Wed Apr 11 2012 David Johansen <david@makewhatis.com> - 0-0.3.20110830.hgd525a9bab875
- Rebuilt for Centos 5.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20110830.hgd525a9bab875
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

