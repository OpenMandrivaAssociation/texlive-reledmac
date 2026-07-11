%global tl_name reledmac
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.44.4
Release:	%{tl_revision}.1
Summary:	Typeset scholarly editions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/reledmac
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/reledmac.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/reledmac.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/reledmac.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package for typesetting scholarly critical editions, replacing the
established ledmac and eledmac packages. Ledmac itself was a LaTeX port
of the plain TeX EDMAC macros. The package supports indexing by page and
by line numbers, and simple tabular- and array-style environments. The
package is distributed with the related reledpar package.

