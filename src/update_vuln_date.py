#!/usr/bin/python

import MySQLdb as mdb
import sys
from git import Repo


def get_conn():
    conn = mdb.connect('127.0.0.1', 'root', 'cisco123', 'analysis_replica', charset='utf8')
    return conn



conn = get_conn()
inner_conn = get_conn()
cursor = conn.cursor()


cursor.execute("select repo_id, repo_name, owner_name from gh_repo limit 10")
rows = cursor.fetchall()
cursor.close()
for repo_id, name, owner in rows:
    print '-------------------'
    print "%d %s/%s" % (repo_id, owner, name)

    inner_cursor = inner_conn.cursor()
    inner_cursor.execute("select v.vuln_id, v.vuln_desc, v.code_sample, f.filename from gh_vuln as v left join gh_file as f on v.file_id = f.file_id where f.repo_id = %s", (repo_id,))

    first = True
    for vuln_id, vuln_type, code_sample, filename in inner_cursor.fetchall():

        if first:
            # clone repo
            git_url = 'https://github.com/%s/%s.git' % (owner, name)
            Repo.clone_from(git_url, '/tmp/repos/%d' % (repo_id))
        first = False

        print repo_id, owner, name, vuln_id, filename.encode('ascii', 'ignore'), vuln_type



    inner_cursor.close()
