Summary:	A fast-action violent game for the X Window System
Summary(cs):	Hra podobn� h�e Pac-Man pro X Window System
Summary(da):	Et Pacman-lignende spil til X-vinduessystemet
Summary(de):	Ein schnelles, extrem gewaltt�tiges Actionspiel f�r X
Summary(fr):	Un jeu d'action rapide et tr�s violent sous X
Summary(it):	Un violento gioco di azione per X Window
Summary(no):	Et hurtig voldelig spill for X-vindussytemet
Summary(pl):	Brutalna gra o szybkiej akcji pod X Window System
Summary(sk):	R�chla n�siln� hra pre X Window Syst�m
Summary(tr):	H�zl� ve �iddet y�kl� bir X oyunu
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
XEvil je hra pro X Window System s podobn�m bo�n�m pohledem na hru
p�ipom�naj�c� hru LodeRunner. C�lem hry je proj�t celou �rove� a zab�t
v�echno v dohledu a dostat se do dal�� �rovn�. XEvil m��ete hr�t proti
po��ta�i nebo proti jin�m hr���m.

%description -l de
Ein Action/Adventure-Spiel f�r X Window, in dem Sie als Ninja alles
niedermachen und dann die Gegend erkunden - wenn Sie �berleben.

%description -l fr
XEvil est un jeu sous X Window avec une vue de c�t� � la Lode Runner.
Il faut explorer les diff�rents niveaux en tuant tout ce qui bouge. On
peut jouer contre un autre �tre humain ou contre l'ordinateur.

%description -l it
Un gioco per X11 con una vista dall'utente stile LodeRunner.
L'obbiettivo del gioco e' quello di andare in giro ed uccidere tutti
esplorando i vari livelli.

%description -l pl
xevil jest gr� pod X Window System bazuj�c� na LodeRunnerze. Celem gry
jest zabijanie wszystkiego w zasi�gu wzroku oraz przechodzenie
kolejnych poziom�w. W xevil mo�na gra� przeciwko komputerowi albo
innym graczom.

%description -l sk
XEvil je hra pre X Window syst�m s bo�n�m poh�adom, pripom�naj�ca
LodeRunner. Cie�om hry je pohybova� sa po hre, zab�ja� v�etko v
doh�ade a sk�ma� rozli�n� �rovne. XEvil m��e by� hran� proti po��ta�u,
alebo proti in�m hr��om.

%description -l tr
X-Windows alt�nda oynanan bir action/macera oyunu. Sizin rol�n�z, bir
Ninja sava���s� olarak kar��n�za ��kan her �eyi �ld�rmek.

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
