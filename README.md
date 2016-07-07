Summary
=======

Gets user emails for a channel on slack.

Notes
=====

15min hack. No error checking or anything nice like that.

Usage
=====

Get a slack API token from https://api.slack.com/docs/oauth-test-tokens

```
$ ./getslackemails.py -t <token> -c <channel_name>
```

Do not preface the channel name with #