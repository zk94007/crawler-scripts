Installation
Requirements:
	- Python 3.x
		sudo apt-get install python3.6
	- Pip 3.x
		sudo apt install python3-pip
Running:
	# sites.csv: Site lists [in]
	# output.csv: Results [out]
	$ python3 crawler.py -i sites.csv -o output.csv
	
	# search.csv: Google search keywords [in]
	$ python3 crawler.py -s search.csv -o output.csv

	# proxies.csv: Proxy lists [in]
	$ python3 crawler.py -i sites.csv -o output.csv -p proxies.csv

	# matching.csv: matching lists [in]
	# result.csv: Results [out]
	$ python3 crawler.py -i sites.csv -o output.csv -m matching.csv -r result.csv
	$ python3 crawler.py -i sites.csv -o output.csv -m matching.csv -r result.csv -p proxies.csv