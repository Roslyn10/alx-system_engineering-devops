0x0B-ssh

0. Use a private key

	Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu
	Requirements:
		* Only use ssh single-character flags
		* Cannot use -l
		* Do not need to handle the case of private key to protected by a passphrase

1. Create an SSH key pair

	Write a Bash script that creates an RSA key pair
	Requirements:
		* Name of the created private key must be school
		* Number of bits in the created key to be created 4096
		* The created key must be protected by the passphrase betty

2. Client configureation file

	Configure the machine to our need so that you can connect to a server without typing a password. Share the SSH client configuration in the answer file.
	Requirements:
		* SSH client configuration must be configured to use the private key ~/.ssh/school
		* SSH client configuration must be configured to refuse to authenticate using a password

3. Let me in!

	Add the SSH public key below to the server so that we can connect using the ubuntu user.
