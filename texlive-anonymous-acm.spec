%global tl_name anonymous-acm
%global tl_revision 55121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Typeset anonymous versions for ACM articles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/anonymous-acm
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/anonymous-acm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/anonymous-acm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Academics often need to submit anonymous versions of their papers for
peer-review. This often requires anonymization which at some future date
needs to be reversed. However de-anonymizing an anonymized paper can be
laborious and error-prone. This LaTeX package allows anonymization
options to be specified at the time of writing for authors using
acmart.cls, the official Association of Computing Machinery (ACM) master
article template. Anonymization or deanonymization is carried out by
simply changing one option and recompiling.

