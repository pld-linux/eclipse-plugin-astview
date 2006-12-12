Summary:	AST View - a view to visualize the AST (abstract syntax tree) of a Java file open in the editor
Name:		eclipse-plugin-astview
Version:	1.1.3
Release:	1
License:	EPL v1.0
Group:		Development/Languages
Source0:	http://www.eclipse.org/jdt/ui/update-site/plugins/org.eclipse.jdt.astview_%{version}.jar
# Source0-md5:	1b189f8076c6c030a3ea51e2fc7401a2
URL:		http://www.eclipse.org/jdt/ui/astview/
Requires:	eclipse >= 3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  	%{_libdir}/eclipse

%description
A view to visualize the AST (abstract syntax tree) of a Java file open
in the editor. Navigate from text selection to AST nodes and from
nodes to selections. Show bindings and compare them.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/plugins

install %{SOURCE0} $RPM_BUILD_ROOT%{_eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/eclipse/plugins/*
