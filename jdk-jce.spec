%global jdk_major %{?jdk_version_major}%{!?jdk_version_major:8}
%global jdk_version_api   1.%{jdk_major}

%global iteration %{?ITERATION}%{!?ITERATION:1}

%global jce_datadir %{_datadir}/%{name}

%if 0%{?rhel} == 7
   # CentOS 7 forces ".el7.centos", wtf?
   %define dist .el7
%endif

Name:           jdk%{jdk_version_api}-jce
Version:        %{jdk_version_api}
Release:        %{iteration}%{?dist}
Summary:        Oracle JDK JCE Binary Package
Group:          Development/Tools
AutoReqProv:    no
Provides:       java-%{jdk_major}-jce
License:        Oracle Binary License
URL:            http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html
Source0:        http://download.oracle.com/otn-pub/java/jce/%{jdk_major}/jce_policy-%{jdk_major}.zip
Source1:        ORACLE-LICENSE.txt
BuildArch:      noarch

%if 0%{?el6}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%endif

%description
Package to deploy Oracle's JCE binaries for use with jdk-helper

%prep
%setup -n UnlimitedJCEPolicyJDK%{jdk_major}
%{__cp} %{SOURCE1} ./LICENSE.txt

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m 0755 %{buildroot}%{jce_datadir}
%{__install} -p -m 0644 -t %{buildroot}%{jce_datadir} *.jar

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt LICENSE.txt
%dir %{jce_datadir}
%{jce_datadir}/*

%changelog
* Wed Jun 14 2017 Brett Delle Grazie <brett.dellegrazie@gmail.com> - 1.8-1
- Initial Version
