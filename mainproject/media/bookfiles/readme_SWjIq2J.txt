 Install instructions:

 1) Unpack & Install the software.
 2) Chose the license server for your desired platform:

    - ./darwin  - MacOSX  ( x86, x64 )
    - ./freebsd - FreeBSD ( x86, x64, arm )
    - ./linux   - Linux   ( x86, x64, arm, arm64 )
    - ./windows - Windows ( x86, x64 )
 
    You can either run the license server on your pc,
    or on a (dedicated) server. Independently of the
    platform, the license server can license clients
    of any platform.

 3) Copy the binary of the license server to a permanent
    directory, such as C:\dvt-jb-lic-server\ or 
    /opt/dvt-jb-lic-server/

 4.1) Windows:
    - Start a command prommpt as an Administrator.
    - Go to the directory, where you put the license
      server, using "cd".
    - Install the license server:

      x64: dvt-jb_licsrv.386.exe -mode install
      x64: dvt-jb_licsrv.amd64.exe -mode install

      This will install the license server as a 
      windows service. If you want to remove it
      again, use "-mode uninstall".

    - Open services.msc and start the service.
      Alternatively, use "net start" or reboot
      your pc/server.

 4.2) *nix:
   - Go to the directory, where you put the license
     server.

   - Execute, either as root or using sudo:

     dvt-jb_licsrv.[platform].[arch] -mode install

     where platform is your OS and arch is your system
     architecture. To uninstall, you can use -mode uninstall.
     This will install (depending on your service system)
     a new service.

   - Start this service using your standard service
     tools.

  5) Start the application and point it to the license server.
     If you are running the license server on the same host,
     you can point it to "http://127.0.0.1:1337". Otherwise, 
     use the ip or hostname of your license server.

  6) Enjoy!


