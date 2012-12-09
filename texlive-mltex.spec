# revision 22650
# category Package
# catalog-ctan /systems/generic/mltex
# catalog-date 2008-01-25 17:33:09 +0100
# catalog-license knuth
# catalog-version 2.2
Name:		texlive-mltex
Version:	2.2
Release:	3
Summary:	The MLTeX system
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/generic/mltex
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mltex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mltex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-latex
Requires:	texlive-mltex.bin

%description
MLTeX is a modification of TeX version >=3.0 that allows the
hyphenation of words with accented letters using ordinary
Computer Modern (CM) fonts. The system is distributed as a TeX
change file.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mltex/lo1enc.def
%{_texmfdistdir}/tex/latex/mltex/mlltxchg.def
%{_texmfdistdir}/tex/latex/mltex/mltex.sty
%{_texmfdistdir}/tex/mltex/config/mltex.ini
%_texmf_fmtutil_d/mltex
%doc %{_texmfdistdir}/doc/latex/mltex/README
%doc %{_texmfdistdir}/doc/latex/mltex/mltex.txt
%doc %{_texmfdistdir}/doc/latex/mltex/testmlft.dvi
%doc %{_texmfdistdir}/doc/latex/mltex/testmlft.tex
%doc %{_texmfdistdir}/doc/latex/mltex/testmlsw.dvi
%doc %{_texmfdistdir}/doc/latex/mltex/testmlsw.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/mltex <<EOF
#
# from mltex:
mllatex pdftex language.dat -translate-file=cp227.tcx -mltex mllatex.ini
mltex pdftex - -translate-file=cp227.tcx -mltex mltex.ini
EOF


%changelog
* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-3
+ Revision: 778454
- Rebuild after tlpobj2spec.pl bug correction.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-2
+ Revision: 754023
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.2-1
+ Revision: 719049
- texlive-mltex
- texlive-mltex
- texlive-mltex
- texlive-mltex

