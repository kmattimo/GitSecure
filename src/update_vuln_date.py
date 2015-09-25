#!/usr/bin/python

import MySQLdb as mdb
import sys
from git import Repo
import shutil
import time



def get_conn():
    conn = mdb.connect('127.0.0.1', 'root', 'cisco123', 'analysis_replica', charset='latin1')
    return conn



conn = get_conn()
inner_conn = get_conn()
cursor = conn.cursor()

updates = 0


cursor.execute("select repo_id, repo_name, owner_name from gh_repo order by repo_id")
rows = cursor.fetchall()
cursor.close()


tot_rows = len(rows)
cur_row = 1
for repo_id, name, owner in rows:


    if (cur_row % 100) == 0:
        print '-------------------'
        print "(%d/%d) %d %s/%s, total updates %d" % (cur_row, tot_rows, repo_id, owner, name, updates)


    cur_row += 1

    inner_cursor = inner_conn.cursor()
    inner_cursor.execute("select v.vuln_id, v.vuln_desc, v.code_sample, f.filename from gh_vuln as v left join gh_file as f on v.file_id = f.file_id where f.repo_id = %s", (repo_id,))

    repo = None
    repo_dir = None
    inner_rows = inner_cursor.fetchall()
    #inner_cursor.close()


    for vuln_id, vuln_type, code_sample, filename in inner_rows:

        if repo is None:
            # clone repo
            git_url = 'https://user:pass@github.com/%s/%s.git' % (owner, name)
            repo_dir = '/tmp/repos/%d/' % (repo_id)
            try:
                repo = Repo.clone_from(git_url, repo_dir)
            except Exception as e:
                print 'Auth failed for repo %s (%d): %s' % (git_url, repo_id, str(e))
                break

        filename = filename[filename.index('/')+1:]

        #print ">>>>", repo_id, owner, name, vuln_id, filename.encode('ascii', 'ignore'), vuln_type
        fname = repo_dir + filename
        fname = ''.join([chr(ord(x)) for x in fname])   # why the fucking fuck unicode fuck youuuu
        try:
            for commit, lines in repo.blame('--before="2015-04-23 00:00"', fname):
                #print '        %s commit on %s (authored %s), %d lines' % (commit.committer, commit.committed_date, commit.authored_date, len(lines))
                if str(code_sample) in lines:
                    # Match!
                    authored_date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(commit.authored_date))
                    committed_date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(commit.committed_date))
                    inner_cursor.execute("update gh_vuln set date_written=%s, committed=%s where vuln_id=%s", (authored_date, committed_date, str(vuln_id)))
                    updates += 1
        except Exception as e:
            print 'Failed in repo %d, vuln %d: %s' % (repo_id, vuln_id, str(e))


    inner_cursor.close()
    if (cur_row % 100) == 0:
        inner_conn.commit()
    if repo is not None and repo_dir != '':
        shutil.rmtree(repo_dir)



inner_conn.commit()
