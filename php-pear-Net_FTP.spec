%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       FTP
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Comfortable communication with FTP-servers
Summary(pl):	%{_pearname} - Komfortowa komunikacja z serwerami FTP
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a35a9d197673b5e1c88633f9f312a047
URL:		http://www.schlitt.info/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-ftp
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class allows you to communicate with FTP-servers more comfortable
that the ftp-functions of PHP. Especially you can up- and download
recursively.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa ta pozwala na bardziej komfortowa komunikacjê z serwerami FTP
ni¿ jest to realizowane przez funkcje w PHP. Szczególnie ³atwy jest
down- i upload rekursywny.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/example/*
%{php_pear_dir}/%{_class}/*.php
