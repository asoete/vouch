# https://github.com/vouch/vouch-proxy
%global goipath         github.com/vouch/vouch-proxy
%global forgeurl        https://github.com/vouch/vouch-proxy
Version:                0.37.0

%gometa

%global common_description %{an SSO and OAuth / OIDC login solution for Nginx
%using the auth_request module }

%global golicenses    LICENSE
%global godocs        *.md

%global godevelheader %{expand:
# The devel package will usually benefit from corresponding project binaries.
Requires:  %{name} = %{version}-%{release}
}

Name:           %{goname}
Release:        1%{?dist}
Summary:        an SSO and OAuth / OIDC login solution for Nginx using the auth_request module
# Detected licences
# - *No copyright* Apache License (v2.0) at 'LICENSE'
# json/ is BSD
License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires: golang(github.com/julienschmidt/httprouter)
BuildRequires: golang(go.uber.org/zap)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/vouch %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

/* %check */
/* %gocheck */

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Apr 13 15:10:43 CET 2022 Arne Soete <arne.soete@irc.vib-UGent.be> - 0.37.0-1
- Initial packaging
