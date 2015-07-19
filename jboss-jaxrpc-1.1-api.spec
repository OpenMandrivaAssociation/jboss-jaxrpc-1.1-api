%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jaxrpc-1.1-api
Version:          1.0.1
Release:          8.2
Summary:          Java API for XML-Based RPC (JAX-RPC) 1.1
Group:		  Development/Java
License:          CDDL or GPLv2 with exceptions
Url:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-jaxrpc-api_spec.git jboss-jaxrpc-1.1-api
# cd jboss-jaxrpc-1.1-api/ && git archive --format=tar --prefix=jboss-jaxrpc-1.1-api/ jboss-jaxrpc-api_1.1_spec-1.0.1.Final | xz > jboss-jaxrpc-1.1-api-1.0.1.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    java-devel
BuildRequires:    jboss-specs-parent
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin
BuildRequires:    maven-ejb-plugin

Requires:         jboss-servlet-3.0-api
Requires:         jpackage-utils
Requires:         java

BuildArch:        noarch

%description
The JAX-RPC 1.1 API classes.

%package javadoc
Summary:          Javadocs for %{name}

Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jaxrpc-1.1-api

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 9 2013 Ade Lee <alee@redhat.com> 1.0.1-4
- Resolves #961461 - Remove unneeded maven-checkstyle-plugin BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Upstream release 1.0.1.Final
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.2.20120309gita3c227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-0.1.20120309gita3c227
- Packaging after license cleanup upstrea

* Mon Oct 24 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-2
- Fixed apidocs issue

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Initial packaging
