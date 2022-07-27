# 0x04. Loops, conditions and parsing

## Resources

- [Loops sample](https://alx-intranet.hbtn.io/rltoken/wT98UJfv_E2tk4yP9PcLLw)
- [Variable assignment and arithmetic](https://alx-intranet.hbtn.io/rltoken/olvOKX699pq50rkHRE5cSA)
- [Comparison operators](https://alx-intranet.hbtn.io/rltoken/HxohzllkOWh0t4dy_HptIQ)
- [File test operators](https://alx-intranet.hbtn.io/rltoken/g8of2ABPEJfCNtPrDQaqVw)
- [Make your scripts portable](https://alx-intranet.hbtn.io/rltoken/O0Ay21p7tDhfLMsYbtAKug)
- [Linux and Mac OS users](https://alx-intranet.hbtn.io/rltoken/Cy1plV2eR3VphjPqliXB8A)
- [Windows users](https://alx-intranet.hbtn.io/rltoken/PXriGT0IKaSXC7L5l0CVag)
- [Data centers](https://alx-intranet.hbtn.io/rltoken/nDPzEm5SYxcdGxP_OpVYXQ)
- [IFS (internal field separator)](https://alx-intranet.hbtn.io/rltoken/8VeAz2XHCtuECDJ0PfMNIg)
- [Understanding /etc/passwd](https://alx-intranet.hbtn.io/rltoken/jm2-sSa3VlvI4zgRdreAsg)

**man or help:**

- `env`
- `cut`
- `for`
- `while`
- `until`
- `if`
- `ssh-keygen`
- `read`

## Objectives

To be able to explain:

- How to create SSH keys
- What is the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
- How to use `while`, `until` and `for` loops
- How to use `if`, `else`, `elif` and `case` condition statements
- How to use the `cut` command
- What are files and other comparison operators, and how to use them

## More Info

### Shellcheck

[Shellcheck](https://alx-intranet.hbtn.io/rltoken/joK6l_yEZ9N7T0GQ1RDjLA) is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. `Shellcheck` is your friend!
Here is how to [install it](https://alx-intranet.hbtn.io/rltoken/jbz0_-i3TV3WpKgxhyrtpA).

For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code `SC2034`, you can browse https://github.com/koalaman/shellcheck/wiki/SC2034.

## Tasks

| Files                                                          | Description                                                                                                                                                                                                               |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [0-RSA_public_key.pub](0-RSA_public_key.pub)                   | Public ssh key for RSA key pair                                                                                                                                                                                           |
| [1-for_best_school](1-for_best_school)                         | Bash script that displays Best School 10 times using for loop                                                                                                                                                             |
| [2-while_best_school](2-while_best_school)                     | Bash script that displays Best School 10 times using while loop                                                                                                                                                           |
| [3-until_best_school](3-until_best_school)                     | Bash script that displays Best School 10 times using until loop                                                                                                                                                           |
| [4-if_9_say_hi](4-if_9_say_hi)                                 | Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line                                                                                                 |
| [5-4_bad_luck_8_is_your_chance](5-4_bad_luck_8_is_your_chance) | Bash script that loops from 1 to 10                                                                                                                                                                                       |
| [6-superstitious_numbers](6-superstitious_numbers)             | Bash script that displays numbers from 1 to 20                                                                                                                                                                            |
| [7-clock](7-clock)                                             | Bash script that displays the time for 12 hours and 59 minutes                                                                                                                                                            |
| [8-for_ls](8-for_ls)                                           | Bash script that displays The content of the current directory, In a list format, Where only the part of the name after the first dash is displayed                                                                       |
| [9-to_file_or_not_to_file](9-to_file_or_not_to_file)           | Bash script that gives you information about the school file                                                                                                                                                              |
| [10-fizzbuzz](10-fizzbuzz)                                     | Bash script that displays numbers from 1 to 100                                                                                                                                                                           |
| [100-read_and_cut](100-read_and_cut)                           | Bash script that displays username, user id and home directory for each line of /etc/passwd                                                                                                                               |
| [101-tell_the_story_of_passwd](101-tell_the_story_of_passwd)   | Bash script that displays a story with each line of /etc/passwd                                                                                                                                                           |
| [102-lets_parse_apache_logs](102-lets_parse_apache_logs)       | Bash scripts that parses an Apache log file and displays the IP and HTTP code for each visitor using awk                                                                                                                  |
| [103-dig_the-data](103-dig_the-data)                           | Bash script that parses an Apache log file and displays the IP and HTTP code for each visitor, along with the number of occurences using awk ordered from the greatest to the lowest number of occurrences in list format |
