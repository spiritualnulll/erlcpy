
# erlcpy
A light-weight ~~script (turns out I was dumb)~~ API wrapper to interact with the ERLC API.
> working since June 9 :)

## Commmand list:
- [server_info](https://apidocs.policeroleplay.community/for-developers/api-reference#server): Fetches server status data. `GET`
- [players](https://apidocs.policeroleplay.community/for-developers/api-reference#server-players): Fetches a list of players currently in the server. `GET`
- [joinlogs](https://apidocs.policeroleplay.community/for-developers/api-reference#server-joinlogs): Fetches join logs data. `GET`
- [queuelist](https://apidocs.policeroleplay.community/for-developers/api-reference#server-queue): Fetches players currently in queue. `GET`
- [killlogs](https://apidocs.policeroleplay.community/for-developers/api-reference#server-killlogs): Fetches kill logs data. `GET`
- [command_logs](https://apidocs.policeroleplay.community/for-developers/api-reference#server-commandlogs): Fetches command logs data. `GET`
- [modcalls](https://apidocs.policeroleplay.community/for-developers/api-reference#server-modcalls): Fetches moderator call logs data. `GET`
- [bans](https://apidocs.policeroleplay.community/for-developers/api-reference#server-bans): Fetches bans data. `GET`
- [vehicles](https://apidocs.policeroleplay.community/for-developers/api-reference#server-vehicles): Fetches a list of spawned vehicles in the server. `GET`
- [cmd](https://apidocs.policeroleplay.community/for-developers/api-reference#server-command): Executes command on the server. `POST`

## How to use it?
First of all you need to initalize it using your **Server key** and your **Global API key** if you have one.
```python
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


**All `GET` commands return RAW json data! Refer the [ERLC API Documentation](https://apidocs.policeroleplay.community/for-developers/api-reference) to see how the json data is structured.**

## Credits
The API is by [PRC](https://twitter.com/PRC_Roblox).
