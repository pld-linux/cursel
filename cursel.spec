Summary:	form and menu langugae interpreter
Summary(pl):	interpreter jêzyka formularzy i menu
Name:		cursel
Version:	0.1.9
Release:	1
License:	GPL
Group:		Applications/Terminal
Group(de):	Applikationen/Terminal
Group(pl):	Aplikacje/Terminal
Source0:	http://users.pandora.be/stes/%{name}-%{version}.tar.gz
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	objc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CURSEL is a FMLI implementation, a small language that allows you to
quickly make a form- and menu- based character interface to shell
scripts and other programs.

%description -l pl
CURSEL jest implementacj± FMLI (Form and Menu Language Interpreter).
Niewielki jêzyk pozwalaj±cy na szybkie tworzenie interfejsu
u¿ytkownika do skryptów pow³oki lub innych programów.

%prep
%setup  -q

%build
%configure
%{__make} \
	OBJC="%{_bindir}/objc -I%{_includedir}/ncurses"\
	LIBS="-lform -lmenu -lncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

gzip -9nf README TODO CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
