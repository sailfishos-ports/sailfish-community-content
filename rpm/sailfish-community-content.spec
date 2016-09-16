Name:       sailfish-community-content

Summary:    Preloded Community Content
Version:    0.0.1
Release:    1
Group:      System
Architecture: noarch
License:    TBD
Source0:    %{name}-%{version}.tar.bz2

%description
Sample content 

%package music
Summary:    Preloded Community Content Music
Group:      System

%description music
Sample Music content 

%package video
Summary:    Preloded Community Content Video
Group:      System

%description video
Sample Video content 

%package picture
Summary:    Preloded Community Content Picture
Group:      System

%description picture
Sample Picture content 

%prep
%setup -q -n %{name}-%{version}

%files music 
%defattr(-,nemo,nemo,-)
/home/nemo/Community-Music/*

%files video 
%defattr(-,nemo,nemo,-)
/home/nemo/Community-Video/*

%files picture 
%defattr(-,nemo,nemo,-)
/home/nemo/Community-Picture/*

%changelog
* Wed Sep 16 2016 Nokius
- first release
