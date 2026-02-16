Name:           svt-jpeg-xs
Version:        0.9.0
Release:        1%{?dist}
Summary:        Intel SVT implementation of ISO/IEC 21122 protocol
License:        BSD-2-Clause-Patent
URL:            https://github.com/OpenVisualCloud/SVT-JPEG-XS

Source0:        %{url}/archive/v%{version}/SVT-JPEG-XS-v%{version}.tar.gz
Patch0:		%{name}-cmake.patch

BuildRequires:  cmake >= 3.16
BuildRequires:  cpuinfo-devel
BuildRequires:  gcc-c++ >= 9.4.0
BuildRequires:  yasm >= 1.2.0

%description
Intel Scalable Video Technology implementation of ISO/IEC 21122 protocol.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Intel JPEG-XS Library tools and samples
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
Tools and samples for the Intel Scalable Video Technology implementation of
the ISO/IEC 21122 protocol.

%prep
%autosetup -p1 -n SVT-JPEG-XS-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE.md
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/SvtJpegxs.pc

%files tools
%{_bindir}/SvtJpegxsDecApp
%{_bindir}/SvtJpegxsEncApp
%{_bindir}/SvtJpegxsSampleDecoder
%{_bindir}/SvtJpegxsSampleEncoder

%changelog
* Mon Feb 16 2026 Simone Caronni <negativo17@gmail.com> - 0.9.0-1
- First build.
