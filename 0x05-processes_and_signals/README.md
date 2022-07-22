# 0x05. Processes and signals

## Resources

**Read or watch:**

- [Linux PID](https://alx-intranet.hbtn.io/rltoken/zh33PXDR6w_qyu7zXUezmw)
- [Linux process](https://alx-intranet.hbtn.io/rltoken/px2TdWSjVO8i9SB5gHchAw)
- [Linux signal](https://alx-intranet.hbtn.io/rltoken/0NIee0VXMrEp36CFR85GIA)
- [Ignoring shellcheck error](https://alx-intranet.hbtn.io/rltoken/vErRT8QGU2bwJ6FLvPLzxw)
- [&](https://alx-intranet.hbtn.io/rltoken/R4YSgPT1k0PhWCrB0TYzoQ)
- [init.d](https://alx-intranet.hbtn.io/rltoken/sVqN4oNYYO6ojS4ctT02Jw)
- [Daemon](https://alx-intranet.hbtn.io/rltoken/kCoQ5aYO3towdDQFVPcfNg)
- [Positional parameters](https://alx-intranet.hbtn.io/rltoken/TJ2rxUwRsnM1mJQHSCnOQA)
- [what a zombie process is](https://alx-intranet.hbtn.io/rltoken/Tb86ZoSxR6ORCKYlZaYzHw)

**man or help:**

- `ps`
- `pgrep`
- `pkill`
- `kill`
- `exit`
- `trap`
- `sudo`

## Objectives

To be able to explain:

- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

### More Info

To know more and learn about all signals, check out [this article](https://alx-intranet.hbtn.io/rltoken/BOU-KVNMqfKEIBo_VOI26A).

## Tasks

| Files                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [0-what-is-my-pid](0-what-is-my-pid)                                                   | Bash script that displays its own PID                                                                                                                                                                                                                                                                                                                                       |
| [1-list_your_processes](1-list_your_processes)                                         | Bash script that displays a list of currently running processes in a user-oriented format / process hierarchy                                                                                                                                                                                                                                                               |
| [2-show_your_bash_pid](2-show_your_bash_pid)                                           | Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.                                                                                                                                                                                                                                                     |
| [3-show_your_bash_pid_made_easy](3-show_your_bash_pid_made_easy)                       | Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.                                                                                                                                                                                                                                                              |
| [4-to_infinity_and_beyond](4-to_infinity_and_beyond)                                   | Bash script that displays To infinity and beyond indefinitely                                                                                                                                                                                                                                                                                                               |
| [5-dont_stop_me_now](5-dont_stop_me_now)                                               | Bash script that stops 4-to_infinity_and_beyond process.                                                                                                                                                                                                                                                                                                                    |
| [6-stop_me_if_you_can](6-stop_me_if_you_can)                                           | Bash script that stops 4-to_infinity_and_beyond process.                                                                                                                                                                                                                                                                                                                    |
| [7-highlander](7-highlander)                                                           | Bash script that displays "To infinity and beyond" indefinitely with a sleep 2 in between each iteration and "I am invincible!!!" when receiving a SIGTERM signal                                                                                                                                                                                                           |
| [8-beheaded_process](8-beheaded_process)                                               | Bash script that kills the process 7-highlander                                                                                                                                                                                                                                                                                                                             |
| [100-process_and_pid_file](100-process_and_pid_file)                                   | Bash script that: creates the file `/var/run/myscript.pid` containing its PID, displays `To infinity and beyond` indefinitely, displays `I hate the kill command` when receiving a SIGTERM signal, displays `Y U no love me?`! when receiving a SIGINT signal and deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal |
| [manage_my_process](manage_my_process), [101-manage_my_process](101-manage_my_process) | `manage_my_process` is a Bash script that indefinitely writes `I am alive!` to the file `/tmp/my_process` while pausing for 2 seconds in between each message and `101-manage_my_process` is a Bash script that manages `manage_my_process`                                                                                                                                 |
| [102-zombie.c](102-zombie.c)                                                           | A C program that creates 5 zombie processes each displaying `Zombie process created, PID: ZOMBIE_PID`.                                                                                                                                                                                                                                                                      |
