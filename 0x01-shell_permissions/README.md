Directory for 0x01-shell_permissions.

0-iam_betty script changes your user ID to 'betty'.
1-who_am_i script prints the effective userid of the current user.
2-groups script prints all the groups the current user is a part of.
3-new_owner script changes the owner of the file 'hello' to the user 'betty'.
4-empty script creates and empty file called 'hello'.
5-execute script adds execute permission to the owner of the file 'hello'.
6-multiple_permissions script adds execute permissions to the owner and the group owner, and read permission to other 
users, to the file 'hello'.
7-everybody script adds execution permission to the owner, the group owner and the other users, to the file 'hello'.
8-James_Bond script sets the owner and group as having no permissions, but all other users full permissions, to the file 'hello'.
9-John_Doe script sets permissions as full access for the owner, read and execute for the group, and write and execute for all other users, for the file 'hello'.
10-mirror_permissions sets the permissions for the file 'hello' to that of 'olleh'.
11-