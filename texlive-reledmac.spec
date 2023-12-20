Name:		texlive-reledmac
Version:	68411
Release:	1
Summary:	Typeset scholarly editions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/reledmac
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reledmac.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reledmac.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reledmac.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for typesetting scholarly critical editions,
replacing the established ledmac and eledmac packages. Ledmac
itself was a LaTeX port of the plain TeX EDMAC macros. The
package supports indexing by page and by line numbers, and
simple tabular- and array-style environments. The package is
distributed with the related reledpar package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/reledmac
%{_texmfdistdir}/tex/latex/reledmac
%doc %{_texmfdistdir}/doc/latex/reledmac

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
