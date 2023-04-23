# PYPI_Test

----------------

    C:\Users\Vicky\Desktop\Repository\Offline-File-Transfer>cd vicks

    C:\Users\Vicky\Desktop\Repository\Offline-File-Transfer\vicks>pip install vixsharefile --upgrade
    Collecting vixsharefile
      Downloading vixsharefile-0.0.1.tar.gz (2.2 kB)
      Preparing metadata (setup.py) ... done
    Building wheels for collected packages: vixsharefile
      Building wheel for vixsharefile (setup.py) ... done
      Created wheel for vixsharefile: filename=vixsharefile-0.0.1-py3-none-any.whl size=2138 sha256=59136962e7616fdfb8008b22ee56d15f6c9853a9f9a2b805ad3c7101e42dfdaa
      Stored in directory: c:\users\vicky\appdata\local\pip\cache\wheels\21\45\ea\523f84fa9e7ee630045483c82e15b0a6ebd4df704a7e2a6b28
    Successfully built vixsharefile
    Installing collected packages: vixsharefile
    Successfully installed vixsharefile-0.0.1

    C:\Users\Vicky\Desktop\Repository\Offline-File-Transfer\vicks>python
    Python 3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on wWarning:
    This Python interpreter is in a conda environment, but the environment has
    not been activated.  Libraries may fail to load.  To activate this environment
    please see https://conda.io/activation

    Type "help", "copyright", "credits" or "license" for more information.
    >>> from vixsharefile import run_server


    Try running below line to start sharing.

    from sharefile import run_server




    Access this link from any Device nearby.


     * Serving Flask app 'app'
     * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on all addresses (0.0.0.0)
     * Running on http://127.0.0.1:5000
     * Running on http://192.168.0.104:5000
    Press CTRL+C to quit
     * Restarting with watchdog (windowsapi)
     * Debugger is active!
     * Debugger PIN: 142-206-457
    192.168.0.104 - - [22/Apr/2023 11:53:45] "GET / HTTP/1.1" 200 -
    192.168.0.104 - - [22/Apr/2023 11:53:45] "GET /static/background.jpg HTTP/1.1" 404 -
    192.168.0.104 - - [22/Apr/2023 11:53:53] "GET / HTTP/1.1" 200 -
    192.168.0.104 - - [22/Apr/2023 11:53:53] "GET /static/background.jpg HTTP/1.1" 404 -
    192.168.0.104 - - [22/Apr/2023 11:53:56] "GET /logout/ HTTP/1.1" 302 -
    192.168.0.104 - - [22/Apr/2023 11:53:56] "GET / HTTP/1.1" 200 -
    192.168.0.104 - - [22/Apr/2023 11:53:56] "GET /static/background.jpg HTTP/1.1" 404 -
    192.168.0.104 - - [22/Apr/2023 11:54:01] "POST /login HTTP/1.1" 308 -
    192.168.0.104 - - [22/Apr/2023 11:54:01] "POST /login/ HTTP/1.1" 200 -
    192.168.0.104 - - [22/Apr/2023 11:54:01] "GET /login/static/background.jpg HTTP/1.1" 404 -
    192.168.0.104 - - [22/Apr/2023 11:54:03] "GET /register/ HTTP/1.1" 200 -
    192.168.0.104 - - [22/Apr/2023 11:54:03] "GET /register/static/background.jpg HTTP/1.1" 404 -
    192.168.0.104 - - [22/Apr/2023 11:54:09] "POST /register/ HTTP/1.1" 200 -
    192.168.0.104 - - [22/Apr/2023 11:54:10] "GET /register/static/background.jpg HTTP/1.1" 404 -
    192.168.0.104 - - [22/Apr/2023 11:54:13] "POST /login HTTP/1.1" 308 -
    192.168.0.104 - - [22/Apr/2023 11:54:13] "POST /login/ HTTP/1.1" 302 -
    192.168.0.104 - - [22/Apr/2023 11:54:13] "GET / HTTP/1.1" 200 -
    192.168.0.104 - - [22/Apr/2023 11:54:14] "GET /static/background.jpg HTTP/1.1" 404 -
    192.168.0.104 - - [22/Apr/2023 11:54:47] "POST / HTTP/1.1" 200 -
    192.168.0.104 - - [22/Apr/2023 11:54:47] "GET /static/background.jpg HTTP/1.1" 404 -
    192.168.0.104 - - [22/Apr/2023 11:54:54] "GET / HTTP/1.1" 200 -
    192.168.0.104 - - [22/Apr/2023 11:54:54] "GET /static/background.jpg HTTP/1.1" 404 -
    192.168.0.104 - - [22/Apr/2023 11:54:58] "GET /static/imvickykumar999/3F4BE5DC454B3D5AB44C3D5C72B2AA8E_video_dashinit.mp4 HTTP/1.1" 200 -
    192.168.0.104 - - [22/Apr/2023 11:54:59] "GET /static/imvickykumar999/3F4BE5DC454B3D5AB44C3D5C72B2AA8E_video_dashinit.mp4 HTTP/1.1" 206 -
