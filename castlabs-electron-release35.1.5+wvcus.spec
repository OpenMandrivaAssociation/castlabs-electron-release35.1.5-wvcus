%ifarch x86_64
%global arch x64
%elifarch znver1
%global arch x64
%elifarch aarch64
%global arch arm64
%endif

%global debug_package %{nil}
%global packagename castlabs-%{name}-%{version}+wvcus

Name:		electron-releases
Version:	35.1.5
Release:    1
Summary:        A complete solution to package and build a ready for distribution Electron app with “auto update” support out of the box
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/castlabs/electron-releases
Source0:        https://github.com/castlabs/electron-releases/archive/v%{version}+wvcus/%{name}-%{version}-wvcus.tar.gz
 Source1:        %{packagename}-node_modules.tar.gz
 Source2:        %{packagename}-pnpm_store.tar.gz

BuildRequires:  nodejs
BuildRequires:  nodejs-packaging
BuildRequires:  zip
BuildRequires:  pnpm
Requires:       bash
Recommends:     python

%description
%summary

%package -n %{packagename}
Summary:        %summary
Group:          Development/Languages/Other

%description -n %{packagename}
%summary

%prep
%autosetup -n %{name}-%{version}-wvcus -p1
tar -zxf %{S:1}
tar -zxf %{S:2}

%install
pnpm config set store-dir %{_builddir}/%{name}-%{version}-wvcus/pnpm_store
pnpm install --offline --force
cd dist
zip -r electron-v35.1.5+wvcus-linux-%{arch}.zip *
mkdir -p %{buildroot}%{_prefix}/src/electron/
mv electron-v35.1.5+wvcus-linux-%{arch}.zip %{buildroot}%{_prefix}/src/electron/

%files -n %{packagename}
%license LICENSE
%{_prefix}/src/electron/
