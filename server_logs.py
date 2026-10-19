    spec.loader.exec_module(lib)  # type: ignore
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^
  File "<frozen importlib._bootstrap_external>", line 1027, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/app/server_logs.py", line 99, in <module>
    from punishment_card import render_card, TYPE_STYLE, TITLE_WORD
ModuleNotFoundError: No module named 'punishment_card'
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "/app/welcome_bot.py", line 231, in <module>
    bot.run(TOKEN)
    ~~~~~~~^^^^^^^
  File "/app/.venv/lib/python3.13/site-packages/discord/client.py", line 933, in run
    asyncio.run(runner())
    ~~~~~~~~~~~^^^^^^^^^^
  File "/mise/installs/python/3.13.16/lib/python3.13/asyncio/runners.py", line 196, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "/mise/installs/python/3.13.16/lib/python3.13/asyncio/runners.py", line 119, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/mise/installs/python/3.13.16/lib/python3.13/asyncio/base_events.py", line 726, in run_until_complete
  File "/app/.venv/lib/python3.13/site-packages/discord/ext/commands/bot.py", line 965, in _load_from_module_spec
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/app/.venv/lib/python3.13/site-packages/discord/client.py", line 922, in runner
    raise errors.ExtensionFailed(key, e) from e
    await self.start(token, reconnect=reconnect)
  File "/app/.venv/lib/python3.13/site-packages/discord/client.py", line 850, in start
discord.ext.commands.errors.ExtensionFailed: Extension 'server_logs' raised an error: ModuleNotFoundError: No module named 'punishment_card'
    await self.login(token)
  File "/app/.venv/lib/python3.13/site-packages/discord/client.py", line 693, in login
    await self.setup_hook()
  File "/app/welcome_bot.py", line 180, in setup_hook
    await bot.load_extension("server_logs")  # server logs (server_logs.py)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/.venv/lib/python3.13/site-packages/discord/ext/commands/bot.py", line 1040, in load_extension
    await self._load_from_module_spec(spec, name)
[2026-10-19 19:42:39] [INFO    ] discord.client: logging in using static token
Traceback (most recent call last):
    ~~~~~~~~~~~^^^^^^^^^^
  File "/app/.venv/lib/python3.13/site-packages/discord/ext/commands/bot.py", line 962, in _load_from_module_spec
  File "/mise/installs/python/3.13.16/lib/python3.13/asyncio/runners.py", line 196, in run
    spec.loader.exec_module(lib)  # type: ignore
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^
    return runner.run(main)
  File "<frozen importlib._bootstrap_external>", line 1027, in exec_module
           ~~~~~~~~~~^^^^^^
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/mise/installs/python/3.13.16/lib/python3.13/asyncio/runners.py", line 119, in run
  File "/app/server_logs.py", line 99, in <module>
    from punishment_card import render_card, TYPE_STYLE, TITLE_WORD
ModuleNotFoundError: No module named 'punishment_card'
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "/app/welcome_bot.py", line 231, in <module>
    bot.run(TOKEN)
    ~~~~~~~^^^^^^^
  File "/app/.venv/lib/python3.13/site-packages/discord/client.py", line 933, in run
    asyncio.run(runner())
  File "/app/.venv/lib/python3.13/site-packages/discord/client.py", line 850, in start
    await self.login(token)
  File "/app/.venv/lib/python3.13/site-packages/discord/ext/commands/bot.py", line 965, in _load_from_module_spec
  File "/app/.venv/lib/python3.13/site-packages/discord/client.py", line 693, in login
    raise errors.ExtensionFailed(key, e) from e
discord.ext.commands.errors.ExtensionFailed: Extension 'server_logs' raised an error: ModuleNotFoundError: No module named 'punishment_card'
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/mise/installs/python/3.13.16/lib/python3.13/asyncio/base_events.py", line 726, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/app/.venv/lib/python3.13/site-packages/discord/client.py", line 922, in runner
    await self.start(token, reconnect=reconnect)
    await self.setup_hook()
  File "/app/welcome_bot.py", line 180, in setup_hook
    await bot.load_extension("server_logs")  # server logs (server_logs.py)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/.venv/lib/python3.13/site-packages/discord/ext/commands/bot.py", line 1040, in load_extension
    await self._load_from_module_spec(spec, name)
[2026-10-19 19:42:41] [INFO    ] discord.client: logging in using static token
Traceback (most recent call last):
  File "/app/.venv/lib/python3.13/site-packages/discord/ext/commands/bot.py", line 962, in _load_from_module_spec
    spec.loader.exec_module(lib)  # type: ignore
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^
  File "<frozen importlib._bootstrap_external>", line 1027, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/app/server_logs.py", line 99, in <module>
    from punishment_card import render_card, TYPE_STYLE, TITLE_WORD
ModuleNotFoundError: No module named 'punishment_card'
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "/app/welcome_bot.py", line 231, in <module>
    bot.run(TOKEN)
    ~~~~~~~^^^^^^^
  File "/app/.venv/lib/python3.13/site-packages/discord/client.py", line 933, in run
    asyncio.run(runner())
    ~~~~~~~~~~~^^^^^^^^^^
  File "/mise/installs/python/3.13.16/lib/python3.13/asyncio/runners.py", line 196, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "/mise/installs/python/3.13.16/lib/python3.13/asyncio/runners.py", line 119, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/mise/installs/python/3.13.16/lib/python3.13/asyncio/base_events.py", line 726, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/app/.venv/lib/python3.13/site-packages/discord/client.py", line 922, in runner
    await self.start(token, reconnect=reconnect)
  File "/app/.venv/lib/python3.13/site-packages/discord/client.py", line 850, in start
    await self.login(token)
  File "/app/.venv/lib/python3.13/site-packages/discord/client.py", line 693, in login
    await self.setup_hook()
  File "/app/welcome_bot.py", line 180, in setup_hook
    await bot.load_extension("server_logs")  # server logs (server_logs.py)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/.venv/lib/python3.13/site-packages/discord/ext/commands/bot.py", line 1040, in load_extension
    await self._load_from_module_spec(spec, name)
  File "/app/.venv/lib/python3.13/site-packages/discord/ext/commands/bot.py", line 965, in _load_from_module_spec
    raise errors.ExtensionFailed(key, e) from e
discord.ext.commands.errors.ExtensionFailed: Extension 'server_logs' raised an error: ModuleNotFoundError: No module named 'punishment_card'
