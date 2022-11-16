Name:		texlive-xindex
Version:	64453
Release:	1
Summary:	Unicode compatible index generation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xindex
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xindex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xindex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a unicode compatible index programm for
LaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/tex/lualatex/xindex
%{_texmfdistdir}/texmf-dist/tex/latex/xindex
%{_texmfdistdir}/texmf-dist/scripts/xindex
%doc %{_texmfdistdir}/texmf-dist/doc/lualatex/xindex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
