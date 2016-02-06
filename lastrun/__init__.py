from __future__ import print_function
import datetime
import pickle


def when():
    try:
        f = open('.lastrun', 'r')
        last = pickle.load(f)
        f.close()
        return last
    except:
        return None


def record():
    with open('.lastrun', 'w') as f:
        now = datetime.datetime.now()
        pickle.dump(now, f)
        return now


def recorder(first_run_log="It hasn't been run yet",
             last_run_log="%s since last run",
             printer=print):
    try:
        now = datetime.datetime.now()
        last = when()
        diff = now - last
        printer(last_run_log % diff)
        return diff
    except Exception as e:
        printer(first_run_log)
    finally:
        record()
