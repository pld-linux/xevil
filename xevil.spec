Summary:	A fast-action violent game for the X Window System
Summary(de):	Ein schnelles, extrem gewaltt�tiges Actionspiel f�r X
Summary(fr):	Un jeu d'action rapide et tr�s violent sous X
Summary(pl):	Brutalna gra o szybkiej akcji pod X Window System
Summary(tr):	H�zl� ve �iddet y�kl� bir X oyunu
Name:		xevil
Version:	2.02
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.xevil.com/stable/%{name}src%{version}.zip
Source1:	%{name}.desktop
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

%description -l de
Ein Action/Adventure-Spiel f�r X Window, in dem Sie als Ninja alles
niedermachen und dann die Gegend erkunden - wenn Sie �berleben.

%description -l fr
Jeu d'action/aventure pour X Window dans lequel vous, guerrier Ninja,
tuez tout ce que vous voyez et essayez de survivre.

%description -l pl
xevil jest gr� pod X Window System bazuj�c� na LodeRunnerze. Celem gry
jest zabijanie wszystkiego w zasi�gu wzroku oraz przedzenie kolejnych
poziom�w. W xevil mo�na gra� przeciwko komputerowi albo innym graczom.

%description -l tr
X-Windows alt�nda oynanan bir action/macera oyunu. Sizin rol�n�z, bir
Ninja sava���s� olarak kar��n�za ��kan her �eyi �ld�rmek.

%prep
%setup -q -T -c
unzip -q %{SOURCE0}

%patch0 -p1
%patch1 -p1

%build
%{__make} HOSTTYPE=i386 \
	DEBUG_OPT="%{rpmcflags} -fno-exceptions -fno-rtti" \
	LINK_FLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Games}

%{__install} x11/REDHAT_LINUX/xevil $RPM_BUILD_ROOT%{_bindir}

gzip -9nf readme.txt

%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz instructions
%attr(755,root,root) %{_bindir}/xevil
%{_applnkdir}/Games/*
