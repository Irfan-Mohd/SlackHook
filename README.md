# SlackHook

#### An automated script for checking if a __*slack incoming webhook URL*__ is valid or not

#### Slack webhook URL's are considered as sensitive tokens which if leaked can be used to craft pishing attacks on your workspace. Often these URL's are left unchecked in the organisation's repositories usually in dev or testing branch.

## Usage

This script takes a file contatining webhook URL's as an input

```python3 slackhook.py -f FILE```

