""" PURPOSE:

	Each method in this file can be called with /[command] from a client.


	for example, /quit will cause the code in quit to be run.

   USAGE:

	Any command in this file MUST accept a server object, client, address
	and command_args. They need not use them, but they must accept them.

	Thus, this shall act as the docstring for each of those commands:

	Args:
		server_object(socket): The server that is being run. This is here to allow
					access to things in the server.
		command_args(list): A list of the arguments passed with the command.

	Finally, The /help command will show all available commands.
	Further, the docstring of each function will also be shown to the user, so
	that they have a better understanding of what each function does.
"""
def stop(server_object, command_args):
	"""
		Stops the server.
	"""

	import socket
	import os

	print("Started shutdown.")

	#: Terminate all looping threads.
	server_object.running = False

	#: Close the connection to each client.
	for client, addr in server_object.clientlist:
		server_object.close_client(client, addr, "Server Shutdown")

	server_object.server.close()

	print("Shutdown successful")

	#: Exit.
	os._exit(0)
