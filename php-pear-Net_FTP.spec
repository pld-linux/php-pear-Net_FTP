%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	FTP
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - comfortable communication with FTP-servers
Summary(pl):	%{_pearname} - komfortowa komunikacja z serwerami FTP
Name:		php-pear-%{_pearname}
Version:	1.3.0
%define	_version	1.3.0beta1
Release:	0.beta1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{_version}.tgz
# Source0-md5:	86e2ad80bfac8153f243e5c51dd79732
URL:		http://pear.php.net/package/Net_FTP/
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
Klasa ta pozwala na bardziej komfortowa komunikacj� z serwerami FTP
ni� jest to realizowane przez funkcje w PHP. Szczeg�lnie �atwy jest
down- i upload rekursywny.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c -n %{name}-%{_version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{_version}/%{_class}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{_version}/example/*
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
