Name:       sailfish-community-content

Summary:    Preloded Community Content
Version:    0.0.1
Release:    1
Group:      System
BuildArch:  noarch
License:    TBD
Source0:    %{name}-%{version}.tar.bz2

%description
Sample content 

#%package music
#Summary:    Preloded Community Content Music
#Group:      System

#%description music
#Sample Music content 

#%package video
#Summary:    Preloded Community Content Video
#Group:      System

#%description video
#Sample Video content 

%package picture
Summary:    Preloded Community Content Picture
Group:      System

%description picture
Sample Picture content 

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}

# create Picture conntent
mkdir -p %{buildroot}/home/nemo/Pictures/Community-Picture
cp -R Community-Picture/* %{buildroot}/home/nemo/Pictures/Community-Picture/

#%files music 
#%defattr(-,nemo,nemo,-)
#/home/nemo/Music/Community-Music/*

#%files video 
#%defattr(-,nemo,nemo,-)
#/home/nemo/Videos/Community-Video/*

%files picture 
%defattr(-,nemo,nemo,-)
/home/nemo/Pictures/Community-Picture/*

%clean
rm -rf %{buildroot}

%changelog
* Wed Sep 16 2016 Nokius
- first release
