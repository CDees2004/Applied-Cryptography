#!/bin/bash

# Team Name: Encryptodes
# Members:Barry Dees, Niko Krause, Javen Wilson,
#         Steven Alleman, and Isiah Hinds.
#
# Bash scrypt to hash all values in the given
# dictionary and compare it to a given hash
# to reverse engineer the original password.


# iterating through every line of the dictionary text
# and hashing looking for a spedified hash to find
# the original password

target_hash="6a5800844860611cb761c82c8110afbbcfce5757526755b244c087e2dd40c15f"

while read line; do
	# storing each hashed string in the line iterable variable
	line_hash=$(echo -n "$line" | sha256sum | awk '{print $1}')
	if [ "$line_hash" == "$target_hash" ]; then
		# if the hash of the line matches our desired hash,
		# then return its associated password
		result_hash=$(sha256sum | awk '{print $2}')
		echo "Password associated with the hash: $line"
		break
	fi
done < "dictionary-1.txt"
