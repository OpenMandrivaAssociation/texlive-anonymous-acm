Name:		texlive-anonymous-acm
Version:	55121
Release:	1
Summary:	Typeset anonymous versions for ACM articles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/anonymous-acm
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anonymous-acm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anonymous-acm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Academics often need to submit anonymous versions of their
papers for peer-review. This often requires anonymization which
at some future date needs to be reversed. However
de-anonymizing an anonymized paper can be laborious and
error-prone. This LaTeX package allows anonymization options to
be specified at the time of writing for authors using
acmart.cls, the official Association of Computing Machinery
(ACM) master article template. Anonymization or deanonymization
is carried out by simply changing one option and recompiling.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/anonymous-acm
%doc %{_texmfdistdir}/doc/latex/anonymous-acm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
