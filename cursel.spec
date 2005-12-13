Summary:	Form and menu language interpreter
Summary(pl):	Interpreter jêzyka formularzy i menu
Name:		cursel
Version:	0.2.2
Release:	1
License:	GPL
Group:		Applications/Terminal
Source0:	http://users.pandora.be/stes/%{name}-%{version}.tar.gz
# Source0-md5:	3797e0236c4f6d76d8cfbb538d5240cf
URL:		http://users.pandora.be/stes/compiler.html
BuildRequires:	autoconf
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	ncurses-ext-devel >= 5.2
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
%setup -q

%build
%{__autoconf}
%configure
%{__make} \
	OBJC="%{_bindir}/objc -Wc:%{rpmcflags} -I/usr/include/ncurses"\
	LIBS="-lform -lmenu -lncurses %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO CHANGES
%attr(755,root,root) %{_bindir}/*
