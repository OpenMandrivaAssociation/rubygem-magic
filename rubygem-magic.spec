%define rbname magic

Summary:	Ruby FFI bindings to libmagic
Name:		rubygem-%{rbname}
Version:	0.2.8
Release:	1
License:	GPLv2+ or Ruby
Group:		Development/Ruby
Url:		https://github.com/qoobaa/%{rbname}
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems
BuildArch:	noarch

%description
Ruby FFI bindings to libmagic.

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install

