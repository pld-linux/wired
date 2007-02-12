# NOTE: current version is 0.2.2
Summary:	Professional music production system
Summary(pl.UTF-8):   Profesjonalny system produkcji muzyki
Name:		wired
Version:	0.11
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/wired/%{name}-%{version}.tar.gz
# Source0-md5:	6002612be1a520088becb1e3369a1088
URL:		http://bloodshed.net/wired/
BuildRequires:	libsndfile-devel
BuildRequires:	portaudio-devel >= 19
BuildRequires:	soundtouch-devel >= 1.2.1
BuildRequires:	wxGTK2-devel >= 2.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wired aims to be a professional music production and creation 
software running on the Linux operating system.

It brings musicians a complete studio environment to compose and 
record music without requiring expensive hardware. 

%description -l pl.UTF-8
Wired ma być profesjonalnym oprogramowaniem do produkcji i tworzenia
muzyki działające pod systemem operacyjnym Linux.

Dostarcza muzykom kompletne środowisko studyjne do komponowania i
nagrywania muzyki bez wymagania drogiego sprzętu.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
