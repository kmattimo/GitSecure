import save_data as sd

random_9726 = [359, 1522 , 417 , 1339 , 6808 , 3094 , 3025 , 4695 , 59 , 6650 , 5056 , 9073 , 6499 , 6125 , 3434 , 6462 , 9724 , 468 , 2358 , 2448 , 5427 , 2362 , 5860 , 2794 , 4084 , 5276 , 441 , 2123 , 6032 , 2257 , 8756 , 5335 , 5468 , 6741 , 6832 , 9476 , 7305 , 8189 , 1396 , 5035 , 9271 , 8343 , 502 , 5434 , 2283 , 193 , 1843 , 7542 , 4092 , 2165 , 5719 , 7142 , 3347 , 3261 , 6750 , 7813 , 648 , 6529 , 2951 , 7358 , 3550 , 9059 , 38 , 9681 , 8159 , 7781 , 8466 , 3381 , 6787 , 2861 , 4675 , 5371 , 1703 , 2037 , 7414 , 8244 , 4965 , 8756 , 4256 , 6754 , 8444 , 5588 , 7644 , 8792 , 4994 , 3905 , 5000 , 3857 , 7993 , 5832 , 7250 , 595 , 3971 , 8176 , 667 , 9076 , 5708 , 6313 , 5552 , 8291 , 5403 , 6252 , 6837 , 7937 , 5238 , 943 , 2647 , 5996 , 2073 , 6752 , 7306 , 5188 , 7395 , 2757 , 4859 , 46 , 2958 , 1899 , 172 , 6092 , 5576 , 7534 , 8569 , 1952 , 8729 , 3766 , 7580 , 6666 , 865 , 877 , 2080 , 1636 , 6501 , 6962 , 5666 , 2206 , 3230 , 4908 , 3589 , 2891 , 3826 , 4613 , 8369 , 5826 , 660 , 6396 , 1232 , 2190 , 3327 , 2092 , 7842 , 9223 , 401 , 6442 , 8430 , 1395 , 7630 , 5149 , 2377 , 2542 , 5542 , 7299 , 8386 , 5637 , 8920 , 8544 , 3539 , 4293 , 862 , 4095 , 8600 , 3880 , 2564 , 3651 , 8991 , 989 , 4494 , 2335 , 4806 , 1229 , 6423 , 1655 , 4391 , 1548 , 7227 , 5677 , 2572 , 7706 , 5624 , 3302 , 4426 , 4555 , 2372 , 3588 , 6377 , 3898 , 9130 , 8617 , 8342 , 1225 , 7815 , 5441 , 283 , 4030 , 7496 , 1148 , 6154 , 9024 , 6156 , 6714 , 3974 , 2250 , 2711 , 2303 , 4768 , 7683 , 8500 , 8766 , 3106 , 5065 , 7450 , 9115 , 618 , 5590 , 8 , 7395 , 7428 , 652 , 5559 , 2379 , 5142 , 2599 , 6081 , 2561 , 7093 , 6044 , 8122 , 6179 , 3274 , 1069 , 7195 , 9056 , 2477 , 2305 , 6371 , 6870 , 8374 , 6007 , 8065 , 5604 , 8323 , 5392 , 4965 , 7111 , 8558 , 4291 , 7945 , 7565 , 7334 , 5855 , 1836 , 1012 , 9143 , 5610 , 1359 , 5229 , 1160 , 9302 , 7737 , 8752 , 2479 , 4893 , 407 , 6172 , 5732 , 8332 , 4361 , 9058 , 2117 , 6375 , 9046 , 9141 , 1258 , 4558 , 4420 , 6664 , 6926 , 3636 , 3071 , 2938 , 197 , 131 , 8684 , 6523 , 2900 , 3137 , 6287 , 1498 , 2642 , 5874 , 3499 , 9509 , 8037 , 4703 , 497 , 1018 , 505 , 7005 , 6902 , 5486 , 4359 , 8851 , 1978 , 8497 , 692 , 1035 , 8420 , 8636 , 3232 , 9052 , 4108 , 9410 , 544 , 9466 , 9053 , 1238 , 8327 , 9277 , 4238 , 8445 , 5966 , 2153 , 6909 , 5880 , 3288 , 4216 , 4964 , 2580 , 5521 , 9572 , 1460 , 3149 , 5199 , 3562 , 8010 , 2989 , 2445 , 3549 , 5071 , 7558 , 6256 , 3608 , 270 , 5482 , 3456 , 2099 , 786 , 2606 , 1733 , 265 , 1895 , 7791 , 7346 , 7061 , 5558 , 9555 , 8725 , 3046 , 3338 , 203 , 214 , 4688 , 4375 , 9638 , 2446 , 4562 , 2025 , 1121 , 5823 , 2490 , 8202 , 6657 , 2596 , 2846 , 1931 , 5486 , 4234 , 7788 , 3678 , 5243 , 2352 , 4913 , 9390 , 6013 , 1290 , 8361 , 5358 , 8955 , 7248 , 2416 , 8241 , 7943 , 8939 , 1518 , 5481 , 6056 , 1888 , 3988 , 2214 , 8479 , 2776 , 7251 , 3457 , 310 , 1550 , 8755 , 8541 , 3951 , 2006 , 4785 , 6801 , 8388 , 923 , 9134 , 3351 , 7454 , 5940 , 1021 , 5584 , 7098 , 3160 , 7289 , 9217 , 5954 , 3456 , 5712 , 6573 , 8991 , 5902 , 5250 , 7571 , 4825 , 1968 , 5579 , 4294 , 1506 , 643 , 3026 , 2697 , 9292 , 6412 , 4465 , 4119 , 3852 , 1156 , 530 , 5249 , 7651 , 8895 , 8188 , 5496 , 8031 , 7114 , 9330 , 2095 , 410 , 2335 , 7028 , 2439 , 5128 , 6628 , 2509 , 8094 , 7840 , 3264 , 7118 , 5925 , 3224 , 3062 , 4850 , 6031 , 8493 , 6581 , 6813 , 8165 , 3310 , 6446 , 3421 , 8540 , 4606 , 2 , 9506 , 6197 , 7631 , 2025 , 2209 , 3298 , 4446 , 3840 , 3415]
#500
print len(random_9726)

db_conn = sd.get_connection("mysqlcreds-sample-c.csv")
cursor = db_conn.cursor()

for rand_id in random_9726:
	
	id_query = 	"select n.repo_id from (select distinct r.repo_id from gh_vuln v, gh_repo r, gh_file f where r.repo_id = f.repo_id and f.file_id = v.file_id and v.vuln_desc = 'strcpy' order by r.repo_id limit " +str(rand_id) + ") n order by  n.repo_id desc limit 1"
	cursor.execute(id_query);
	repo_id = int(cursor.fetchall()[0][0])
	#print str(rand_id) + ": " + str(repo_id)
	
	data_query = "select owner_name, repo_name, filename, code_sample, line_number, date_created, r.repo_id from gh_vuln v, gh_repo r, gh_file f where r.repo_id = f.repo_id and f.file_id = v.file_id and r.repo_id =" + str(repo_id) + " limit 100"
	cursor.execute(data_query)
	data = cursor.fetchall()
	
	owner_name = data[0][0]
	repo_name = data[0][1]
	filename = data[0][2]
	code_sample = data[0][3]
	line_number = data[0][4]
	date_created = data[0][5]
	
	URL1 = "https://github.com/" + str(owner_name) + "/" + str(repo_name)
	#print URL1
	URL2 = URL1 + "/blob/master/" + str(filename.split("/",1)[1])
	#print URL2
	#print(str(rand_id) + "	" + str(repo_id) + "	" + owner_name + "	" + repo_name + "	" + str(date_created) + "	" + filename + "	" + str(line_number) + "	" + code_sample)
	print(URL2 + "\t" + str(rand_id) + "\t" + str(repo_id) + "\t" + owner_name + "\t" + repo_name + "\t" + str(date_created) + "\t" + filename + "\t" + str(line_number) + "\t" + URL1 + "\t" + code_sample)