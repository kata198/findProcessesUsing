# findProcessesUsing
Scans all running applications on a host to identify those using a shared library, or an executable, or some other mapping.


This application works on UNIX-derived systems (Linux, BSD, etc). You can use it, for example, to scan for processes using a certain version of a shared library, or running under a certain interpreter. It can print a summarized view, or optionally print all matching mappings as well.

This could be paired with https://github.com/kata198/remote_copy_and_execute to do audits of running software/library usage across many machines on a network.


You must be root to scan all running processes, otherwise this will only scan that which is running under your current user.

Example Usage
=============

	]$ sudo findProcessesUsing libc | head -n 20 | tail -n5
	Found libc in 803 (john) [ -bash  ]
	Found libc in 1060 (john) [ /usr/lib/tracker/tracker-extract  ]
	Found libc in 1062 (www) [ /usr/bin/httpd  ]
	Found libc in 808 (frankl) [ /bin/sh /usr/bin/startx  ]
	Found libc in 1065 (frankl) [ /usr/lib/tracker/tracker-miner-user-guides  ]

