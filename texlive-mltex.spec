%global tl_name mltex
%global tl_revision 71363
%global tl_bin_links mllatex:pdftex mltex:pdftex

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	The MLTeX system
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/systems/generic/mltex
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mltex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mltex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(babel)
Requires:	texlive(cm)
Requires:	texlive(dehyph)
Requires:	texlive(firstaid)
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(l3backend)
Requires:	texlive(l3kernel)
Requires:	texlive(latex)
Requires:	texlive(latex-fonts)
Requires:	texlive(latexconfig)
Requires:	texlive(mltex.bin)
Requires:	texlive(plain)
Requires:	texlive(tex-ini-files)
Requires:	texlive(unicode-data)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
MLTeX is a modification of TeX version >=3.0 that allows the hyphenation
of words with accented letters using ordinary Computer Modern (CM)
fonts. The system is distributed as a TeX change file.

