Summary:	A fast-action violent game for the X Window System
Summary(cs.UTF-8):   Hra podobná hře Pac-Man pro X Window System
Summary(da.UTF-8):   Et Pacman-lignende spil til X-vinduessystemet
Summary(de.UTF-8):   Ein schnelles, extrem gewalttätiges Actionspiel für X
Summary(fr.UTF-8):   Un jeu d'action rapide et très violent sous X
Summary(it.UTF-8):   Un violento gioco di azione per X Window
Summary(nb.UTF-8):   Et hurtig voldelig spill for X-vindussytemet
Summary(pl.UTF-8):   Brutalna gra o szybkiej akcji pod X Window System
Summary(sk.UTF-8):   Rýchla násilná hra pre X Window Systém
Summary(tr.UTF-8):   Hızlı ve şiddet yüklü bir X oyunu
Name:		xevil
Version:	2.02r2
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.xevil.com/download/stable/%{name}src%{version}.zip
# Source0-md5:	09a9ef720b7204b0be68c4f462def370
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
Patch1:		%{name}-gcc3.patch
Patch2:		%{name}-const_float.patch
Patch3:		%{name}-c++.patch
URL:		http://www.xevil.com/
BuildRequires:	libstdc++-devel
BuildRequires:	unzip
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XEvil is an X Window System based game with a side view display
reminiscent of LodeRunner. The object of the game is to run around
killing everything in sight and exploring the different levels. XEvil
can be played against the computer or against other people.

%description -l cs.UTF-8
XEvil je hra pro X Window System s podobným bočním pohledem na hru
připomínající hru LodeRunner. Cílem hry je projít celou úroveň a zabít
všechno v dohledu a dostat se do další úrovně. XEvil můžete hrát proti
počítači nebo proti jiným hráčům.

%description -l de.UTF-8
Ein Action/Adventure-Spiel für X Window, in dem Sie als Ninja alles
niedermachen und dann die Gegend erkunden - wenn Sie überleben.

%description -l fr.UTF-8
XEvil est un jeu sous X Window avec une vue de côté à la Lode Runner.
Il faut explorer les différents niveaux en tuant tout ce qui bouge. On
peut jouer contre un autre être humain ou contre l'ordinateur.

%description -l it.UTF-8
Un gioco per X11 con una vista dall'utente stile LodeRunner.
L'obbiettivo del gioco e' quello di andare in giro ed uccidere tutti
esplorando i vari livelli.

%description -l pl.UTF-8
xevil jest grą pod X Window System bazującą na LodeRunnerze. Celem gry
jest zabijanie wszystkiego w zasięgu wzroku oraz przechodzenie
kolejnych poziomów. W xevil można grać przeciwko komputerowi albo
innym graczom.

%description -l sk.UTF-8
XEvil je hra pre X Window systém s bočným pohľadom, pripomínajúca
LodeRunner. Cieľom hry je pohybovať sa po hre, zabíjať všetko v
dohľade a skúmať rozličné úrovne. XEvil môže byť hraný proti počítaču,
alebo proti iným hráčom.

%description -l tr.UTF-8
X Window altında oynanan bir action/macera oyunu. Sizin rolünüz, bir
Ninja savaşçısı olarak karşınıza çıkan her şeyi öldürmek.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# no <strstream.h> compat in gcc 3.3
cat > cmn/strstream.h <<EOF
#include <strstream>
using namespace std;
EOF

%build
%{__make} \
	HOSTTYPE=i386 \
	DEBUG_OPT="%{rpmcflags} -fno-exceptions" \
	LINK_FLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

install x11/REDHAT_LINUX/xevil $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt instructions
%attr(755,root,root) %{_bindir}/xevil
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
