Summary:	A fast-action violent game for the X Window System
Summary(pl):	Brutalna gra o szybkiej akcji pod X Window System
Name:		xevil
Version:	2.02
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	ftp://ftp.xevil.com/stable/%{name}src%{version}.zip
Patch0:		%{name}-config.patch
Patch1:		%{name}-c++.patch
URL:		http://www.xevil.com/
BuildRequires:	unzip
BuildRequires:	XFree86-devel >= 4.0
BuildRequires:	libstdc++-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XEvil is an X Window System based game with a side view display
reminiscent of LodeRunner. The object of the game is to run around
killing everything in sight and exploring the different levels. XEvil
can be played against the computer or against other people.

%description -l pl
xevil jest gr± pod X Window System bazuj±c± na LodeRunnerze. Celem gry
jest zabijanie wszystkiego w zasiêgu wzroku oraz przedzenie kolejnych
poziomów. W xevil mo¿na graæ przeciwko komputerowi albo innym graczom.

%prep
%setup -q -T -c

unzip -q %{SOURCE0}

%patch0 -p1
%patch1 -p1

%build
%{__make} HOSTTYPE=i386 DEBUG_OPT="%{rpmcflags}" LINK_FLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Games}

install x11/REDHAT_LINUX/xevil $RPM_BUILD_ROOT%{_bindir}

gzip -9nf readme.txt

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xevil.desktop <<EOF
# KDE Config File
[KDE Desktop Entry]
Name=xevil
Comment=Fast action game
Exec=xevil
Terminal=0
Type=Application
EOF

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz instructions
%attr(755,root,root) %{_bindir}/xevil
%{_applnkdir}/Games/*
