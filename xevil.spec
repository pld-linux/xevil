Summary:	A fast-action violent game for the X Window System
Summary(cs):	Hra podobná høe Pac-Man pro X Window System
Summary(da):	Et Pacman-lignende spil til X-vinduessystemet
Summary(de):	Ein schnelles, extrem gewalttätiges Actionspiel für X
Summary(fr):	Un jeu d'action rapide et très violent sous X
Summary(it):	Un violento gioco di azione per X Window
Summary(no):	Et hurtig voldelig spill for X-vindussytemet
Summary(pl):	Brutalna gra o szybkiej akcji pod X Window System
Summary(sk):	Rýchla násilná hra pre X Window Systém
Summary(tr):	Hýzlý ve þiddet yüklü bir X oyunu
Name:		xevil
Version:	2.02
Release:	3
License:	GPL
Group:		X11/Applications/Games
#Source0:	http://www.xevil.com/stable/%{name}src%{version}.zip
Source0:	%{name}src%{version}.zip
# Source0-md5:	e1890f77144367e2e8bbf3609458b784
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
Patch1:		%{name}-c++.patch
Patch2:		%{name}-gcc3.patch
Patch3:		%{name}-const_float.patch
URL:		http://www.xevil.com/
BuildRequires:	unzip
BuildRequires:	XFree86-devel >= 4.0
BuildRequires:	libstdc++-devel
BuildRequires:	/usr/bin/compress
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XEvil is an X Window System based game with a side view display
reminiscent of LodeRunner. The object of the game is to run around
killing everything in sight and exploring the different levels. XEvil
can be played against the computer or against other people.

%description -l cs
XEvil je hra pro X Window System s podobným boèním pohledem na hru
pøipomínající hru LodeRunner. Cílem hry je projít celou úroveò a zabít
v¹echno v dohledu a dostat se do dal¹í úrovnì. XEvil mù¾ete hrát proti
poèítaèi nebo proti jiným hráèùm.

%description -l de
Ein Action/Adventure-Spiel für X Window, in dem Sie als Ninja alles
niedermachen und dann die Gegend erkunden - wenn Sie überleben.

%description -l fr
XEvil est un jeu sous X Window avec une vue de côté à la Lode Runner.
Il faut explorer les différents niveaux en tuant tout ce qui bouge. On
peut jouer contre un autre être humain ou contre l'ordinateur.

%description -l it
Un gioco per X11 con una vista dall'utente stile LodeRunner.
L'obbiettivo del gioco e' quello di andare in giro ed uccidere tutti
esplorando i vari livelli.

%description -l pl
xevil jest gr± pod X Window System bazuj±c± na LodeRunnerze. Celem gry
jest zabijanie wszystkiego w zasiêgu wzroku oraz przechodzenie
kolejnych poziomów. W xevil mo¿na graæ przeciwko komputerowi albo
innym graczom.

%description -l sk
XEvil je hra pre X Window systém s boèným pohµadom, pripomínajúca
LodeRunner. Cieµom hry je pohybova» sa po hre, zabíja» v¹etko v
dohµade a skúma» rozlièné úrovne. XEvil mô¾e by» hraný proti poèítaèu,
alebo proti iným hráèom.

%description -l tr
X-Windows altýnda oynanan bir action/macera oyunu. Sizin rolünüz, bir
Ninja savaþçýsý olarak karþýnýza çýkan her þeyi öldürmek.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} HOSTTYPE=i386 \
	DEBUG_OPT="%{rpmcflags} -fno-exceptions" \
	LINK_FLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Games/Arcade,%{_pixmapsdir}}

install x11/REDHAT_LINUX/xevil $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt instructions
%attr(755,root,root) %{_bindir}/xevil
%{_applnkdir}/Games/Arcade/*
%{_pixmapsdir}/*.png
