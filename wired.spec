#
Summary:	Professional music production system
Name:		wired
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/wired/%{name}-%{version}.tar.gz
# Source0-md5:	90db7fe5b070a3fb4255d681226626cd
URL:		http://bloodshed.net/wired/
BuildRequires:	wxGTK2-devel >= 2.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wired aims to be a professional music production and creation 
software running on the Linux operating system.

It brings musicians a complete studio environment to compose and 
record music without requiring expensive hardware. 

%prep
%setup -q -n %{name}

%build
cd src
#rm -f missing
#%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
#%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/*
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
