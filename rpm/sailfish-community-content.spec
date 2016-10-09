Name:       sailfish-community-content

Summary:    Preloded Community Content
Version:    0.0.1
Release:    1
Group:      System/GUI/Other
BuildArch:  noarch
License:    TBD
Source0:    %{name}-%{version}.tar.bz2
URL:		https://github.com/Nokius/sailfish-community-content

%description
Sample content 

%package music
Summary:    Preloded Community Content Music
Group:      System/GUI/Other

%description music
Sample Music content 

%package video
Summary:    Preloded Community Content Video
Group:      System/GUI/Other

%description video
Sample Video content 

%package picture
Summary:    Preloded Community Content Picture
Group:      System/GUI/Other

%description picture
Sample Picture content 

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}

# create Muisc conntent
mkdir -p %{buildroot}/home/nemo/Music/Community-Music
cp -R Community-Music/* %{buildroot}/home/nemo/Music/Community-Music/

# create Video conntent
mkdir -p %{buildroot}/home/nemo/Videos/Community-Video
cp -R Community-Video/* %{buildroot}/home/nemo/Videos/Community-Video/

# create Picture conntent
mkdir -p %{buildroot}/home/nemo/Pictures/Community-Picture
cp -R Community-Picture/* %{buildroot}/home/nemo/Pictures/Community-Picture/

%files music 
%defattr(644,nemo,nemo,755)
#%attr(-,nemo,nemo) /home/nemo/Music/Community-Music/*
%dir /home/nemo/Music/Community-Music
/home/nemo/Music/Community-Music/*

%files video 
%defattr(644,nemo,nemo,755)
#%attr(-,nemo,nemo) /home/nemo/Videos/Community-Video/*
/home/nemo/Videos/Community-Video/*

%files picture 
%defattr(644,nemo,nemo,755)
#%attr(-,nemo,nemo) /home/nemo/Pictures/Community-Picture/*
/home/nemo/Pictures/Community-Picture/*

%clean
rm -rf %{buildroot}

%changelog
* Wed Oct 08 2016 Nokius
- first release
