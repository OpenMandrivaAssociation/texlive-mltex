Name:		texlive-mltex
Version:	62145
Release:	2
Summary:	The MLTeX system
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/generic/mltex
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mltex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mltex.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/mltex <<EOF
#
# from mltex:
mllatex pdftex language.dat -translate-file=cp227.tcx -mltex *mllatex.ini
mltex pdftex - -translate-file=cp227.tcx -mltex mltex.ini
EOF
