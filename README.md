# shuffler-discord-bot

Bot to shuffle or pick from lists of items or lists of users.

## Usage

`$help` basic information.

For the shuffle and pick commands, adding the `-dm` option will send the result to your dms.

### Shuffle

```
'$shuffle list item1 item2 item3' to shuffle items in list. 'shuffle item1 item2 item3' also works.
'$shuffle audio' to shuffle the members of the audio channel you're currently in.
'$shuffle role @role1 role2' to shuffle the members in roles @role1 and @role2.
```

### Pick

```
'$pick list 2 item1 item2 item3' to pick 2 items from the list (item1, item2, item3). 'pick 2 item1 item2 item3' also works.
'$pick audio 3' to pick 3 users from the audio channel you're currently in.
'$pick role 4 @role1 @role2' to pick 4 users from roles @role1 and @role2.
If you don't specify a number, one item will be chosen (i.e. 'pick item1 item2 item3')
```
