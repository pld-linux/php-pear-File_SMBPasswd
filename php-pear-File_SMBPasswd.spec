%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	SMBPasswd
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - class for managing SAMBA style password files
Summary(pl):	%{_pearname} - klasa do zarz±dzania plikami z has³ami SAMBY
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	efc273c183fbf2524089f15c92fc8fa6
URL:		http://pear.php.net/package/File_SMBPasswd/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With this package, you can maintain smbpasswd-files, usualy used by
SAMBA.

In PEAR status of this package is: %{_status}.

%description -l pl
Przy u¿yciu tego pakietu mo¿na zarz±dzaæ plikami smbpasswd, u¿ywanymi
zwykle przez SAMBÊ.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
