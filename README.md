# erlcpy
A light-weight script to interact with the ERLC API
-------

## Commmand list:
- server_info: Fetches server status data.
- players: Fetches a list of players currently in the server.
- joinlogs: Fetches join logs data.
- queuelist: Fetches players currently in queue.
- killlogs: Fetches kill logs data.
- command_logs: Fetches command logs data.
- modcalls: Fetches moderator call logs data.
- bans: Fetches bans data.
- vehicles: Fetches a list of spawned vehicles in the server.
- cmd: Executes command on the server.

## How to use it?
First of all you need to initalize it using your **server key** and if your **Global API key** if you have one
```python
#                               required                     not required           default = false and not required
              erlc = ERLC(server_key="your_server_key", global_key="your_global_key", debug=True)
```

- `server_key` is a required string.
- `global_key` is not required
- `debug` is a `True` or `False` statement, enabling it will result in logging being enabled which is just printing out logs.


Now you can use the features that come with the API!
```python
server_info = erlc.server_info() 
players = erlc.players()
join_logs = erlc.joinlogs()
queue_list = erlc.queuelist()
kill_logs = erlc.killlogs()
command_logs = erlc.command_logs()
mod_calls = erlc.modcalls()
bans = erlc.bans()
vehicles = erlc.vehicles()
command_response = erlc.cmd("kill LuckySpy_King") # ay thats me! don't kill me!!
```


**All commands return json data! Refer the [ERLC API Documentation](https://apidocs.policeroleplay.community/for-developers/api-reference) to see how the json data is strucutred.**

## Credits
The API is by [PRC](https://twitter.com/PRC_Roblox).
