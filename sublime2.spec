%define ver  2139
%define rel  1

Name:          sublime-text
Version:       %{ver}
Release:       1%{dist}
Summary:       Sublime Text is a sophisticated text editor for code, html and prose. You'll love the slick user interface and extraordinary features. 
Group:         Applications/Editors
License:       Copyright Sublime HQ Pty Ltd
BuildArch:	   %{_arch}
URL:           http://www.sublimetext.com
Source0:       %{name}-%{version}-%{_arch}.tar.gz
Source1:	   sublime2.desktop
Source2:	   sublime-text-2.png
BuildRoot:     %{_tmppath}/%{name}.%{version}-%{release}
Requires: 		python
%description
Sublime Text is a sophisticated text editor for code, html and prose. You'll love the slick user interface and extraordinary features.

%prep
%setup 
#-q -n %{name}-%{version}-%{_arch}

%build

%install
rm -rf %{buildroot}
%{__mkdir_p}  %{buildroot}/usr/local/%{name}
%{__mkdir_p}  %{buildroot}/usr/share/pixmaps
%{__mkdir_p}  %{buildroot}%{_datadir}/applications
%{__cp} -aR ./* %{buildroot}/usr/local/%{name}/
install -m 644 %{SOURCE2}  %{buildroot}/usr/share/pixmaps/sublime-text-2.png
%{__chmod} 755 %{buildroot}/usr/local/%{name}/sublime_text
%{__cp} %{SOURCE1} %{buildroot}%{_datadir}/applications/

%clean
%{__rm} -rf %{_builddir}


%files
%defattr(-,root,root,-)
/usr/local/%{name}/
/usr/share/applications/sublime2.desktop
/usr/share/pixmaps/sublime-text-2.png

%changelog
* Sun Nov 6 2011 David Johansen <david@fhlabs.com> 2139
- Initial rpm using stable v0.4.12
