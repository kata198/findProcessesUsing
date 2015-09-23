# findProcessesUsing
Scans all running applications on a host to identify those using a shared library, or an executable, some other mapping, or an open file descriptor.


This application works on UNIX-derived systems (Linux, BSD, cygwin, etc). You can use it, for example, to scan for processes using a certain version of a shared library, or running under a certain interpreter. It can print a summarized view, or optionally print all matching mappings as well.

This application can also scan for open files, either fully qualified or partially qualified.

This could be paired with https://github.com/kata198/remote_copy_and_execute to do audits of running software/library usage across many machines on a network.


You must be root to scan all running processes, otherwise this will only scan that which is running under your current user.


Usage
-----
	Usage: findProcessesUsing (options) [search portion]

	Searches all running processes for those containing a given mapping, or an open file (with -f).
	Mappings include running executables (like python), or a shared library, or a device.

		Options:

			-v or --verbose        Also print mapping lines containing the given pattern, or matched filenames when given -f.
			-e or --exact          Require exact match. Default is to allow partial matches
			-p or --pids-only      Only print pids, one per line

			-f                     Scan for open files instead of mappings. This should not be a symbolic link.
			--version              Print the version


	Examples:
	  findProcessesUsing libpython2.7             # Scan for any processes linking against anything containing "libpython2.7"
	  findProcessesUsing -f /var/lib/data.db      # Scan for any processes with an open handle to "/var/lib/data.db"


	It is recommended to run this process as root, otherwise you are only able to scan your own processes.


Example Usage
-------------

Scan for mappings of libc


	]$ sudo findProcessesUsing libc | head -n 20 | tail -n5
	Found libc in 803 (john) [ -bash  ]
	Found libc in 1060 (john) [ /usr/lib/tracker/tracker-extract  ]
	Found libc in 1062 (www) [ /usr/bin/httpd  ]
	Found libc in 808 (frankl) [ /bin/sh /usr/bin/startx  ]
	Found libc in 1065 (frankl) [ /usr/lib/tracker/tracker-miner-user-guides  ]


Scan for open file descriptor of pty


	]$ ./findProcessesUsing -f -v pty

	Found pty {fd=0,1,2,31} in 2384 (user1) [ /bin/bash  ]

			   0 = "/dev/pty1"
			   1 = "/dev/pty1"
			   2 = "/dev/pty1"
			  31 = "/dev/pty1"

	Found pty {fd=3} in 5732 (user1) [ SCREEN  ]

			   3 = "/dev/pty0"

	Found pty {fd=0,1,2} in 6184 (user1) [ screen  ]

			   0 = "/dev/pty0"
			   1 = "/dev/pty0"
			   2 = "/dev/pty0"

	Found pty {fd=0,1,2} in 5772 (user1) [ python  ]

			   0 = "/dev/pty2"
			   1 = "/dev/pty2"
			   2 = "/dev/pty2"

	Found pty {fd=0,1,2,31} in 6672 (user1) [ -bash  ]

			   0 = "/dev/pty0"
			   1 = "/dev/pty0"
			   2 = "/dev/pty0"
			  31 = "/dev/pty0"

	Found pty {fd=0,1,2,31} in 6072 (user1) [ /bin/bash  ]

			   0 = "/dev/pty3"
			   1 = "/dev/pty3"
			   2 = "/dev/pty3"
			  31 = "/dev/pty3"

	Found pty {fd=0,1,2,31} in 4796 (user1) [ /bin/bash  ]

			   0 = "/dev/pty2"
			   1 = "/dev/pty2"
			   2 = "/dev/pty2"
			  31 = "/dev/pty2"

